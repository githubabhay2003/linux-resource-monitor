# 🖥️ LRMAS - Linux Resource Monitoring & Alert System

A lightweight Python-based Linux resource monitoring tool that runs as a background systemd service and sends real-time alerts via email when CPU, memory, or disk usage exceeds defined thresholds.

---

## 🚀 Features

- Monitors:
  - ✅ CPU usage
  - ✅ RAM usage
  - ✅ Disk space
- Sends email alerts using Gmail SMTP
- Auto-logs warnings to a local file
- Runs in background using `systemd`
- Lightweight and easy to configure

---

## 🛠️ Requirements

- Python 3.x
- `psutil`, `smtplib`, `email.mime` (standard)
- Gmail account with App Password enabled

Install dependencies:
```bash
pip3 install psutil
