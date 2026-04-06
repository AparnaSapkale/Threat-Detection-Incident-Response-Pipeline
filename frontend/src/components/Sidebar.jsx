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
      
      {/* Title */}
      <h3 className="sidebar-title">🛡️ SIEM</h3>

      {/* Menu */}
      <ul className="sidebar-menu">
        <li>
          <Link to="/" className={getLinkClass("/")}>
            📊 Dashboard
          </Link>
        </li>

        <li>
          <Link to="/incidents" className={getLinkClass("/incidents")}>
            🚨 Incidents
          </Link>
        </li>

        <li>
          <Link to="/investigation" className={getLinkClass("/investigation")}>
            🔍 Investigation
          </Link>
        </li>

        <li>
          <Link to="/reports" className={getLinkClass("/reports")}>
            📄 Reports
          </Link>
        </li>
      </ul>

    </div>
  );
}

export default Sidebar;