import React, { useState } from 'react';

import { Container } from 'react-bootstrap';

import logo from './logo.svg';
import './App.css';

import MainContent from './components/MainContent'
import Header from './components/Header'

function App() {

  return (
    <div className="App">
      <Header />

      <Container className="mt-4">
        <MainContent />
      </Container>
    </div>
  );
}

export default App;
