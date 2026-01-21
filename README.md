# Linux Resource Monitoring & Alerting Tool

A lightweight Linux system monitoring tool built with Python to track CPU, memory, and disk usage, log metrics periodically, and trigger alerts when defined thresholds are exceeded.

This project was built as a small, practical SRE-style monitoring agent focusing on observability, automation, and operational clarity.

---

## Features

- Periodic monitoring of:
  - CPU usage
  - Memory usage
  - Disk usage (root filesystem)
- Structured logging with timestamps
- Threshold-based alerting
- Graceful shutdown handling (Ctrl+C)
- Configurable thresholds and check intervals
- No external dependencies (standard library only)

---

## Project Structure
```
linux-resource-monitor/
├── monitor.py # Main monitoring logic
├── config.py # Thresholds and configuration
├── README.md
├── requirements.txt
├── logs/
│ ├── metrics.log # Resource usage logs
│ └── alerts.log # Alert events
└── venv/ # Python virtual environment 
```
## Environment Setup

This project uses a Python virtual environment to isolate dependencies and avoid modifying system-level Python packages.

```bash
python3 -m venv venv
source venv/bin/activate
```

No external Python packages are required.

##Configuration

Monitoring thresholds and check intervals can be configured in config.py:
```
CPU_THRESHOLD = 80      # percent
MEM_THRESHOLD = 75      # percent
DISK_THRESHOLD = 70     # percent
CHECK_INTERVAL = 5      # seconds
```

### Running the Monitor

From the project root:

```python3 monitor.py ```

On startup, the monitor will:
  Begin collecting metrics at the configured interval
  Write usage data to logs/metrics.log
  Write alert events to logs/alerts.log
  Print minimal live status updates to the terminal

Press Ctrl+C to stop the monitor gracefully.

## Logs
Metrics Log (logs/metrics.log)

Contains periodic snapshots of system resource usage:

```2026-01-21 18:42:06 | CPU:5.1% MEM:43.0% DISK:61.0%```

Alerts Log (logs/alerts.log)

Contains alert events and operational messages:

```ALERT | 2026-01-21 19:12:44 | CPU usage high: 92.3% ```
``` ALERT | 2026-01-21 19:14:02 | Monitor stopped by user (Ctrl+C) ```

Logs are append-only and designed for inspection using standard Linux tools such as less, tail, and grep.

## Testing & Validation

The tool was tested by:
  Running under normal system load
  Generating synthetic CPU load to trigger alerts
  Verifying log output and alert behavior
  Confirming graceful shutdown via Ctrl+C

System metrics were cross-validated using standard Linux tools (top, free, df).

