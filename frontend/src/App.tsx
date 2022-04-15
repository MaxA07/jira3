import React from 'react';
import logo from './logo.svg';
import './App.css';
import { Block } from './Block';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <Block value={123}/>
      </header>
    </div>
  );
}

export default App;
