import React from "react";
import "../styles/pages/dashboard.css";

import StatsCards from "../components/StatsCards";
import AttackChart from "../components/AttackChart";
import TopIPsChart from "../components/TopIPsChart";
import AlertTable from "../components/AlertTable";
import IncidentTable from "../components/IncidentTable";

const Dashboard = () => {
  return (
    <div className="dashboard">

      {/* Header */}
      <div className="dashboard-header">
        <div>
          <h1>SOC Overview</h1>
          <p>Real-time security monitoring and threat detection</p>
        </div>
      </div>

      {/* Stats Cards */}
      <StatsCards />

      {/* Charts */}
      <div className="charts-grid">
        <div className="chart-card large-chart">
          <h3>Alerts Over Time</h3>
          <AttackChart />
        </div>

        <div className="chart-card">
          <h3>Alerts by Severity</h3>
          <TopIPsChart />
        </div>
      </div>

      {/* Tables */}
      {/* <div className="tables-grid"> */}

        <div className="table-card">
          <div className="card-header">
            <h3>Recent Alerts</h3>
          </div>
          <AlertTable />
        </div>

        <div className="table-card">
          <div className="card-header">
            <h3>Active Incidents</h3>
          </div>
          <IncidentTable />
        </div>

      </div>

    // </div>
  );
};

export default Dashboard;