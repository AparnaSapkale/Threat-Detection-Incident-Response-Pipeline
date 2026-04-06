import React from "react";
import './index.css';

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
      <Navbar />

      <div style={{ display: "flex" }}>
        <Sidebar />

        <div style={{ padding: "20px", width: "100%" }}>
          <Routes>
            <Route path="/" element={<Dashboard />} />
            <Route path="/incidents" element={<Incidents />} />
            <Route path="/investigation" element={<Investigation />} />
            <Route path="/investigation/:ip" element={<Investigation />} />
            <Route path="/reports" element={<Reports />} />
          </Routes>
        </div>
      </div>
    </Router>
  );
}

export default App;

