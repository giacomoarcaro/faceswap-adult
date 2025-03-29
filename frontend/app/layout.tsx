import type { Metadata } from 'next'
import { Roboto_Condensed } from 'next/font/google'
import './globals.css'

const robotoCondensed = Roboto_Condensed({ 
  subsets: ['latin'],
  weight: ['400', '700'],
})

export const metadata: Metadata = {
  title: 'MyBestOne - Face Swap',
  description: 'Professional face swapping for adult content',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body className={`${robotoCondensed.className} bg-black text-white min-h-screen`}>
        {children}
      </body>
    </html>
  )
} 