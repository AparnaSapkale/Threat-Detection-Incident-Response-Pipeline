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
        `http://127.0.0.1:8000/alerts/filter?ip=${ip}`
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

  const uniqueAttackTypes = [...new Set(alerts.map(a => a.attack_type))];
  const totalAlerts = alerts.length;

  const getSeverityClass = (severity) => {
    if (severity === "HIGH") return "inv-high";
    if (severity === "MEDIUM") return "inv-medium";
    return "inv-low";
  };

  return (
    <div className="investigation">
      
      {/* Title */}
      <h2 className="investigation-title">🔍 Investigation: {ip}</h2>

      {loading ? (
        <p className="loading">Loading...</p>
      ) : (
        <>
          {/* Summary */}
          <div className="investigation-summary">
            <p className="summary-item">
              <strong>Total Alerts:</strong> {totalAlerts}
            </p>
            <p className="summary-item">
              <strong>Attack Types:</strong> {uniqueAttackTypes.join(", ")}
            </p>
          </div>

          {/* Table */}
          <div className="investigation-table">
            <table>
              <thead>
                <tr>
                  <th>Timestamp</th>
                  <th>Attack Type</th>
                  <th>Severity</th>
                </tr>
              </thead>

              <tbody>
                {alerts.length > 0 ? (
                  alerts.map((alert, index) => (
                    <tr key={index}>
                      <td>{alert.timestamp}</td>
                      <td>{alert.attack_type}</td>
                      <td className={getSeverityClass(alert.severity)}>
                        {alert.severity}
                      </td>
                    </tr>
                  ))
                ) : (
                  <tr>
                    <td colSpan="3">No data found</td>
                  </tr>
                )}
              </tbody>
            </table>
          </div>
        </>
      )}
    </div>
  );
}

export default Investigation;

// import React, { useEffect, useState } from "react";
// import { useParams } from "react-router-dom";

// function Investigation() {
//   const { ip } = useParams();
//   const [alerts, setAlerts] = useState([]);
//   const [loading, setLoading] = useState(true);

//   const fetchAlerts = async () => {
//     try {
//       const res = await fetch(
//         `http://127.0.0.1:8000/alerts/filter?ip=${ip}`
//       );
//       const data = await res.json();

//       // ✅ Ensure it's always an array
//       setAlerts(Array.isArray(data) ? data : []);
//     } catch (err) {
//       console.error("Error fetching investigation data:", err);
//       setAlerts([]); // fallback
//     } finally {
//       setLoading(false);
//     }
//   };

//   useEffect(() => {
//     fetchAlerts();
//   }, [ip]);

//   // ✅ Safe calculations
//   const uniqueAttackTypes = [...new Set(alerts.map(a => a.attack_type))];
//   const totalAlerts = alerts.length;

//   return (
//     <div>
//       <h2>🔍 Investigation: {ip}</h2>

//       {/* LOADING */}
//       {loading ? (
//         <p>Loading...</p>
//       ) : (
//         <>
//           {/* SUMMARY */}
//           <div style={{ marginBottom: "20px" }}>
//             <p><strong>Total Alerts:</strong> {totalAlerts}</p>
//             <p><strong>Attack Types:</strong> {uniqueAttackTypes.join(", ")}</p>
//           </div>

//           {/* TABLE */}
//           <table
//             border="1"
//             cellPadding="10"
//             style={{ width: "100%", textAlign: "center" }}
//           >
//             <thead>
//               <tr>
//                 <th>Timestamp</th>
//                 <th>Attack Type</th>
//                 <th>Severity</th>
//               </tr>
//             </thead>
//             <tbody>
//               {alerts.length > 0 ? (
//                 alerts.map((alert, index) => (
//                   <tr key={index}>
//                     <td>{alert.timestamp}</td>
//                     <td>{alert.attack_type}</td>
//                     <td>{alert.severity}</td>
//                   </tr>
//                 ))
//               ) : (
//                 <tr>
//                   <td colSpan="3">No data found</td>
//                 </tr>
//               )}
//             </tbody>
//           </table>
//         </>
//       )}
//     </div>
//   );
// }

// export default Investigation;