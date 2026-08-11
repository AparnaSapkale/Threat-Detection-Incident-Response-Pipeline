import React, { useMemo, useState } from "react";
import "./rules.css";

const detectionRules = [
  {
    id: 1,
    name: "SSH Brute Force",
    severity: "High",
    status: "Enabled",
    logSource: "Linux Auth Logs",
    tactic: "Credential Access",
    tacticId: "TA0006",
    technique: "Brute Force",
    techniqueId: "T1110",
    threshold: "5 failed logins within 60 seconds",
    response: "Alert + Auto Block IP",
    description:
      "Detects repeated failed SSH login attempts indicating brute-force attacks.",
    logic: [
      "Monitor authentication logs",
      "Count failed SSH logins",
      "If failures ≥ 5 in 60 seconds",
      "Generate High Severity Alert",
      "Block source IP automatically",
    ],
  },
  {
    id: 2,
    name: "Port Scan Detection",
    severity: "Medium",
    status: "Enabled",
    logSource: "Firewall Logs",
    tactic: "Discovery",
    tacticId: "TA0007",
    technique: "Network Service Discovery",
    techniqueId: "T1046",
    threshold: "20 ports scanned in 30 seconds",
    response: "Generate Alert",
    description:
      "Detects hosts performing rapid scans across multiple ports.",
    logic: [
      "Monitor firewall logs",
      "Track destination ports",
      "More than 20 unique ports",
      "Generate Medium Severity Alert",
    ],
  },
  {
    id: 3,
    name: "Reverse Shell Detection",
    severity: "Critical",
    status: "Enabled",
    logSource: "Process Monitoring",
    tactic: "Execution",
    tacticId: "TA0002",
    technique: "Command & Scripting Interpreter",
    techniqueId: "T1059",
    threshold: "Known reverse shell command execution",
    response: "Alert + Kill Process + Block IP",
    description:
      "Detects reverse shell payload execution commonly used by attackers.",
    logic: [
      "Monitor process execution",
      "Detect suspicious shell commands",
      "Correlate outbound connection",
      "Generate Critical Alert",
      "Terminate process",
      "Block remote IP",
    ],
  },
  {
    id: 4,
    name: "SQL Injection Attempt",
    severity: "High",
    status: "Enabled",
    logSource: "Web Server Logs",
    tactic: "Initial Access",
    tacticId: "TA0001",
    technique: "Exploit Public Facing Application",
    techniqueId: "T1190",
    threshold: "Known SQLi payload detected",
    response: "Alert",
    description:
      "Detects SQL Injection payloads in HTTP requests.",
    logic: [
      "Inspect HTTP request",
      "Regex match SQL keywords",
      "Generate High Alert",
    ],
  },
  {
    id: 5,
    name: "XSS Attempt",
    severity: "Medium",
    status: "Enabled",
    logSource: "Web Logs",
    tactic: "Execution",
    tacticId: "TA0002",
    technique: "Command & Scripting Interpreter",
    techniqueId: "T1059",
    threshold: "JavaScript payload detected",
    response: "Alert",
    description:
      "Detects Cross Site Scripting attempts using malicious JavaScript.",
    logic: [
      "Inspect GET & POST parameters",
      "Detect script tags",
      "Generate Alert",
    ],
  },
  {
    id: 6,
    name: "Directory Enumeration",
    severity: "Medium",
    status: "Enabled",
    logSource: "Apache Logs",
    tactic: "Reconnaissance",
    tacticId: "TA0043",
    technique: "Active Scanning",
    techniqueId: "T1595",
    threshold: "Multiple 404 requests",
    response: "Alert",
    description:
      "Detects attackers enumerating hidden web directories.",
    logic: [
      "Count repeated 404 responses",
      "Multiple requests in short period",
      "Generate Alert",
    ],
  },
  {
    id: 7,
    name: "Privilege Escalation",
    severity: "Critical",
    status: "Enabled",
    logSource: "Linux Audit Logs",
    tactic: "Privilege Escalation",
    tacticId: "TA0004",
    technique: "Exploitation for Privilege Escalation",
    techniqueId: "T1068",
    threshold: "Unauthorized sudo execution",
    response: "Alert + Notify SOC",
    description:
      "Detects suspicious privilege escalation attempts.",
    logic: [
      "Monitor sudo commands",
      "Detect unusual privilege usage",
      "Generate Critical Alert",
    ],
  },
];

