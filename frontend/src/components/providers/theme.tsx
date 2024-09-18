'use client'

import { ChakraProvider } from '@chakra-ui/react'
import { theme } from 'theme'

const ThemeProvider: React.FC<{ children: JSX.Element }> = ({ children }) => (
  <ChakraProvider theme={theme}>{children}</ChakraProvider>
)

export default ThemeProvider
