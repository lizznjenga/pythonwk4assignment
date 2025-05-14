const toggleBtn = document.getElementById('toggleThemeBtn');

document.addEventListener('DOMContentLoaded', () => {
    const savedTheme = localStorage.getItem('theme') || 'light';
    document.body.classList.add(savedTheme);
  });

  toggleBtn.addEventListener('click', () => {
    document.body.classList.toggle('dark');
    document.body.classList.toggle('light');

    const currentTheme = document.body.classList.contains('dark') ? 'dark' : 'light';
  localStorage.setItem('theme', currentTheme);

  toggleBtn.classList.add('bounce');

  toggleBtn.addEventListener('animationend', () => {
    toggleBtn.classList.remove('bounce');
  }, { once: true });
});