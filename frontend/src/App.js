import React from "react";
import "./index.css";
import Footer from "./components/Footer";

import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

import Navbar from "./components/Navbar";
import Sidebar from "./components/Sidebar";

import Dashboard from "./pages/Dashboard";
import Incidents from "./pages/Incidents";
import Investigation from "./pages/Investigation";
import Reports from "./pages/Reports";

function App() {
  return (
    <Router>

      <div className="app-layout">

        {/* Sidebar */}
        <Sidebar />

        {/* Main Content */}
        <div className="main-layout">

          {/* Navbar */}
          <Navbar />

          {/* Page Content */}
          <div className="page-content">

            <Routes>
              <Route path="/" element={<Dashboard />} />
              <Route path="/incidents" element={<Incidents />} />
              <Route path="/investigation" element={<Investigation />} />
              <Route path="/investigation/:ip" element={<Investigation />} />
              <Route path="/reports" element={<Reports />} />
            </Routes>

          </div>
        <Footer/>
        </div>

      </div>
      
    </Router>
    
  );
}

export default App;