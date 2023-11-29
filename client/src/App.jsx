import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import GorillaSelection from './components/GorillaSelection'; // Updated import
import GorillaProfile from './components/GorillaProfile'; // Updated impor
import LandingPage from './components/LandingPage';
import './index.css'; // Import global CSS


function App() {
  return (
    <Router>
      <Routes>
        <Route path= "/" element={<LandingPage/>} />
        <Route path="/selection" element={<GorillaSelection />} />
        <Route path="/gorilla/:id" element={<GorillaProfile />} />
      </Routes>
    </Router>
  );
}

export default App;
