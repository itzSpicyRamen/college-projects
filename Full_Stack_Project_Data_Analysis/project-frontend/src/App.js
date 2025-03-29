import React from 'react';
import './App.css';
import Navbar from './components/Navbar';
import { BrowserRouter as Router, Routes, Route} from 'react-router-dom';
import About from './pages/about';
import './App.css';
import MapView from './components/leafletUI/MapView';
import CovidData from './components/CovidComp/coviddata';
import Signin from './pages/signin';

function App() {
  return (

    <Router>
      <Navbar />
      <Routes>
      <Route path="/crimedata" element={<MapView/>} exact />
      <Route path="/coviddata" element={<CovidData/>} exact />
      <Route path="/about" element={<About/>} exact />
      <Route path="/signin" element={<Signin/>} exact />
      </Routes>
    </Router>
  );
}

export default App;