import React, { useEffect, useState } from "react";

const StatsCards = () => {
  const [stats, setStats] = useState({});

  useEffect(() => {
    fetch("http://127.0.0.1:8000/stats")
      .then(res => res.json())
      .then(data => setStats(data));
  }, []);

  return (
    <div style={{ display: "flex", gap: "20px", marginBottom: "20px" }}>
      <div>🚨 Alerts: {stats.total_alerts}</div>
      <div>🔥 Active Incidents: {stats.active_incidents}</div>
      <div>🚫 Blocked IPs: {stats.blocked_ips}</div>
    </div>
  );
};

export default StatsCards;