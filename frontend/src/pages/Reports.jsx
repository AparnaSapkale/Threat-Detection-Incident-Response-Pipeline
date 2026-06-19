import React, { useEffect, useState } from "react";

import "../styles/pages/reports.css";

const Reports = () => {

  const [summary, setSummary] = useState({});
  const [top, setTop] = useState({});

  useEffect(() => {

    fetch("http://127.0.0.1:8001/report/summary")
      .then((res) => res.json())
      .then((data) => setSummary(data));

    fetch("http://127.0.0.1:8001/report/top-attacker")
      .then((res) => res.json())
      .then((data) => setTop(data));

  }, []);

  return (
    <div className="reports-page">

      {/* Header */}
      <div className="reports-header">

        <div>
          <h1>Security Reports & Analytics</h1>

          <p>
            SOC reporting, attack analytics, and threat intelligence overview
          </p>
        </div>

      </div>

      {/* Summary Cards */}
      <div className="report-stats">

        <div className="report-stat-card">
          <h3>Total Alerts</h3>
          <h1>{summary.total_alerts || 0}</h1>
          <p>Detected security events</p>
        </div>

        <div className="report-stat-card danger">
          <h3>Top Attacker</h3>
          <h2>{top.ip || "N/A"}</h2>
          <p>{top.count || 0} detected attacks</p>
        </div>

        <div className="report-stat-card warning">
          <h3>Threat Level</h3>
          <h1>HIGH</h1>
          <p>Active threat activity detected</p>
        </div>

        <div className="report-stat-card success">
          <h3>System Status</h3>
          <h1>99.9%</h1>
          <p>Monitoring uptime</p>
        </div>

      </div>

      {/* Main Analytics */}
      <div className="reports-grid">

        {/* Attack Breakdown */}
        <div className="report-card">

          <div className="card-header">
            <h2>Attack Breakdown</h2>
          </div>

          <div className="attack-breakdown">

            {summary.attack_breakdown?.length > 0 ? (

              summary.attack_breakdown.map((attack, index) => (

                <div
                  className="attack-item"
                  key={index}
                >

                  <div className="attack-info">

                    <span className="attack-name">
                      {attack._id}
                    </span>

                    <span className="attack-count">
                      {attack.count}
                    </span>

                  </div>

                  <div className="attack-bar-bg">

                    <div
                      className="attack-bar-fill"
                      style={{
                        width: `${attack.count * 10}%`
                      }}
                    ></div>

                  </div>

                </div>
              ))

            ) : (

              <p>No attack data available</p>

            )}

          </div>

        </div>

        {/* Analyst Summary */}
        <div className="report-card">

          <div className="card-header">
            <h2>Analyst Summary</h2>
          </div>

          <div className="analyst-summary">

            <div className="summary-item">
              <span className="summary-label">
                Top Threat Source
              </span>

              <p>{top.ip || "N/A"}</p>
            </div>

            <div className="summary-item">
              <span className="summary-label">
                Most Frequent Activity
              </span>

              <p>
                {summary.attack_breakdown?.[0]?._id || "N/A"}
              </p>
            </div>

            <div className="summary-item">
              <span className="summary-label">
                Risk Assessment
              </span>

              <p className="risk-high">
                Elevated Threat Activity
              </p>
            </div>

            <div className="summary-item">
              <span className="summary-label">
                Recommended Action
              </span>

              <p>
                Continue active monitoring and block suspicious IPs
              </p>
            </div>

          </div>

        </div>

      </div>

      {/* Download Section */}
      <div className="download-section">

        <div className="download-card">

          <div>

            <h2>Export Security Report</h2>

            <p>
              Download complete incident and alert data
            </p>

          </div>

          <a
            href="http://127.0.0.1:8001/report/full"
            target="_blank"
            rel="noopener noreferrer"
            className="download-btn"
          >
            Download JSON Report
          </a>

        </div>

      </div>

    </div>
  );
};

export default Reports;