document.addEventListener('DOMContentLoaded', () => {
    const userBtn = document.getElementById('user-icon-btn');
    const dropdown = document.getElementById('user-dropdown');

    userBtn.addEventListener('click', (e) => {
      e.stopPropagation(); // Para que no se cierre de inmediato
      dropdown.classList.toggle('hidden'); // Muestra u oculta el menú
    });

    document.addEventListener('click', (e) => {
      if (!userBtn.contains(e.target) && !dropdown.contains(e.target)) {
        dropdown.classList.add('hidden'); // Oculta si se hace clic afuera
      }
    });
  });