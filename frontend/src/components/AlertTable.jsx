
import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import "../styles/components/table.css";

const AlertTable = () => {
  const [alerts, setAlerts] = useState([]);
  const [searchIP, setSearchIP] = useState("");
  const navigate = useNavigate();

  const fetchAlerts = async () => {
    try {
      let url = "http://127.0.0.1:8000/alerts";

      if (searchIP) {
        url = `http://127.0.0.1:8000/alerts/filter?ip=${searchIP}`;
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
    if (count > 10) return "HIGH";
    if (count > 5) return "MEDIUM";
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
            alerts.map((alert, index) => (
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


// import React, { useEffect, useState } from "react";
// import { useNavigate } from "react-router-dom";
// const AlertTable = () => {
//   const [alerts, setAlerts] = useState([]);
//   const [searchIP, setSearchIP] = useState("");
//   const navigate = useNavigate();

//   const fetchAlerts = async () => {
//     try {
//       let url = "http://127.0.0.1:8000/alerts";

//       if (searchIP) {
//         url = `http://127.0.0.1:8000/alerts/filter?ip=${searchIP}`;
//       }

//       const res = await fetch(url);
//       const data = await res.json();
//       setAlerts(data);
//     } catch (err) {
//       console.error("Error fetching alerts:", err);
//     }
//   };

//   useEffect(() => {
//     fetchAlerts();
//     const interval = setInterval(fetchAlerts, 3000);
//     return () => clearInterval(interval);
//   }, [searchIP]);

//   const getSeverityStyle = (severity) => {
//     switch (severity) {
//       case "HIGH":
//         return { color: "red", fontWeight: "bold" };
//       case "WARNING":
//         return { color: "orange", fontWeight: "bold" };
//       default:
//         return { color: "green" };
//     }
//   };

//   const getRiskLevel = (count) => {
//     if (count > 10) return "HIGH";
//     if (count > 5) return "MEDIUM";
//     return "LOW";
//   };

//   return (
//     <div>
//       <input
//         type="text"
//         placeholder="Search by IP..."
//         value={searchIP}
//         onChange={(e) => setSearchIP(e.target.value)}
//         style={{ marginBottom: "15px", padding: "5px" }}
//       />

//       <table border="1" cellPadding="10" style={{ width: "100%", textAlign: "center" }}>
//         <thead>
//           <tr>
//             <th>Timestamp</th>
//             <th>IP</th>
//             <th>IP Type</th>
//             <th>Attack Type</th>
//             <th>Severity</th>
//             <th>Attack Count</th>
//             <th>Risk</th>
//           </tr>
//         </thead>

//         <tbody>
//           {alerts.map((alert, index) => (
//             <tr key={index}>
//               <td>{alert.timestamp}</td>
//               <td
//                 style={{ cursor: "pointer", color: "blue" }}
//                 onClick={() => navigate(`/investigation/${alert.ip}`)}
//               >
//                 {alert.ip}
//               </td>

//               <td>
//                 {alert.ip_type === "PUBLIC" ? "🌍 Public" : "🏠 Private"}
//               </td>

//               <td>{alert.attack_type}</td>

//               <td style={getSeverityStyle(alert.severity)}>
//                 {alert.severity}
//               </td>

//               <td>{alert.attack_count}</td>

//               <td>{getRiskLevel(alert.attack_count)}</td>
//             </tr>
//           ))}
//         </tbody>
//       </table>
//     </div>
//   );
// };

// export default AlertTable;