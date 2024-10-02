const switchInput = document.getElementById('switch');

// Función para actualizar el tema en base a localStorage
const applyTheme = () => {
  // Verificamos el valor en localStorage para aplicar el tema adecuado
  const theme = localStorage.getItem('theme');
  if (theme === 'dark') {
    document.documentElement.setAttribute('data-theme', 'dark');
    switchInput.checked = true;  // Aseguramos que el switch esté en la posición correcta
  } else {
    document.documentElement.setAttribute('data-theme', 'light');
    switchInput.checked = false;
  }
};

// Aplicar el tema al cargar la página
applyTheme();

switchInput.addEventListener('change', () => {
  if (switchInput.checked) {
    document.documentElement.setAttribute('data-theme', 'dark');
    localStorage.setItem('theme', 'dark');
  } else {
    document.documentElement.setAttribute('data-theme', 'light');
    localStorage.setItem('theme', 'light');
  }
});