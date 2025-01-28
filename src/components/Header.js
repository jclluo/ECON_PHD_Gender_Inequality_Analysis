import React from "react";
import { Link } from "react-router-dom";

const Header = () => {
  return (
    <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
      <div className="container-fluid">
        <Link to="/" className="navbar-brand">
          Gender Inequality in Econ PhD
        </Link>
        <button
          className="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarNav"
        >
          <span className="navbar-toggler-icon"></span>
        </button>

        <div className="collapse navbar-collapse" id="navbarNav">
          <ul className="navbar-nav ms-auto">
            <li className="nav-item">
              <Link to="/" className="nav-link">
                Project Overview
              </Link>
            </li>
            <li className="nav-item">
              <Link to="/institutions" className="nav-link">
                Targeted Institutions
              </Link>
            </li>
            <li className="nav-item">
              <Link to="/dataprocessing" className="nav-link">
                Data Processing
              </Link>
            </li>
            <li className="nav-item">
              <Link to="/codeguide" className="nav-link">
                Code Guide
              </Link>
            </li>
            <li className="nav-item">
              <Link to="/analysis" className="nav-link">
                Analysis
              </Link>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  );
};

export default Header;
