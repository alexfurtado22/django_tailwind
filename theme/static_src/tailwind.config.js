import plugin from 'tailwindcss/plugin'

const config = {
  darkMode: ['class'],
  content: [
    // Ensure Django template files are watched
    '../templates/**/*.html',
    '../../templates/**/*.html',
    './templates/**/*.html',

    // Include Tailwind classes from static CSS and JS/TS files
    './static_src/src/**/*.{css,js,jsx,ts,tsx}',
    '../../static_src/src/**/*.{css,js,jsx,ts,tsx}',

    // Ignore node_modules to prevent unnecessary processing
    '!../../node_modules/**',

    /**
     * Python: If you use Tailwind CSS classes in Python, uncomment the following line
     * and make sure the pattern below matches your project structure.
     */
    // '../../**/*.py'
  ],
  prefix: '',
  theme: {
    screens: {
      xxs: '240px',
      xs: '384px',
      sm: '512px',
      md: '672px',
      lg: '768px',
      xlg: '1024px',
      xxl: '1440px',
      xxxl: '1920px',
    },
    extend: {
      fontFamily: {
        sans: ['InterVariable', 'sans-serif'],
        serif: ['Playfair Display', 'serif'],
      },
      colors: {
        'clr-neon-pink': 'var(--clr-neon-pink)',
        'clr-yellow': 'var(--clr-yellow)',
        'clr-destructive': 'var(--clr-destructive)',
        'clr-pink': 'var(--clr-pink)',
        card: 'var(--card)',
        background: 'var(--background)',
        background2: 'var(--background2)',
        background3: 'var(--background3)',
        text1: 'var(--text1)',
        text2: 'var(--text2)',
        text3: 'var(--text3)',
        textshadow: 'var(--textshadow)',
        textshadow2: 'var(--textshadow2)',
        border: 'var(--border)',
        shadowlight: 'var(--shadowlight)',
        shadowstrong: 'var(--shadowstrong)',
        muted: 'var(--muted)',
        input: 'var(--text1)',
        'input-bg': 'var(--input-bg)',
        'input-placeholder': 'var(--input-placeholder)',
        ring: 'var(--ring-color)',
        'ring-focus': 'var(--ring-focus)',
      },
      fontSize: {
        'fluid-00': 'clamp(.50rem, 2vw, 1rem)',
        'fluid-0': 'clamp(.75rem, 2vw, 1rem)',
        'fluid-base': 'clamp(1.125rem, 3vw, 1.5rem)',
        'fluid-1': 'clamp(1rem, 4vw, 1.5rem)',
        'fluid-2': 'clamp(1.5rem, 6vw, 2.5rem)',
        'fluid-3': 'clamp(2rem, 9vw, 3.5rem)',
        'fluid-4': 'clamp(2rem, 4vw, 3rem)',
        'fluid-5': 'clamp(4rem, 5vw, 5rem)',
        'fluid-6': 'clamp(5rem, 7vw, 7.5rem)',
        'fluid-7': 'clamp(7.5rem, 10vw, 10rem)',
        'fluid-8': 'clamp(10rem, 20vw, 15rem)',
        'fluid-9': 'clamp(15rem, 30vw, 20rem)',
        'fluid-10': 'clamp(20rem, 40vw, 30rem)',
      },
    },
  },
  plugins: [
    require('@tailwindcss/forms'),
    require('@tailwindcss/typography'),
    require('@tailwindcss/aspect-ratio'),
    require('@tailwindcss/container-queries'),
    require('tailwindcss-animate'),
    plugin(function ({ addUtilities }) {
      const newUtilities = {
        '.holder': {
          width: '100%',
          marginLeft: 'auto',
          marginRight: 'auto',
          paddingLeft: '0.5rem',
          paddingRight: '0.5rem',
          border: '1px solid red',
        },
        '.text-shadow': {
          textShadow: '0 0 10px var(--textshadow), 0 0 25px var(--textshadow2)',
        },
        '.section': {
          marginTop: '5rem',
        },
        '.pattern': {
          backgroundImage:
            'linear-gradient(to right, transparent 49.5%, rgba(251, 232, 67, 0.2) 49.5%, rgba(251, 232, 67, 0.6) 50.5%, transparent 50.5%)',
          backgroundSize: '5% 100%',
          backgroundPosition: 'center',
          backgroundRepeat: 'repeat-x',
        },
      }
      addUtilities(newUtilities)
    }),
  ],
}

export default config
