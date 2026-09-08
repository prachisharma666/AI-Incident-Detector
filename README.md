# 🤖 AAIAS Project (AI Incident Detector)

An intelligent, multi-agent diagnostic command center designed for Site Reliability Engineering (SRE) and DevOps teams. The AI Incident Detector automates the critical diagnostic phase of system outages—bridging statistical Z-score anomaly detection, text log analysis, and generative AI reasoning to isolate root causes in seconds.

---

## 🌟 Key Features

- **Interactive Simulation Engine:** Simulate realistic production failure modes (`payment_failure`, `database_slowdown`, `traffic_spike`) without needing live infrastructure.
- **Statistical Z-Score Anomaly Detection:** Dynamically profiles baseline telemetry data to catch abnormal spikes and behavioral shifts.
- **Multi-Agent AI Architecture:** Powered by Google GenAI (`gemini-3.6-flash`), specialized agents independently investigate distinct facets of an incident:
  - **Data Agent (`data_agent.py`):** Evaluates metric anomalies for technical and business impact.
  - **Log Agent (`log_agent.py`):** Scans raw text system logs for error signatures and failure codes.
  - **Root Cause Agent (`root_cause_agent.py`):** Synthesizes multi-agent findings into a structured JSON diagnostic report (Severity, Confidence, Root Cause, Summary).
- **FastAPI Backend (`app/main.py`):** High-performance asynchronous REST API orchestration.
- **Corporate SaaS Dashboard (`templates/index.html`):** Clean web interface for triggering failure simulations and viewing real-time agent telemetry and root cause analysis.

---

## 📁 Project Directory Structure

```text
AAIAS_Project/
│
├── agents/
│   ├── data_agent.py          # AI agent for analyzing metric anomalies
│   ├── log_agent.py           # AI agent for parsing raw text system logs
│   └── root_cause_agent.py    # AI agent for synthesizing final JSON reports
│
├── app/
│   └── main.py                # FastAPI application and route orchestration
│
│
├── detection/
│   └── da/
│       ├── anomaly_detection.py # Z-score statistical anomaly computation
│       └── incident_detector.py # Rule-based incident validation logic
│
├── simulations/
│   └── simulation.py          # Generates baseline metrics and failure scenarios
│
├── templates/
│   └── index.html             # Corporate SaaS frontend interface
│
├── tests/
│   └── test_detection.py      # Pytest suite for automated pipeline verification
│
├── .env                       # Environment variables (Gemini API key)
├── .gitignore                 # Git ignore rules
└── requirements.txt           # Project dependencies