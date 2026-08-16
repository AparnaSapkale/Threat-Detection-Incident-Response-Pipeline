# Threat Detection & Incident Response Pipeline

The **Threat Detection & Incident Response Pipeline** is a Security Operations Center (SOC) simulation project that demonstrates the complete lifecycle of security monitoring, threat detection, incident investigation, and automated response.

The project collects and analyzes security events from monitored systems, detects suspicious activities using custom detection rules, generates alerts, manages incidents, and provides dashboards and reports to help security analysts investigate and respond to cyber threats.

---

## 🚀 Key Features

### 🔍 Threat Detection
- Detects suspicious activities through log analysis.
- Supports custom detection rules for multiple attack scenarios.
- Generates real-time security alerts.

### 🚨 Alert Management
- Displays alerts with severity, attack type, source IP, destination IP, attack count, and risk level.
- Real-time alert updates with automatic refresh.
- Search and filtering capabilities.

### 🛡️ Incident Management
- Convert alerts into security incidents.
- Track incident status throughout the investigation lifecycle.
- Centralized incident management dashboard.

### 🔎 Investigation
- Investigate suspicious IP addresses and related activities.
- View attack history and correlated events.
- Simplifies threat analysis for SOC analysts.

### 📊 Dashboard
- Real-time visualization of security events.
- Attack statistics and severity distribution.
- Top attacking IPs and security metrics.

### 📈 Reports
- Generate security reports for detected threats and incidents.
- Summarize daily security events.
- Visual analytics for SOC reporting.

### ⚡ Automated Response
- Automatically blocks high-severity malicious IP addresses.
- Designed for future SOAR integration.

---

## 📸 Project Screenshots

### Dashboard

<img width="1915" height="982" alt="Screenshot 2026-08-16 195314" src="https://github.com/user-attachments/assets/897764d0-f56c-4473-8d54-177ea9515d02" />

---

### Incidents

<img width="1919" height="980" alt="Screenshot 2026-08-16 195338" src="https://github.com/user-attachments/assets/bf242f9d-86b4-4812-b473-751053f30744" />


---

### Investigation

<img width="1917" height="977" alt="Screenshot 2026-08-16 195358" src="https://github.com/user-attachments/assets/a8650b22-56ba-4b0b-bfde-f523176e2c70" />


---

### Reports

<img width="1919" height="977" alt="Screenshot 2026-08-16 195419" src="https://github.com/user-attachments/assets/17f99e9d-98fd-44f0-8677-8d4c113df654" />


---

### Detection Rules

<img width="1916" height="989" alt="Screenshot 2026-08-16 195448" src="https://github.com/user-attachments/assets/0c6fe922-9b1a-4da0-88f4-017b1c7ae120" />
<img width="1642" height="958" alt="Screenshot 2026-08-16 195527" src="https://github.com/user-attachments/assets/8e8b9a8c-bcdd-4965-a601-170c6f99ecf5" />
<img width="1919" height="981" alt="Screenshot 2026-08-16 195547" src="https://github.com/user-attachments/assets/9121f2f9-6454-4bcf-9b7d-990946b6a059" />


---

## 🔧 Technologies Used

### Frontend
- React.js
- CSS
- JavaScript

### Backend
- FastAPI
- Python

### Database
- MongoDB

### Security & Detection
- Custom Detection Engine
- Log Analysis
- Threat Correlation
- Automated Response

---

## 📌 Upcoming Enhancements

- Add automated response playbooks for incident containment.
- Integrate SOAR platforms for response orchestration.
- Integrate EDR solutions for endpoint visibility.
- Add MITRE ATT&CK technique mapping.
- Support additional attack detection rules.
- Raw log viewer for alerts.
- Advanced filtering and search capabilities.
- User authentication and role-based access control.
- Email and Slack alert notifications.
- Comprehensive user documentation.

---

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

---

## 🎯 Project Workflow

```
Endpoint Logs
      │
      ▼
Detection Engine
      │
      ▼
Alert Generation
      │
      ▼
Incident Creation
      │
      ▼
Investigation
      │
      ▼
Automated Response
      │
      ▼
Dashboard & Reports
```

---

## 💡 Future Scope

- SOAR Integration
- EDR Integration
- Threat Intelligence Feeds
- Email Notifications
- MITRE ATT&CK Mapping
- IOC Management
- Case Management
- Analyst Notes
- Audit Logs
- Multi-source Log Collection
