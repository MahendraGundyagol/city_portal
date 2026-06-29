// This example adds a subtle hover effect to back button with JavaScript (optional)
const backBtn = document.querySelector('.back-btn');

backBtn.addEventListener('mouseenter', () => {
  backBtn.style.transform = 'scale(1.2)';
});

backBtn.addEventListener('mouseleave', () => {
  backBtn.style.transform = 'scale(1)';
});
