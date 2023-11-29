import React from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import GorillaSelection from './components/GorillaSelection';
import GorillaProfile from './components/GorillaProfile';
import LandingPage from './components/LandingPage';
import './index.css';


function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<LandingPage />} />
        <Route path="/selection" element={<GorillaSelection />} />
        <Route path="/gorilla/:id" element={<GorillaProfile />} />
      </Routes>
    </Router>
  );
}

export default App;