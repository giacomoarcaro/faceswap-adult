/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './pages/**/*.{js,ts,jsx,tsx,mdx}',
    './components/**/*.{js,ts,jsx,tsx,mdx}',
    './app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {
      colors: {
        'ph-orange': '#f90',
      },
      fontFamily: {
        'condensed': ['Roboto Condensed', 'sans-serif'],
      },
    },
  },
  plugins: [],
} 