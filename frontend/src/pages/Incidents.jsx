import React from "react";

import IncidentTable from "../components/IncidentTable";

import "../styles/pages/incidents.css";

function Incidents() {

  return (
    <div className="incidents-page">

      {/* Header */}
      <div className="incidents-header">

        <div>
          <h1>Incident Management</h1>
          <p>
            Monitor, investigate, and respond to security incidents
          </p>
        </div>

      </div>

      {/* Summary Cards */}
      <div className="incident-stats">
        {/* render real values form backend  and there is no such functionality available implement it*/}
        <div className="incident-card critical">
          <h3>Critical</h3>
          <h1>12</h1>
          <p>High priority incidents</p>
        </div>

        <div className="incident-card warning">
          <h3>Open</h3>
          <h1>8</h1>
          <p>Require analyst action</p>
        </div>

        <div className="incident-card success">
          <h3>Resolved</h3>
          <h1>24</h1>
          <p>Successfully mitigated</p>
        </div>

        <div className="incident-card primary">
          <h3>Blocked IPs</h3>
          <h1>18</h1>
          <p>Threat sources blocked</p>
        </div>

      </div>

      {/* Filters */}
      <div className="incident-toolbar">

        <input
          type="text"
          placeholder="Search incidents..."
          className="search-input"
        />

        <select className="filter-select">
          <option>All Severity</option>
          <option>Critical</option>
          <option>High</option>
          <option>Medium</option>
          <option>Low</option>
        </select>

        <select className="filter-select">
          <option>All Status</option>
          <option>Open</option>
          <option>Closed</option>
        </select>

      </div>

      {/* Table */}
      <div className="incident-table-section">

        <div className="section-header">
          <h2>Active Incidents</h2>
        </div>

        <IncidentTable />

      </div>

    </div>
  );
}

export default Incidents;