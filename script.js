// Nav toggle for mobile
const nav = document.getElementById('nav');
const navToggle = document.getElementById('navToggle');
navToggle.addEventListener('click', ()=>{
  nav.classList.toggle('show');
});

// Simple form handler (no backend) - shows a message
const form = document.getElementById('contactForm');
const formMsg = document.getElementById('formMsg');
form.addEventListener('submit', (e)=>{
  e.preventDefault();
  const name = document.getElementById('name').value.trim();
  formMsg.textContent = `Cảm ơn ${name || 'bạn'}! Tin nhắn của bạn đã được gửi.`;
  form.reset();
  setTimeout(()=> formMsg.textContent = '', 5000);
});
