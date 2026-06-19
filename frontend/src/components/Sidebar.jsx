import React from "react";
import { Link, useLocation } from "react-router-dom";
import "../styles/components/sidebar.css";

function Sidebar() {

  const location = useLocation();

  const getLinkClass = (path) => {
    return location.pathname === path
      ? "sidebar-link active"
      : "sidebar-link";
  };

  return (
    <div className="sidebar">

      <div className="sidebar-logo">
        <h2>SIEM</h2>
      </div>

      <div className="sidebar-section">
        <p className="section-label">Monitoring</p>

        <Link to="/" className={getLinkClass("/")}>
          📊 Dashboard
        </Link>

        <Link to="/alerts" className={getLinkClass("/alerts")}>
          🚨 Alerts
        </Link>

        <Link to="/incidents" className={getLinkClass("/incidents")}>
          🔥 Incidents
        </Link>

        <Link to="/investigation" className={getLinkClass("/investigation")}>
          🔍 Investigation
        </Link>

        <Link to="/reports" className={getLinkClass("/reports")}>
          📄 Reports
        </Link>
      </div>

      <div className="sidebar-section">
        <p className="section-label">Configuration</p>

        <Link to="/rules" className={getLinkClass("/rules")}>
          ⚙️ Detection Rules
        </Link>
      </div>

    </div>
  );
}

export default Sidebar;