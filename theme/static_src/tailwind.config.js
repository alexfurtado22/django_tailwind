/**
 * This is a minimal config.
 *
 * If you need the full config, get it from here:
 * https://unpkg.com/browse/tailwindcss@latest/stubs/defaultConfig.stub.js
 */

module.exports = {
  content: [
    // Templates within theme app
    '../templates/**/*.html',

    // Main templates directory
    '../../templates/**/*.html',
    './templates/**/*.html', // Watch Django template files for class usage
    './static_src/src/**/*.css', // Include source CSS files

    // Templates in other apps
    '../../**/templates/**/*.html',

    // Include JavaScript/TypeScript files in static_src (if Tailwind classes are used)
    '../../static_src/**/*.{js,jsx,ts,tsx}',

    // Ignore node_modules to avoid unnecessary processing
    '!../../**/node_modules',

    /**
     * Python: If you use Tailwind CSS classes in Python, uncomment the following line
     * and make sure the pattern below matches your project structure.
     */
    // '../../**/*.py'
  ],
  theme: {
    extend: {},
  },
  plugins: [
    /**
     * '@tailwindcss/forms' is the forms plugin that provides a minimal styling
     * for forms. If you don't like it or have own styling for forms,
     * comment the line below to disable '@tailwindcss/forms'.
     */
    require('@tailwindcss/forms'),
    require('@tailwindcss/typography'),
    require('@tailwindcss/aspect-ratio'),
  ],
}
