import React from "react";
import "../styles/components/navbar.css";

function Navbar() {
  return (
    <header className="navbar">

      {/* Left Section */}
      <div className="navbar-left">
        <h2>Threat Detection & Incident Response</h2>
        <p>SOC Monitoring Console</p>
      </div>

      {/* Right Section */}
      <div className="navbar-right">

        {/* System Status */}
        <div className="status-card">
          <span className="status-dot"></span>
          <span>System Active</span>
        </div>

        {/* Time Filter */}
        <div className="time-filter">
          <span>Last 24 Hours</span>
        </div>

        {/* User Profile */}
        <div className="user-profile">
          <div className="avatar">S</div>

          <div className="user-info">
            <span className="role">SOC Analyst</span>
            <span className="level">Level 1 Monitoring</span>
          </div>
        </div>

      </div>

    </header>
  );
}

export default Navbar;
// import React from "react";
// import "../styles/components/navbar.css";

// function Navbar() {
//   return (
//     <div className="navbar">

//       <div className="navbar-left">
//         <h2>Threat Detection & Incident Response</h2>
//       </div>

//       <div className="navbar-right">

//         <div className="status">
//           <span className="status-dot"></span>
//           <span>System Active</span>
//         </div>

//         <div className="time-filter">
//           Last 24 Hours
//         </div>

//         <div className="user-profile">
//           <div className="avatar">S</div>
//           <span>SOC Analyst</span>
//         </div>

//       </div>

//     </div>
//   );
// }

// export default Navbar;