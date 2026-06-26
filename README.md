Threat Detection & Incident Response Pipeline

The Threat-Detection-Incident-Response-Pipeline project is designed to demonstrate and simulate the workflow of a Security Operations Center (SOC) analyst.
It focuses on the end-to-end process of threat detection, analysis, and automated incident response.

🚀 Key Features
    Threat Detection via Log Analysis
        Analyze logs generated from endpoint devices to identify potential security threats.
    Automated Incident Response
        Automatically block high-severity threat IP addresses to mitigate risks in real time.
    Real-Time Threat Monitoring
        Detect live threats and generate alerts for immediate attention.
    Dashboard for Alert Visualization
        Provide a centralized dashboard to monitor daily alerts and system activity.
    Daily Activity Reporting
        Generate reports with visual dashboards summarizing daily security events and actions.
        
🔧 Additional Features
      Investigation Capabilities
      Enables analysts to perform detailed investigations on detected incidents.
      
 📌 Upcoming Enhancements
      Add automated playbooks for structured incident response (affected device containment)
      Introduce new alert types for broader threat coverage 
      Provide comprehensive user guidelines for the pipeline (How it works)
      Integrate with security tools such as EDR, SOAR and DSP/ISP platforms to enhance automation and orchestration

## 📂 Project Structure

```
Threat-Detection-Incident-Response-Pipeline
│
├── backend/
│   ├── database/
│   │   └── db.py
│   │
│   ├── models/
│   │   ├── alert_model.py
│   │   └── incident_model.py
│   │
│   ├── monitor/
│   │   ├── core/
│   │   │   ├── correlation.py
│   │   │   ├── duplicate.py
│   │   │   └── state.py
│   │   │
│   │   ├── detectors/
│   │   │   ├── reverse_shell_detector.py
│   │   │   ├── scan_detector.py
│   │   │   └── ssh_detector.py
│   │   │
│   │   ├── utils/
│   │   │   ├── network.py
│   │   │   └── sender.py
│   │   │
│   │   ├── config.py
│   │   ├── config_loader.py
│   │   ├── detector.py
│   │   ├── main_monitor.py
│   │   ├── sender.py
│   │   └── utils.py
│   │
│   ├── routes/
│   │   ├── admin_routes.py
│   │   ├── alert_routes.py
│   │   ├── dashboard_routes.py
│   │   ├── incident_routes.py
│   │   ├── report_routes.py
│   │   └── stats_routes.py
│   │
│   ├── services/
│   │   ├── admin_service.py
│   │   ├── alert_service.py
│   │   ├── config_service.py
│   │   ├── detection_service.py
│   │   ├── incident_service.py
│   │   ├── report_service.py
│   │   ├── response_service.py
│   │   ├── rules_service.py
│   │   └── soar_service.py
│   │
│   ├── utils/
│   │   ├── constants.py
│   │   ├── helpers.py
│   │   └── logger.py
│   │
│   └── main.py
│
├── frontend/
│   ├── public/
│   │
│   ├── src/
│   │   ├── components/
│   │   │   ├── AlertTable.jsx
│   │   │   ├── AttackChart.jsx
│   │   │   ├── FilterPanel.jsx
│   │   │   ├── Footer.jsx
│   │   │   ├── IncidentTable.jsx
│   │   │   ├── Loader.jsx
│   │   │   ├── Navbar.jsx
│   │   │   ├── SearchBar.jsx
│   │   │   ├── Sidebar.jsx
│   │   │   ├── StatsCard.jsx
│   │   │   ├── StatsCards.jsx
│   │   │   └── TopIPsChart.jsx
│   │   │
│   │   ├── pages/
│   │   │   ├── Admin.jsx
│   │   │   ├── Alerts.jsx
│   │   │   ├── Dashboard.jsx
│   │   │   ├── Incidents.jsx
│   │   │   ├── Investigation.jsx
│   │   │   ├── Reports.jsx
│   │   │   ├── Response.jsx
│   │   │   └── Rules.jsx
│   │   │
│   │   ├── services/
│   │   │   └── api.js
│   │   │
│   │   ├── styles/
│   │   │   ├── components/
│   │   │   │   ├── buttons.css
│   │   │   │   ├── chart.css
│   │   │   │   ├── footer.css
│   │   │   │   ├── navbar.css
│   │   │   │   ├── sidebar.css
│   │   │   │   ├── statscards.css
│   │   │   │   └── table.css
│   │   │   │
│   │   │   └── pages/
│   │   │       ├── dashboard.css
│   │   │       ├── global.css
│   │   │       ├── incidents.css
│   │   │       ├── investigation.css
│   │   │       └── reports.css
│   │   │
│   │   ├── utils/
│   │   │   ├── formatTime.js
│   │   │   ├── riskCalculator.js
│   │   │   └── severityColor.js
│   │   │
│   │   ├── App.js
│   │   ├── App.css
│   │   ├── index.js
│   │   └── index.css
│   │
│   ├── package.json
│   ├── package-lock.json
│   ├── tailwind.config.js
│   └── postcss.config.js
│
├── .gitignore
└── README.md
```
