import hashlib
import os
import time
import smtplib
from email.mime.text import MIMEText

# Function to calculate the hash of a file
def calculate_hash(file_path):
    with open(file_path, 'rb') as f:
        file_data = f.read()
        return hashlib.sha256(file_data).hexdigest()

# Send alert email
def send_alert(subject, body, to_email):
    from_email = "your_email@gmail.com"
    password = "your_email_password"

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(from_email, password)
    server.sendmail(from_email, to_email, msg.as_string())
    server.quit()

# Monitor file integrity
def monitor_file(file_path, check_interval=60):
    if not os.path.exists(file_path):
        print(f"Error: {file_path} does not exist!")
        return

    last_hash = calculate_hash(file_path)
    print(f"Monitoring {file_path}...")

    while True:
        time.sleep(check_interval)
        current_hash = calculate_hash(file_path)

        if current_hash != last_hash:
            print(f"Change detected in {file_path}!")
            send_alert(
                subject="File Change Alert",
                body=f"The file {file_path} has been changed.",
                to_email="alert_recipient@gmail.com"
            )
            last_hash = current_hash

# Define file to monitor
file_to_monitor = '/etc/passwd'  # Change this to the file path you want to monitor

# Start monitoring
monitor_file(file_to_monitor)
