import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import "../styles/components/table.css";

const IncidentTable = () => {

  const [incidents, setIncidents] = useState([]);
  const navigate = useNavigate();

  const fetchIncidents = async () => {
    try {
      const res = await fetch("http://127.0.0.1:8000/incidents");
      const data = await res.json();
      setIncidents(data);
    } catch (err) {
      console.error("Error fetching incidents:", err);
    }
  };

  const closeIncident = async (id) => {
    try {
      await fetch(`http://127.0.0.1:8000/incident/${id}/close`, {
        method: "PUT",
      });
      fetchIncidents();
    } catch (err) {
      console.error("Error closing incident:", err);
    }
  };

  useEffect(() => {
    fetchIncidents();
    const interval = setInterval(fetchIncidents, 3000);
    return () => clearInterval(interval);
  }, []);

  const blockIP = async (ip) => {
    try {
      await fetch(`http://127.0.0.1:8000/block_ip?ip=${ip}`, {
        method: "POST",
      });
      alert(`Blocked IP: ${ip}`);
    } catch (err) {
      console.error("Error blocking IP:", err);
    }
  };

  const getSeverityClass = (severity) => {
  return severity === "HIGH" ? "severity-high" : "severity-warning";
};
//   return (
//     <div>
//       <table border="1" cellPadding="10" style={{ width: "100%", textAlign: "center" }}>
//         <thead>
//           <tr>
//             <th>ID</th>
//             <th>IP</th>
//             <th>Attack Types</th>
//             <th>Severity</th>
//             <th>Status</th>
//             <th>Alert Count</th>
//             <th>First Seen</th>
//             <th>Last Seen</th>
//             <th>Action</th>
//           </tr>
//         </thead>

//         <tbody>
//           {incidents.map((inc, index) => (
//             <tr key={index}>
//               <td>{inc._id}</td>
//               <td
//                 style={{ cursor: "pointer", color: "blue" }}
//                 onClick={() => navigate(`/investigation/${inc.ip}`)}
//               >
//                 {inc.ip}
//               </td>
//               <td>{inc.attack_types.join(", ")}</td>

//               <td
//                 style={{
//                   color: inc.severity === "HIGH" ? "red" : "orange",
//                   fontWeight: "bold",
//                 }}
//               >
//                 {inc.severity}
//               </td>

//               <td
//                 style={{
//                   color: inc.status === "OPEN" ? "red" : "green",
//                   fontWeight: "bold",
//                 }}
//               >
//                 {inc.status === "OPEN" ? "🔴 OPEN" : "🟢 CLOSED"}
//               </td>

//               <td>{inc.alert_count}</td>
//               <td>{inc.first_seen}</td>
//               <td>{inc.last_seen}</td>

//               <td>
//                 {inc.status === "OPEN" && (
//                   <>
//                     <button
//                       onClick={() => closeIncident(inc._id)}
//                       style={{
//                         marginRight: "5px",
//                         padding: "5px",
//                         backgroundColor: "#ff4d4d",
//                         color: "white",
//                         border: "none",
//                       }}
//                     >
//                       Close
//                     </button>

//                     <button
//                       onClick={() => blockIP(inc.ip)}
//                       style={{
//                         padding: "5px",
//                         backgroundColor: "#333",
//                         color: "white",
//                         border: "none",
//                       }}
//                     >
//                       Block IP
//                     </button>
//                   </>
//                 )}
//               </td>
//             </tr>
//           ))}
//         </tbody>
//       </table>
//     </div>
//   );
// };

// export default IncidentTable;
 return (
    <div className="table-container">
      <table className="custom-table">
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
            <th>Action</th>
          </tr>
        </thead>

        <tbody>
          {incidents.length > 0 ? (
            incidents.map((inc, index) => (
              <tr key={index}>
                <td>{inc._id}</td>

                <td
                  className="ip-link"
                  onClick={() => navigate(`/investigation/${inc.ip}`)}
                >
                  {inc.ip}
                </td>

                <td>{inc.attack_types.join(", ")}</td>

                <td className={getSeverityClass(inc.severity)}>
                  {inc.severity}
                </td>

                <td
                  className={
                    inc.status === "OPEN" ? "status-open" : "status-closed"
                  }
                >
                  {inc.status === "OPEN" ? "🔴 OPEN" : "🟢 CLOSED"}
                </td>

                <td>{inc.alert_count}</td>
                <td>{inc.first_seen}</td>
                <td>{inc.last_seen}</td>

                <td>
                  {inc.status === "OPEN" && (
                    <>
                      <button
                        className="btn btn-close"
                        onClick={() => closeIncident(inc._id)}
                      >
                        Close
                      </button>

                      <button
                        className="btn btn-block"
                        onClick={() => blockIP(inc.ip)}
                      >
                        Block IP
                      </button>
                    </>
                  )}
                </td>
              </tr>
            ))
          ) : (
            <tr>
              <td colSpan="9">No incidents found</td>
            </tr>
          )}
        </tbody>
      </table>
    </div>
  );
};

export default IncidentTable;