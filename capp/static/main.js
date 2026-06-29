document.addEventListener('DOMContentLoaded',()=>{

    const login = document.getElementsByClassName("login-box");

    const btn = document.querySelector("#butt");

    const log = login[0];

    btn.addEventListener('click', ()=>{
        console.log("before log")
        login[0].sty = 'block';
        console.log("After log")
    })
})
const video = document.getElementById('cityVideo');
const factBox = document.getElementById('factBox');

const funFacts = [
  {start: 2, end: 8, text: "Belagavi is known as 'Kundina Nagari' and has rich cultural heritage."},
  {start: 10, end: 16, text: "The Suvarna Vidhana Soudha is an architectural marvel in the city."},
  {start: 18, end: 24, text: "Belagavi is famous for its delicious cuisine and sweets."},
  {start: 26, end: 32, text: "The city hosts vibrant festivals like Kar Hunnime and Kambala."},
  {start: 34, end: 40, text: "Belagavi has several historic forts and temples to explore."},
];

// Set initial state for autoplay
video.volume = 1;
video.muted = true;

// Toggle play/pause and unmute on click
video.addEventListener('click', () => {
  if (video.paused) {
    video.play().then(() => {
      video.muted = false;
    }).catch((err) => {
      console.log("Play error:", err);
    });
  } else {
    video.pause();
  }
});

// Show/hide fun facts
video.addEventListener('timeupdate', () => {
  const currentTime = video.currentTime;
  const fact = funFacts.find(f => currentTime >= f.start && currentTime <= f.end);

  if (fact) {
    factBox.style.display = 'block';
    factBox.textContent = fact.text;
  } else {
    factBox.style.display = 'none';
  }
});
