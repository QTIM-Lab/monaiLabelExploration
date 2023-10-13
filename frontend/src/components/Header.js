import React, { useState } from 'react';

import { Navbar, Nav } from 'react-bootstrap';

import 'bootstrap/dist/css/bootstrap.min.css';

const Header = () => {

  return (
      <Navbar bg="dark" variant="dark">
        <Navbar.Brand href="#home">My App</Navbar.Brand>
        <Nav className="ml-auto">
          <Nav.Link href="#home">Home</Nav.Link>
          <Nav.Link href="#about">About</Nav.Link>
          <Nav.Link href="#contact">Contact</Nav.Link>
        </Nav>
      </Navbar>
  );
}

export default Header;
