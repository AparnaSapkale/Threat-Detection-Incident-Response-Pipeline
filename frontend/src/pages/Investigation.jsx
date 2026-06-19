import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";

import "../styles/pages/investigation.css";

function Investigation() {

  const { ip } = useParams();

  const [alerts, setAlerts] = useState([]);
  const [loading, setLoading] = useState(true);

  const fetchAlerts = async () => {

    try {

      const res = await fetch(
        `http://127.0.0.1:8001/alerts/filter?ip=${ip}`
      );

      const data = await res.json();

      setAlerts(Array.isArray(data) ? data : []);

    } catch (err) {

      console.error("Error fetching investigation data:", err);

      setAlerts([]);

    } finally {

      setLoading(false);

    }
  };

  useEffect(() => {
    fetchAlerts();
  }, [ip]);

  const uniqueAttackTypes = [
    ...new Set(alerts.map((a) => a.attack_type))
  ];

  const totalAlerts = alerts.length;

  const highAlerts = alerts.filter(
    (a) => a.severity === "HIGH"
  ).length;

  const mediumAlerts = alerts.filter(
    (a) => a.severity === "MEDIUM"
  ).length;

  const lowAlerts = alerts.filter(
    (a) => a.severity === "LOW"
  ).length;

  const getSeverityClass = (severity) => {

    if (severity === "HIGH") return "severity-high";

    if (severity === "MEDIUM") return "severity-medium";

    return "severity-low";
  };

  return (
    <div className="investigation-page">

      {/* Header */}
      <div className="investigation-header">

        <div>
          <h1>Threat Investigation</h1>
          <p>
            Analyze suspicious activity and investigate indicators
          </p>
        </div>

        <div className="target-ip">
          {ip}
        </div>

      </div>

      {/* Summary Cards */}
      <div className="investigation-stats">

        <div className="inv-card">
          <h3>Total Alerts</h3>
          <h1>{totalAlerts}</h1>
        </div>

        <div className="inv-card high-card">
          <h3>High Severity</h3>
          <h1>{highAlerts}</h1>
        </div>

        <div className="inv-card medium-card">
          <h3>Medium Severity</h3>
          <h1>{mediumAlerts}</h1>
        </div>

        <div className="inv-card low-card">
          <h3>Low Severity</h3>
          <h1>{lowAlerts}</h1>
        </div>

      </div>

      {/* Threat Summary */}
      <div className="threat-summary">

        <div className="summary-card">

          <h2>Threat Intelligence Summary</h2>

          <div className="summary-grid">

            <div>
              <span className="summary-label">
                Target IP
              </span>

              <p>{ip}</p>
            </div>

            <div>
              <span className="summary-label">
                Attack Types
              </span>

              <p>
                {uniqueAttackTypes.join(", ")}
              </p>
            </div>

            <div>
              <span className="summary-label">
                Threat Score
              </span>

              <p className="threat-score">
                HIGH RISK
              </p>
            </div>

            <div>
              <span className="summary-label">
                Recommendation
              </span>

              <p>
                Block source IP and continue monitoring
              </p>
            </div>

          </div>

        </div>

      </div>

      {/* Investigation Table */}
      <div className="investigation-table-card">

        <div className="table-header">
          <h2>Alert Timeline</h2>
        </div>

        {loading ? (

          <div className="loading">
            Loading investigation data...
          </div>

        ) : (

          <div className="investigation-table">

            <table>

              <thead>
                <tr>
                  <th>Timestamp</th>
                  <th>Attack Type</th>
                  <th>Severity</th>
                  <th>Status</th>
                </tr>
              </thead>

              <tbody>

                {alerts.length > 0 ? (

                  alerts.map((alert, index) => (

                    <tr key={index}>

                      <td>{alert.timestamp}</td>

                      <td>{alert.attack_type}</td>

                      <td>

                        <span
                          className={`severity-badge ${getSeverityClass(alert.severity)}`}
                        >
                          {alert.severity}
                        </span>

                      </td>

                      <td>

                        <span className="status-badge">
                          DETECTED
                        </span>

                      </td>

                    </tr>
                  ))

                ) : (

                  <tr>
                    <td colSpan="4">
                      No investigation data found
                    </td>
                  </tr>

                )}

              </tbody>

            </table>

          </div>

        )}

      </div>

    </div>
  );
}

export default Investigation;