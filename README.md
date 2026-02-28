### **DFIR Triage Collector**



A lightweight, Windows-first Digital Forensics \& Incident Response (DFIR) triage collection tool designed to rapidly gather high-value host artifacts for investigation.



**This tool focuses on:**



* Read-only artifact collection
* Fast execution for live-response scenarios
* Structured output (raw text + manifest with SHA256 hashes)
* Simple CLI-based workflow



Built as part of an applied cybersecurity tooling project.



#### **Purpose**



When responding to a suspected incident, time matters.



This tool allows responders to quickly collect:

* Host identification data
* Running processes
* Network connections
* Active servicesIP configuration
* System information



All outputs are written to a structured case directory and hashed for integrity verification.



#### **Requirements**



* Python 3.10+
* Windows OS (v0.1.0 supports Windows only)
* Administrator privileges recommended for full artifact access (required for certain future features like EVTX export)



#### **Installation**



***Clone the repository:***



git clone https://github.com/brandenvtcybersec/dfir-triage-collector.git

cd dfir-triage-collector



***Create and activate a virtual environment:***



python -m venv .venv

.venv\\Scripts\\activate



***Install in editable mode:***



pip install -e .



#### **Usage**



***Run a triage collection:***



dfir-triage --case INC-001



***Optional parameters:***



dfir-triage --case INC-001 --out cases

dfir-triage --case INC-001 --no-zip



#### **Output Structure**



Example output:



cases/

└── INC-001/

&nbsp;   ├── raw/

&nbsp;   │   ├── hostname.txt

&nbsp;   │   ├── systeminfo.txt

&nbsp;   │   ├── tasklist.txt

&nbsp;   │   ├── netstat.txt

&nbsp;   │   └── ipconfig.txt

&nbsp;   ├── manifest.json

└── INC-001.zip

raw/



Contains command output artifacts collected from the host.



manifest.json



Contains:



* Case ID
* Timestamp metadata
* SHA256 hash of each collected file



This allows integrity validation and chain-of-custody verification.



#### **Design Principles**



* Read-only collection
* No registry modification
* No persistence changes
* No artifact deletion
* Transparent command execution
* Evidence hashing



This tool is designed for safe live triage, not full forensic acquisition.



#### **Roadmap**



Planned improvements (v0.2+):



* Windows Event Log (EVTX) export
* PowerShell operational log collection
* Scheduled task enumeration
* Persistence artifact triage
* Structured JSON summary output
* Command execution logging
* Modular collector profiles (quick / full)



#### **Disclaimer**



This tool is intended for educational and legitimate security operations use only.



Use only on systems you own or have explicit authorization to assess.



#### **Author**



Branden V.T.

Cybersecurity \& DFIR Tooling Project

