/** @type {import('tailwindcss').Config} */
export default {
  darkMode: 'class',
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        "text-primary": "#0F0E1A",
        "border-soft": "#E8E7F5",
        "surface-tint": "#5b598c",
        "surface-dim": "#d3daea",
        "secondary": "#855300",
        "inverse-primary": "#c4c1fb",
        "outline": "#787680",
        "on-surface-variant": "#47464f",
        "primary-container": "#1e1b4b",
        "tertiary-container": "#002819",
        "surface-muted": "#F8F7FF",
        "on-primary-fixed": "#181445",
        "primary-fixed": "#e3dfff",
        "surface-bright": "#f9f9ff",
        "on-background": "#151c27",
        "on-tertiary": "#ffffff",
        "accent-hover": "#D97706",
        "surface-container-low": "#f0f3ff",
        "surface-container-high": "#e2e8f8",
        "on-surface": "#151c27",
        "surface-container": "#e7eefe",
        "background": "#f9f9ff",
        "error": "#ba1a1a",
        "surface-container-lowest": "#ffffff",
        "on-secondary": "#ffffff",
        "surface": "#f9f9ff",
        "danger": "#DC2626",
        "on-primary": "#ffffff",
        "on-primary-container": "#8683ba",
        "secondary-container": "#fea619",
        "primary": "#070235",
        "saffron": "#F59E0B"
      },
      borderRadius: {
        "DEFAULT": "0.25rem",
        "lg": "12px",
        "xl": "0.75rem",
        "full": "50px"
      },
      spacing: {
        "lg": "24px",
        "max-content-width": "1200px",
        "base": "4px",
        "sidebar-width": "280px",
        "md": "16px",
        "xs": "8px",
        "3xl": "64px",
        "2xl": "48px",
        "sm": "12px",
        "xl": "32px"
      },
      fontFamily: {
        "headline-lg": ["Inter", "sans-serif"],
        "display-hero": ["Playfair Display", "serif"],
        "title-card": ["Inter", "sans-serif"],
        "headline-md": ["Inter", "sans-serif"],
        "nav-link": ["Inter", "sans-serif"],
        "label-caps": ["Inter", "sans-serif"],
        "body-sm": ["Inter", "sans-serif"],
        "body-main": ["Inter", "sans-serif"],
        "button-text": ["Inter", "sans-serif"]
      },
      fontSize: {
        "headline-lg": ["36px", {"lineHeight": "44px", "fontWeight": "600"}],
        "display-hero": ["60px", {"lineHeight": "1.1", "letterSpacing": "-0.02em", "fontWeight": "700"}],
        "title-card": ["18px", {"lineHeight": "24px", "fontWeight": "500"}],
        "headline-md": ["28px", {"lineHeight": "36px", "fontWeight": "600"}],
        "nav-link": ["14px", {"lineHeight": "20px", "fontWeight": "500"}],
        "label-caps": ["12px", {"lineHeight": "16px", "letterSpacing": "0.05em", "fontWeight": "600"}],
        "body-sm": ["15px", {"lineHeight": "22px", "fontWeight": "400"}],
        "body-main": ["16px", {"lineHeight": "24px", "fontWeight": "400"}],
        "button-text": ["14px", {"lineHeight": "20px", "fontWeight": "600"}]
      }
    },
  },
  plugins: [],
}
