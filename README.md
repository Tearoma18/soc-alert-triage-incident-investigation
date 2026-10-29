# SOC Alert Triage and Incident Investigation Lab

## Overview

This project demonstrates a simulated Security Operations Center (SOC) investigation workflow using Python to analyze authentication logs, identify suspicious login patterns, and document investigation findings.

The lab focuses on basic log analysis, alert triage, incident documentation, severity assessment, and recommended response actions.

**Project type:** Hands-on cybersecurity lab  
**Environment:** Local Python environment  
**Data source:** Synthetic authentication logs  
**Incident ID:** LAB-IR-001

## Objectives

- Analyze authentication events using Python.
- Identify repeated failed login attempts and suspicious login sequences.
- Summarize failed and successful authentication events.
- Document investigation findings and a chronological event timeline.
- Assess potential security risks while distinguishing confirmed facts from possible explanations.
- Recommend appropriate investigation, containment, and follow-up steps.

## Tools and Technologies

- **Python 3** — log parsing and basic analysis.
- **Regular expressions (Regex)** — extraction of authentication event details.
- **Windows Command Prompt** — execution of the analysis script.
- **Markdown** — investigation reports and technical documentation.
- **GitHub** — project versioning and portfolio presentation.

## Lab Scenario

The lab uses a synthetic authentication log containing successful and failed login attempts for two fictional users.

The Python script analyzes the events and flags a successful authentication that follows multiple failed attempts from the same source IP address.

This pattern may indicate password guessing or another suspicious authentication sequence. However, repeated failures followed by a successful login do not independently confirm unauthorized access.

## Methodology

1. Created a synthetic authentication log for the investigation.
2. Developed a Python script to parse the log entries.
3. Counted authentication events and summarized failed and successful attempts.
4. Examined login sequences associated with the same user and source IP address.
5. Identified a suspicious sequence for further investigation.
6. Documented the timeline, assessment, limitations, and recommended response.
7. Prepared an incident investigation report with a provisional severity assessment.

## Findings

The supplied synthetic dataset contains the following events:

| Metric | Result |
|---|---:|
| Total authentication events | 8 |
| Failed authentication attempts | 6 |
| Successful authentication attempts | 2 |

The analysis identified four consecutive failed authentication attempts for user `alex` from `192.0.2.45`, followed by a successful authentication from the same address.

This activity was flagged for further investigation. The available evidence does not establish that the account was compromised.

## Repository Structure

soc-alert-triage-incident-investigation/
├── analyze_logs.py
├── evidence/
│   └── findings.md
├── investigation/
│   ├── alert_analysis.md
│   └── incident_report.md
├── logs/
│   └── simulated_auth.log
├── screenshots/
│   ├── analysis-output1.png
│   ├── analysis-output2.png
│   ├── incident-investigation-report1.png
│   ├── incident-investigation-report2.png
│   ├── project-structure.png
│   └── python-script-run.png
└── README.md

## How to Run

### Prerequisites
- Python 3 installed on your computer.
- The project files downloaded or cloned locally.

### Execution

From the project root directory, run:

bash
python analyze_logs.py

The script reads the synthetic authentication log and prints a summary of the events and any suspicious login sequence identified by its detection logic.

## Investigation Documentation

- **Findings:** `evidence/findings.md`
- **Alert analysis:** `investigation/alert_analysis.md`
- **Incident report:** `investigation/incident_report.md`
- **Sample authentication data:** `logs/simulated_auth.log`
- **Screenshots:** `screenshots/`

## Limitations

- The authentication data is synthetic and does not represent a live production environment.
- No real user accounts or systems were investigated.
- The lab does not include endpoint telemetry, multifactor authentication records, geolocation, or session activity.
- The source IP addresses and authentication events were not independently validated.
- The investigation flag indicates a suspicious pattern, not confirmed account compromise.
- No real containment, remediation, or incident escalation actions were performed.

## Skills Demonstrated

- Authentication log analysis
- Python scripting and regular expressions
- Basic alert triage
- Identification of suspicious login patterns
- Incident timeline development
- Evidence documentation
- Preliminary severity assessment
- Incident response recommendations
- Technical reporting

## Disclaimer

This project was created for educational and portfolio purposes. All users, events, and authentication data are fictional. The findings and recommended actions are illustrative and do not represent a confirmed security incident.

