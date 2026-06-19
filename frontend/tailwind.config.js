/** @type {import('tailwindcss').Config} */
export default {
  darkMode: 'class', // Enable dark mode toggling via a CSS class on HTML tag
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      fontFamily: {
        sans: ['Inter', 'system-ui', 'sans-serif'],
      },
      colors: {
        brand: {
          accent: '#1E3A5F', // Muted navy for primary actions
          accentHover: '#162C4A', // Darker navy for hover states
        },
        surface: {
          light: '#FFFFFF',
          offwhite: '#F9F9F9',
          dark: '#1E293B',
          bgDark: '#0F172A',
        },
        ink: {
          lightest: '#F0F0F0',
          light: '#9CA3AF',
          mid: '#374151',
          dark: '#111827',
          mutedDark: '#94A3B8', // For secondary text in dark mode
        },
        alert: {
          error: '#DC2626',
          success: '#16A34A',
          info: '#2563EB',
        }
      },
      boxShadow: {
        'solid': '0 1px 2px rgba(0,0,0,0.08)',
      }
    },
  },
  plugins: [],
}