const Rules = () => {
  const [search, setSearch] = useState("");
  const [severityFilter, setSeverityFilter] = useState("All");
  const [statusFilter, setStatusFilter] = useState("All");
  const [selectedRule, setSelectedRule] = useState(null);

  const filteredRules = useMemo(() => {
    return detectionRules.filter((rule) => {
      const matchesSearch =
        rule.name.toLowerCase().includes(search.toLowerCase()) ||
        rule.technique.toLowerCase().includes(search.toLowerCase()) ||
        rule.techniqueId.toLowerCase().includes(search.toLowerCase());

      const matchesSeverity =
        severityFilter === "All" ||
        rule.severity === severityFilter;

      const matchesStatus =
        statusFilter === "All" ||
        rule.status === statusFilter;

      return (
        matchesSearch &&
        matchesSeverity &&
        matchesStatus
      );
    });
  }, [search, severityFilter, statusFilter]);

  const totalRules = detectionRules.length;

  const enabledRules = detectionRules.filter(
    (r) => r.status === "Enabled"
  ).length;

  const criticalRules = detectionRules.filter(
    (r) => r.severity === "Critical"
  ).length;

  const mitreCoverage = new Set(
    detectionRules.map((r) => r.techniqueId)
  ).size;
    return (
    <div className="rules-page">
      {/* ================= HEADER ================= */}
      <div className="rules-header">
        <div>
          <h1>Detection Rules</h1>
          <p>
            Detection playbooks mapped with MITRE ATT&CK techniques used by the
            SOC pipeline.
          </p>
        </div>
      </div>

      {/* ================= STATS ================= */}
      <div className="stats-grid">
        <div className="stat-card">
          <h2>{totalRules}</h2>
          <span>Total Rules</span>
        </div>

        <div className="stat-card">
          <h2>{enabledRules}</h2>
          <span>Enabled</span>
        </div>

        <div className="stat-card critical">
          <h2>{criticalRules}</h2>
          <span>Critical Rules</span>
        </div>

        <div className="stat-card">
          <h2>{mitreCoverage}</h2>
          <span>MITRE Techniques</span>
        </div>
      </div>

      {/* ================= FILTER BAR ================= */}

      <div className="filter-bar">

        <input
          type="text"
          placeholder="Search Rule, Technique or MITRE ID..."
          value={search}
          onChange={(e) => setSearch(e.target.value)}
        />

        <select
          value={severityFilter}
          onChange={(e) => setSeverityFilter(e.target.value)}
        >
          <option>All</option>
          <option>Critical</option>
          <option>High</option>
          <option>Medium</option>
          <option>Low</option>
        </select>

        <select
          value={statusFilter}
          onChange={(e) => setStatusFilter(e.target.value)}
        >
          <option>All</option>
          <option>Enabled</option>
          <option>Disabled</option>
        </select>

      </div>

      {/* ================= RULES ================= */}

      <div className="rules-grid">

        {filteredRules.map((rule) => (

          <div className="rule-card" key={rule.id}>

            <div className="rule-top">

              <h2>{rule.name}</h2>

              <div className="badge-group">

                <span
                  className={`severity ${rule.severity.toLowerCase()}`}
                >
                  {rule.severity}
                </span>

                <span
                  className={`status ${rule.status.toLowerCase()}`}
                >
                  {rule.status}
                </span>

              </div>

            </div>

            <p className="description">
              {rule.description}
            </p>

            <div className="rule-info">

              <div>
                <strong>Log Source</strong>
                <p>{rule.logSource}</p>
              </div>

              <div>
                <strong>Threshold</strong>
                <p>{rule.threshold}</p>
              </div>

              <div>
                <strong>Response</strong>
                <p>{rule.response}</p>
              </div>

            </div>

            <div className="mitre-section">

              <div className="mitre-box">
                <span className="mitre-title">
                  Tactic
                </span>

                <strong>
                  {rule.tacticId}
                </strong>

                <p>{rule.tactic}</p>
              </div>

              <div className="mitre-box">

                <span className="mitre-title">
                  Technique
                </span>

                <strong>
                  {rule.techniqueId}
                </strong>

                <p>{rule.technique}</p>

              </div>

            </div>

            <button
              className="logic-btn"
              onClick={() => setSelectedRule(rule)}
            >
              View Detection Logic
            </button>

          </div>

        ))}

      </div>

      {/* ================= MODAL ================= */}

      {selectedRule && (

        <div
          className="modal-overlay"
          onClick={() => setSelectedRule(null)}
        >

          <div
            className="modal"
            onClick={(e) => e.stopPropagation()}
          >

            <div className="modal-header">

              <h2>{selectedRule.name}</h2>

              <button
                className="close-btn"
                onClick={() => setSelectedRule(null)}
              >
                ✕
              </button>

            </div>

            <div className="modal-content">

              <h3>Description</h3>

              <p>{selectedRule.description}</p>

              <h3>MITRE ATT&CK</h3>

              <div className="modal-mitre">

                <div>

                  <strong>
                    {selectedRule.tacticId}
                  </strong>

                  <p>{selectedRule.tactic}</p>

                </div>

                <div>

                  <strong>
                    {selectedRule.techniqueId}
                  </strong>

                  <p>{selectedRule.technique}</p>

                </div>

              </div>

              <h3>Detection Logic</h3>

              <ol>

                {selectedRule.logic.map((step, index) => (
                  <li key={index}>
                    {step}
                  </li>
                ))}

              </ol>

              <h3>Response Action</h3>

              <p>{selectedRule.response}</p>

            </div>

          </div>

        </div>

      )}

    </div>
  );
};

export default Rules;