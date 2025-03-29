# MyBestOne Frontend

A modern, Pornhub-inspired face swap web application built with Next.js and Tailwind CSS.

## Features

- Drag-and-drop file uploads
- Real-time face swapping
- Progress tracking
- Responsive design
- Modern UI with Pornhub-inspired styling

## Tech Stack

- Next.js 14
- TypeScript
- Tailwind CSS
- React Dropzone
- React Icons

## Getting Started

1. Clone the repository:
```bash
git clone https://github.com/giacomoarcaro/faceswap-adult.git
cd faceswap-adult/frontend
```

2. Install dependencies:
```bash
npm install
```

3. Run the development server:
```bash
npm run dev
```

4. Open [http://localhost:3000](http://localhost:3000) in your browser.

## Development

- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run start` - Start production server
- `npm run lint` - Run ESLint

## Deployment on Vercel

1. Push your code to GitHub
2. Go to [Vercel](https://vercel.com) and sign up/login with your GitHub account
3. Click "New Project"
4. Import your GitHub repository (faceswap-adult)
5. Configure the project:
   - Framework Preset: Next.js
   - Root Directory: frontend
   - Build Command: `next build`
   - Output Directory: `.next`
6. Add Environment Variables:
   - Name: `NEXT_PUBLIC_API_URL`
   - Value: Your backend API URL (e.g., `https://your-backend-url.com`)
7. Click "Deploy"

## Environment Variables

Create a `.env.local` file with the following variables:

```env
NEXT_PUBLIC_API_URL=http://localhost:8000
```

## License

MIT 