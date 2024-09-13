'use client'

import { ChakraProvider } from '@chakra-ui/react'

const ThemeProvider: React.FC<{ children: JSX.Element }> = ({ children }) => (
	<ChakraProvider>{children}</ChakraProvider>
)

export default ThemeProvider
