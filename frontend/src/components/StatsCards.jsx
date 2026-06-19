import React, { useEffect, useState } from "react";
import "../styles/components/statscards.css";

const StatsCards = () => {

  const [stats, setStats] = useState({});

  useEffect(() => {
    fetch("http://127.0.0.1:8001/stats")
      .then((res) => res.json())
      .then((data) => setStats(data));
  }, []);

  const cards = [
  {
    title: "Total Alerts",
    value: stats.total_alerts || 0,
    icon: "🚨",
    className: "danger"
  },

  {
    title: "Active Incidents",
    value: stats.active_incidents || 0,
    icon: "🔥",
    className: "warning"
  },

  {
    title: "Blocked IPs",
    value: stats.blocked_ips || 0,
    icon: "🛡️",
    className: "success"
  },

  {
    title: "Assets Monitored",
    value: stats.assets_monitored || 0,
    icon: "💻",
    className: "primary"
  }
];

  return (
    <div className="stats-grid">

      {cards.map((card, index) => (
        <div className="stat-card" key={index}>

          <div>
            <p className="card-title">{card.title}</p>
            <h2>{card.value}</h2>
          </div>

          <div className={`card-icon ${card.className}`}>
            {card.icon}
          </div>

        </div>
      ))}

    </div>
  );
};

export default StatsCards;