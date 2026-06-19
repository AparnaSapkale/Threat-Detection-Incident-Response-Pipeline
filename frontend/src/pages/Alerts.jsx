// Given bellow is the code for Alerts.jsx which is currently commented out as we have moved the AlertTable component to components folder for better reusability and separation of concerns. You can refer to the AlertTable.jsx file in components folder for the actual implementation of the alert table which is being used in the Alerts page.

// alerts page functions 
// 1. which shows all the alerts in a table format with search functionality and auto refresh every 3 seconds
// 2. clicking on the IP in the alert table will navigate to the investigation page for that IP
// 3. the alert table will show timestamp, src_IP, Dest_IP, attck type, severity, attack count and risk level for each alert, view (raw logs) button will be added in the actions column in future for each alert which will show the raw logs for that alert in a modal view
// 4. shows which alerts are new , investigating , open and closed based on the status of the alert in the backend which will be implemented in future
// 5. also there should be search fuctionality to search for specific IPs , attck types 
//  take the help of AlertTable component for the implementation of the alert table in the Alerts page , make sure to implement the search functionality and auto refresh functionality in the AlertTable component as well as the navigation to the investigation page on clicking the IP in the alert table and make sure all fuctions as mansion must be implemented in the AlertTable component for better reusability and separation of concerns

/*

import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import "../styles/components/table.css";

const AlertTable = () => {
  const [alerts, setAlerts] = useState([]);
  const [searchIP, setSearchIP] = useState("");
  const navigate = useNavigate();

  const fetchAlerts = async () => {
    try {
      let url = "http://127.0.0.1:8001/alerts";

      if (searchIP) {
        url = `http://127.0.0.1:8001/alerts/filter?ip=${searchIP}`;
      }

      const res = await fetch(url);
      const data = await res.json();
      setAlerts(Array.isArray(data) ? data : []);
    } catch (err) {
      console.error("Error fetching alerts:", err);
      setAlerts([]);
    }
  };

  useEffect(() => {
    fetchAlerts();
    const interval = setInterval(fetchAlerts, 3000);
    return () => clearInterval(interval);
  }, [searchIP]);

  const getSeverityClass = (severity) => {
    switch (severity) {
      case "HIGH":
        return "severity-high";
      case "WARNING":
        return "severity-warning";
      default:
        return "severity-low";
    }
  };

  const getRiskLevel = (count) => {
    if (count > 30) return "HIGH";
    if (count > 10) return "MEDIUM";
    return "LOW";
  };

  const getRiskClass = (count) => {
    const risk = getRiskLevel(count);
    if (risk === "HIGH") return "risk-high";
    if (risk === "MEDIUM") return "risk-medium";
    return "risk-low";
  };

  return (
    <div className="table-container">
      {/* Search Input * /}
      <input
        type="text"
        placeholder="Search by IP..."
        value={searchIP}
        onChange={(e) => setSearchIP(e.target.value)}
        className="table-search"
      />

      <table className="custom-table">
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
          {alerts.length > 0 ? (
            // only show top 10 alerts for performance other can be accessed via investigation page
            alerts.slice(0, 10).map((alert, index) => (
              <tr key={index}>
                <td>{alert.timestamp}</td>

                <td
                  className="ip-link"
                  onClick={() => navigate(`/investigation/${alert.ip}`)}
                >
                  {alert.ip}
                </td>

                <td>
                  {alert.ip_type === "PUBLIC" ? " Public" : " Private"}
                </td>

                <td>{alert.attack_type}</td>

                <td className={getSeverityClass(alert.severity)}>
                  {alert.severity}
                </td>

                <td>{alert.attack_count}</td>

                <td className={getRiskClass(alert.attack_count)}>
                  {getRiskLevel(alert.attack_count)}
                </td>
              </tr>
            ))
          ) : (
            <tr>
              
              <td colSpan="7">No alerts found</td>
            </tr>
          )}
        </tbody>
      </table>
    </div>
  );
};

export default AlertTable;
 */