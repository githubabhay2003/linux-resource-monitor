import psutil
import time
from datetime import datetime
import smtplib
from email.mime.text import MIMEText

# Thresholds
CPU_THRESHOLD = 1  # in percent
MEMORY_THRESHOLD = 1  # in percent
DISK_THRESHOLD = 1  # in percent

# Email Setup
EMAIL_ADDRESS = "sender@gmail.com"
EMAIL_PASSWORD = "gmail_app password"
TO_EMAIL = "receiver@gmail.com"

def send_email_alert(subject, body):
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = TO_EMAIL

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
    except Exception as e:
        print(f"Email failed: {e}")

def log_alert(message):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    full_message = f"[{timestamp}] {message}"
    with open("alerts.log", "a") as f:
        f.write(full_message + "\n")
    send_email_alert("⚠️ LRMAS Alert", full_message)

while True:
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent

    if cpu > CPU_THRESHOLD:
        log_alert(f"High CPU Usage: {cpu}%")

    if memory > MEMORY_THRESHOLD:
        log_alert(f"High Memory Usage: {memory}%")

    if disk > DISK_THRESHOLD:
        log_alert(f"High Disk Usage: {disk}%")

    time.sleep(5)

