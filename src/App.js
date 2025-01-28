import React from "react";
import { Route, Routes } from "react-router-dom";
import Header from "./components/Header";
import Footer from "./components/Footer";

import Home from "./pages/Home";
import Institutions from "./pages/Institutions";
import DataProcessing from "./pages/DataProcessing";
import CodeGuide from "./pages/CodeGuide";
import Analysis from "./pages/Analysis";

import "./App.css";

function App() {
  return (
    <div className="app-container">
      <Header />
      <div className="main-content container mt-5">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/institutions" element={<Institutions />} />
          <Route path="/dataprocessing" element={<DataProcessing />} />
          <Route path="/codeguide" element={<CodeGuide />} />
          <Route path="/analysis" element={<Analysis />} />
        </Routes>
      </div>
      <Footer />
    </div>
  );
}

export default App;
