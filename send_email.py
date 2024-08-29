import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email configuration
sender_email = "youremail@example.com"
sender_password = "yourpassword"
recipients = ["recipient1@example.com", "recipient2@example.com"]
subject = "Daily Report"
body = "Hello,\n\nThis is your daily report. Please review the attached files.\n\nBest regards,\nYour Name"

# Create the email message
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = ", ".join(recipients)
msg['Subject'] = subject

# Attach the body of the email
msg.attach(MIMEText(body, 'plain'))

# Set up the SMTP server
smtp_server = "smtp.example.com"  # Replace with your email provider's SMTP server
smtp_port = 587  # Commonly used port for SMTP

try:
    # Start the SMTP server and login
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_email, sender_password)

    # Send the email
    server.sendmail(sender_email, recipients, msg.as_string())
    print("Email sent successfully!")

except Exception as e:
    print(f"Failed to send email: {e}")

finally:
    # Terminate the SMTP session
    server.quit()
