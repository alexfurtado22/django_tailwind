document.addEventListener('DOMContentLoaded', function () {
  const mobileMenuButton = document.getElementById('mobile-menu-button')
  const mobileMenu = document.getElementById('mobile-menu')
  const menuIcon = document.getElementById('menu-icon')
  const closeIcon = document.getElementById('close-icon')

  mobileMenuButton.addEventListener('click', function () {
    const isOpen = mobileMenu.classList.toggle('hidden') // Toggle menu visibility
    menuIcon.classList.toggle('hidden', !isOpen) // Show hamburger when menu is hidden
    closeIcon.classList.toggle('hidden', isOpen) // Show close icon when menu is open
  })
})
