import React from "react";
import "../styles/components/navbar.css";

function Navbar() {
  return (
    <div className="navbar">
      
      {/* Left */}
      <h2 className="navbar-title">
        🚨 Threat Detection & Incident Response
      </h2>

      {/* Right */}
      <div className="navbar-right">
        <span className="system-status">🟢 System Active</span>
        <span className="user">SOC Analyst</span>
      </div>

    </div>
  );
}

export default Navbar;