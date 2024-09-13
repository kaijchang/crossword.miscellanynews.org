import ThemeProvider from 'components/providers/theme'

const RootLayout: React.FC<{ children: JSX.Element }> = ({ children }) => (
  <html lang="en">
    <body>
      <ThemeProvider>{children}</ThemeProvider>
    </body>
  </html>
)

export default RootLayout
