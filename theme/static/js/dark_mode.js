document.addEventListener('DOMContentLoaded', () => {
  const toggleButton = document.getElementById('dark-mode-toggle')
  const htmlElement = document.documentElement
  const sunIcon = document.getElementById('sun-icon')
  const moonIcon = document.getElementById('moon-icon')

  // Load initial preference from cookies
  const isDarkMode = document.cookie.split('; ').some((cookie) => cookie === 'dark_mode=true')
  if (isDarkMode) {
    htmlElement.classList.add('dark')
    sunIcon.classList.add('hidden')
    moonIcon.classList.remove('hidden')
  } else {
    htmlElement.classList.remove('dark')
    sunIcon.classList.remove('hidden')
    moonIcon.classList.add('hidden')
  }

  // Toggle dark mode on button click
  toggleButton.addEventListener('click', () => {
    const darkModeEnabled = htmlElement.classList.toggle('dark')
    document.cookie = `dark_mode=${darkModeEnabled}; path=/`

    // Toggle icon visibility
    if (darkModeEnabled) {
      sunIcon.classList.add('hidden')
      moonIcon.classList.remove('hidden')
    } else {
      sunIcon.classList.remove('hidden')
      moonIcon.classList.add('hidden')
    }
  })
})
