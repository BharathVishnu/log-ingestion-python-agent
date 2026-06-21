# Log Ingestion Python Agent

A lightweight Python-based log ingestion agent designed to collect, process, and forward application logs for centralized monitoring, analysis, and observability.

## eatures

- Real-time log monitoring
- Log parsing and processing
- Structured log generation
- Configurable log sources
- Error handling and retries
- Lightweight and extensible architecture
- Easy integration with downstream systems

---

## Architecture

```text
Application Logs
       │
       ▼
┌─────────────────┐
│ Log Ingestion   │
│ Python Agent    │
└─────────────────┘
       │
       ▼
Log Processing & Parsing
       │
       ▼
Structured Output
       │
       ▼
Storage / Analytics Platform
```

---

## Project Structure

```text
log-ingestion-python-agent/
│
├── agent/
│   ├── ingestion.py
│   ├── parser.py
│   ├── processor.py
│   └── utils.py
│
├── config/
│   └── config.yaml
│
├── logs/
│
├── requirements.txt
├── README.md
└── main.py
```

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/BharathVishnu/log-ingestion-python-agent.git

cd log-ingestion-python-agent
```

### Create Virtual Environment

```bash
python -m venv .venv
```

#### Windows

```bash
.venv\Scripts\activate
```

#### Linux / Mac

```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Application

```bash
python main.py
```

The agent will start monitoring configured log sources and process incoming log entries.

---

## Configuration

Example configuration:

```yaml
log_file: logs/application.log

poll_interval: 5

output_format: json
```

---

## Sample Log Input

```text
2026-06-20 12:30:15 INFO User login successful
2026-06-20 12:30:18 ERROR Database connection failed
```

---

## Sample Processed Output

```json
{
  "timestamp": "2026-06-20T12:30:18",
  "level": "ERROR",
  "message": "Database connection failed"
}
```

---

## Tech Stack

- Python
- File Monitoring
- JSON Processing
- Logging Frameworks

---

## Learning Outcomes

This project demonstrates:

- Log ingestion pipelines
- File monitoring techniques
- Stream processing fundamentals
- Data transformation and parsing
- Backend system design
- Error handling and resilience patterns

---

## Future Enhancements

- Kafka Integration
- AI-powered Log Analysis

---

## Author

**Bharath Vishnu**
**Tanu Rawat**


---
⭐ If you found this project useful, consider giving it a star.
