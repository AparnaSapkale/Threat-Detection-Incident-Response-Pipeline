import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

import "../styles/components/table.css";

const IncidentTable = () => {

  const [incidents, setIncidents] = useState([]);

  const navigate = useNavigate();

  /* Fetch Incidents */

  const fetchIncidents = async () => {

    try {

      const res = await fetch(
        "http://127.0.0.1:8001/incidents"
      );

      const data = await res.json();

      setIncidents(Array.isArray(data) ? data : []);

    } catch (err) {

      console.error(
        "Error fetching incidents:",
        err
      );
    }
  };

  /* Close Incident */

  const closeIncident = async (id) => {

    try {

      await fetch(
        `http://127.0.0.1:8001/incident/${id}/close`,
        {
          method: "PUT",
        }
      );

      fetchIncidents();

    } catch (err) {

      console.error(
        "Error closing incident:",
        err
      );
    }
  };

  /* Block IP */

  const blockIP = async (ip) => {

    try {

      await fetch(
        `http://127.0.0.1:8001/block_ip?ip=${ip}`,
        {
          method: "POST",
        }
      );

      alert(`Blocked IP: ${ip}`);

    } catch (err) {

      console.error(
        "Error blocking IP:",
        err
      );
    }
  };

  /* Auto Refresh */

  useEffect(() => {

    fetchIncidents();

    const interval = setInterval(
      fetchIncidents,
      3000
    );

    return () => clearInterval(interval);

  }, []);

  /* Severity */

  const getSeverityClass = (severity) => {

    if (severity === "HIGH")
      return "severity-high";

    if (severity === "MEDIUM")
      return "severity-medium";

    return "severity-low";
  };

  return (
    <div className="table-container">

      <table className="custom-table">

        <thead>

          <tr>
            <th>Incident</th>
            <th>Source IP</th>
            <th>Attack Type</th>
            <th>Severity</th>
            <th>Status</th>
            <th>Alerts</th>
            <th>Timeline</th>
            <th>Actions</th>
            
          </tr>

        </thead>

        <tbody>

          {incidents.length > 0 ? (

            incidents.map((inc, index) => (

              <tr key={index}>

                {/* Incident ID */}

                <td>
                  <div className="incident-id">
                    #{inc._id}
                  </div>
                </td>

                {/* IP */}

                <td>

                  <span
                    className="ip-link"
                    onClick={() =>
                      navigate(
                        `/investigation/${inc.ip}`
                      )
                    }
                  >
                    {inc.ip}
                  </span>

                </td>

                {/* Attack Types */}

                <td>

                  <div className="attack-tags">

                    {inc.attack_types.map(
                      (type, idx) => (

                        <span
                          key={idx}
                          className="attack-tag"
                        >
                          {type}
                        </span>
                      )
                    )}

                  </div>

                </td>

                {/* Severity */}

                <td>

                  <span
                    className={`severity-badge ${getSeverityClass(
                      inc.severity
                    )}`}
                  >
                    {inc.severity}
                  </span>

                </td>

                {/* Status */}

                <td>

                  <span
                    className={
                      inc.status === "OPEN"
                        ? "status-badge status-open"
                        : "status-badge status-closed"
                    }
                  >
                    {inc.status}
                  </span>

                </td>

                {/* Alert Count */}

                <td>

                  <div className="alert-count">
                    {inc.alert_count}
                  </div>

                </td>

                {/* Timeline */}

                <td>

                  <div className="timeline-info">

                    <span>
                      First:
                      {" "}
                      {inc.first_seen}
                    </span>

                    <span>
                      Last:
                      {" "}
                      {inc.last_seen}
                    </span>

                  </div>

                </td>

                {/* Actions */}

                <td>

                  {inc.status === "OPEN" ? (

                    <div className="action-buttons">

                      <button
                        className="btn btn-close"
                        onClick={() =>
                          closeIncident(inc._id)
                        }
                      >
                        Close
                      </button>

                      <button
                        className="btn btn-block"
                        onClick={() =>
                          blockIP(inc.ip)
                        }
                      >
                        Block
                      </button>

                    </div>

                  ) : (

                    <span className="resolved-text">
                      Resolved
                    </span>

                  )}

                </td>

              </tr>
            ))

          ) : (

            <tr>

              <td
                colSpan="8"
                className="empty-state"
              >
                No incidents found
              </td>

            </tr>

          )}
                    {/* add raw logs view button */}
        </tbody>

      </table>

    </div>
  );
};

export default IncidentTable;