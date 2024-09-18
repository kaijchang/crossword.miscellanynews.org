'use client'

import { chakra, Heading } from '@chakra-ui/react'

const Page: React.FC = () => (
  <chakra.div
    display="flex"
    flexDirection="column"
    alignItems="center"
    color="white"
    bg="misc"
    p={4}
  >
    <chakra.img src="/logo.svg" />
    <Heading>Games</Heading>
  </chakra.div>
)

export default Page
