import ThemeProvider from 'components/providers/theme'
import { UnifrakturMaguntia } from 'next/font/google'

export const unifrakturMaguntia = UnifrakturMaguntia({
  weight: ['400'],
  subsets: ['latin'],
  variable: '--font-unifraktur-maguntia',
})

const RootLayout: React.FC<{ children: JSX.Element }> = ({ children }) => (
  <html lang="en" className={unifrakturMaguntia.variable}>
    <body>
      <ThemeProvider>{children}</ThemeProvider>
    </body>
  </html>
)

export default RootLayout
