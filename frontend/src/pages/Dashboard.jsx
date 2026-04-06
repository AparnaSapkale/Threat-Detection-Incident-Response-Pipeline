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
      
      {/* Title */}
      <h1 className="dashboard-title">🚨 SOC Dashboard</h1>

      {/* Stats */}
      <StatsCards />

      {/* Charts */}
      <div className="dashboard-charts">
        <AttackChart />
        <TopIPsChart />
      </div>

      {/* Alerts */}
      <div className="dashboard-section">
        <h2 className="section-title">Alerts</h2>
        <AlertTable />
      </div>

      {/* Incidents */}
      <div className="dashboard-section">
        <h2 className="section-title">Incidents</h2>
        <IncidentTable />
      </div>

    </div>
  );
};

export default Dashboard;