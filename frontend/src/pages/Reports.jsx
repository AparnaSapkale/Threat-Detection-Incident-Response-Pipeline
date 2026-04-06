import React, { useEffect, useState } from "react";
import "../styles/pages/reports.css";

const Reports = () => {
  const [summary, setSummary] = useState({});
  const [top, setTop] = useState({});

  useEffect(() => {
    fetch("http://127.0.0.1:8000/report/summary")
      .then((res) => res.json())
      .then((data) => setSummary(data));

    fetch("http://127.0.0.1:8000/report/top-attacker")
      .then((res) => res.json())
      .then((data) => setTop(data));
  }, []);

  return (
    <div className="reports">
      
      {/* Title */}
      <h1 className="reports-title">📊 Security Report</h1>

      {/* Total Alerts */}
      <div className="report-card">
        <p className="report-text">
          Total Alerts: <span className="highlight">{summary.total_alerts || 0}</span>
        </p>
      </div>

      {/* Top Attacker */}
      <div className="report-card">
        <p className="report-text">Top Attacker:</p>
        <p className="highlight">
          {top.ip || "N/A"} ({top.count || 0} attacks)
        </p>
      </div>

      {/* Attack Breakdown */}
      <div className="report-card">
        <p className="report-text">Attack Breakdown:</p>
        <ul className="report-list">
          {summary.attack_breakdown?.map((a, i) => (
            <li key={i}>
              {a._id} → {a.count}
            </li>
          ))}
        </ul>
      </div>

      {/* Download */}
      <a
        href="http://127.0.0.1:8000/report/full"
        target="_blank"
        rel="noopener noreferrer"
        className="download-btn"
      >
        📥 Download JSON Report
      </a>

    </div>
  );
};

export default Reports;
// import React, { useEffect, useState } from "react";

// const Reports = () => {
//     const [summary, setSummary] = useState({});
//     const [top, setTop] = useState({});

//     useEffect(() => {
//         fetch("http://127.0.0.1:8000/report/summary")
//             .then(res => res.json())
//             .then(data => setSummary(data));

//         fetch("http://127.0.0.1:8000/report/top-attacker")
//             .then(res => res.json())
//             .then(data => setTop(data));
//     }, []);

//     return (
//         <div style={{ padding: "20px" }}>
//             <h1>📊 Security Report</h1>

//             <h3>Total Alerts: {summary.total_alerts}</h3>

//             <h3>Top Attacker:</h3>
//             <p>{top.ip} ({top.count} attacks)</p>

//             <h3>Attack Breakdown:</h3>
//             <ul>
//                 {summary.attack_breakdown?.map((a, i) => (
//                     <li key={i}>
//                         {a._id} → {a.count}
//                     </li>

//                 ))}
//             </ul>
//             <a
//                 href="http://127.0.0.1:8000/report/full"
//                 target="_blank"
//                 rel="noopener noreferrer"
//             >
//                 📥 Download JSON Report
//             </a>
//         </div>
//     );
// };

// export default Reports;