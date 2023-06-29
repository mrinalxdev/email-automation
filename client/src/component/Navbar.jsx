import React, { useState } from 'react'
import { Link , useNavigate } from 'react-router-dom'


import { CustomButton } from './'
import { logo, menu, serach, thirdweb } from '../assets'
import { navlinks } from '../constants'

const Navbar = () => {
  const navigate = useNavigate()
  const [isActive, setIsActive] = useState('dashboard')
  const [toggleDrawer, setToggleDrawer] = useState(false)
  return (
    <div>
      This is Navbar
    </div>
  )
}

export default Navbar
