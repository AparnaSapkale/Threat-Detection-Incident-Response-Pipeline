import React, { useEffect, useState } from "react";

function App() {
  const [alerts, setAlerts] = useState([]);
  const [incidents, setIncidents] = useState([]);
  const [searchIP, setSearchIP] = useState("");

  // RISK SCORING HELPER 
  const getRiskLevel = (count) => {
  if (count > 10) return "HIGH";
  if (count > 5) return "MEDIUM";
  return "LOW";
};

  const fetchAlerts = async () => {
  try {
    let url = "http://127.0.0.1:8000/alerts";

    if (searchIP) {
      url = `http://127.0.0.1:8000/alerts/filter?ip=${searchIP}`;
    }

    const res = await fetch(url);
    const data = await res.json();
    setAlerts(data);
  } catch (err) {
    console.error("Error fetching alerts:", err);
  }
};

  const fetchIncidents = async () => {
  try {
    const res = await fetch("http://127.0.0.1:8000/incidents");
    const data = await res.json();
    setIncidents(data);
  } catch (err) {
    console.error("Error fetching incidents:", err);
  }
};

  useEffect(() => {
  fetchAlerts();
  fetchIncidents();

  const interval = setInterval(() => {
    fetchAlerts();
    fetchIncidents();
  }, 3000);

  return () => clearInterval(interval);
}, []);

  const getSeverityStyle = (severity) => {
    switch (severity) {
      case "HIGH":
        return { color: "red", fontWeight: "bold" };
      case "WARNING":
        return { color: "orange", fontWeight: "bold" };
      default:
        return { color: "green" };
    }
  };

  const closeIncident = async (id) => {
  try {
    await fetch(`http://127.0.0.1:8000/incident/${id}/close`, {
      method: "PUT",
    });
    fetchIncidents(); // refresh
  } catch (err) {
    console.error("Error closing incident:", err);
  }
};

  return (
    <div style={{ padding: "20px" }}>
      <h1>🚨 Mini SIEM Dashboard</h1>

      <input
        type="text"
        placeholder="Search by IP..."
        value={searchIP}
        onChange={(e) => setSearchIP(e.target.value)}
        style={{ marginBottom: "20px", padding: "5px" }}
      />

      <table border="1" cellPadding="10" style={{ width: "100%", textAlign: "center" }}>
        <thead>
          <tr>
            <th>Timestamp</th>
            <th>IP</th>
            <th>IP Type</th>
            <th>Attack Type</th>
            <th>Severity</th>
            <th>Attack Count</th>
            <th>Risk</th>
          </tr>
        </thead>

        <tbody>
          {alerts.map((alert, index) => (
            <tr key={index}>
              <td>{alert.timestamp}</td>
              <td>{alert.ip}</td>

              <td>
                {alert.ip_type === "PUBLIC" ? "🌍 Public" : "🏠 Private"}
              </td>

              <td>{alert.attack_type}</td>

              <td style={getSeverityStyle(alert.severity)}>
                {alert.severity}
              </td>

              <td>{alert.attack_count}</td>
              <td>{getRiskLevel(alert.attack_count)}</td>
            </tr>
          ))}
        </tbody>
      </table>
      <h2 style={{ marginTop: "40px" }}>🚨 Incidents</h2>

<table border="1" cellPadding="10" style={{ width: "100%", textAlign: "center" }}>
  <thead>
    <tr>
      <th>ID</th>
      <th>IP</th>
      <th>Attack Types</th>
      <th>Severity</th>
      <th>Status</th>
      <th>Alert Count</th>
      <th>First Seen</th>
      <th>Last Seen</th>
    </tr>
  </thead>

  <tbody>
  {incidents.map((inc, index) => (
    <tr key={index}>
      <td>{inc.id}</td>
      <td>{inc.ip}</td>
      <td>{inc.attack_types.join(", ")}</td>

      {/* Severity */}
      <td
        style={{
          color: inc.severity === "HIGH" ? "red" : "orange",
          fontWeight: "bold",
        }}
      >
        {inc.severity}
      </td>

      {/* Status */}
      <td
        style={{
          color: inc.status === "OPEN" ? "red" : "green",
          fontWeight: "bold",
        }}
      >
        {inc.status === "OPEN" ? "🔴 OPEN" : "🟢 CLOSED"}
      </td>

      <td>{inc.alert_count}</td>
      <td>{inc.first_seen}</td>
      <td>{inc.last_seen}</td>

      {/* Action Button */}
      <td>
        {inc.status === "OPEN" && (
          <button
            onClick={() => closeIncident(inc.id)}
            style={{
              padding: "5px 10px",
              cursor: "pointer",
              backgroundColor: "#ff4d4d",
              color: "white",
              border: "none",
              borderRadius: "5px",
            }}
          >
            Close
          </button>
        )}
      </td>
    </tr>
  ))}
</tbody>
</table>
    </div>
  );
}

export default App;