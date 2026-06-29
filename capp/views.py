from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.conf import settings
from .models import HomepageImage
from django.core.mail import send_mail


def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
def tourism(request):
    return render(request, 'tourism.html')
def development(request):
    return render(request, 'development.html')
def services(request):
    return render(request, 'services.html')
def health(request):
    return render(request, 'health.html')   
def education(request):
    return render(request, 'education.html')
def water_power_view(request):
    return render(request, 'water_power.html')


def signup(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        
        if User.objects.filter(username=uname).exists():
            messages.error(request, "Username already taken")
            return redirect('signup')

        if pass1 != pass2:
            messages.error(request, "Passwords do not match")
            return redirect('signup')
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered")
            return redirect('login')
         # Create inactive user
        user = User.objects.create_user(uname, email, pass1)
        user.is_active = False
        user.save()

        # Create token & uid
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = default_token_generator.make_token(user)

        # Build activation URL
        activation_link = f"http://127.0.0.1:8000/activate/{uid}/{token}/"

        # Send email
        subject = "Activate Your Account"
        message = render_to_string('email/activation_email.html', {
            'user': user,
            'activation_link': activation_link
        })

        email_message = EmailMessage(subject, message, to=[email])
        email_message.content_subtype = "html"
        email_message.send()
       
        messages.success(request, "Check your email to activate your account.")
        return redirect('login')
    return render(request, 'signup.html')  


def loginPage(request):
    from django.contrib.auth import authenticate, login

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pass')  # This matches your form's input name

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect('index')  # Redirect to homepage or dashboard
        else:
            messages.error(request, "Invalid username or password")
            return redirect('login')

    return render(request, 'login.html')
from django.utils.encoding import force_str

def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, "Account activated! You can now log in.")
        return redirect('login')
    else:
        messages.error(request, "Activation link is invalid!")
        return redirect('signup')
    

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        subject = f"Message from {name}"
        full_message = f"From: {name} <{email}>\n\n{message}"

        try:
            send_mail(subject, full_message, email, ['ishwarkalloli956@gmail.com'])  # Recipient
            messages.success(request, "Your message has been sent successfully!")
        except Exception as e:
            messages.error(request, f"Failed to send message. Error: {str(e)}")

        return redirect('contact')

    return render(request, 'contact.html')

   


   


