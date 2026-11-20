import logging
import os
import smtplib
from email.message import EmailMessage

logger = logging.getLogger(__name__)

def send_email(email_data, dry_run=True):
    """Simulate or send an email using SMTP."""
    if dry_run:
        logger.info(
            "DRY RUN: Email simulated for %s | Subject: %s",
            email_data["to"],
            email_data["subject"]
        )
        return {
            "recipient": email_data["to"],
            "subject": email_data["subject"],
            "status": "Simulated",
            "message": "Dry-run successful. No email was sent."
        }

    if os.getenv("ALLOW_REAL_EMAILS", "false").lower() != "true":
        raise RuntimeError(
            "Real email sending is disabled. "
            "Set ALLOW_REAL_EMAILS=true only when ready."
        )

    smtp_host = os.getenv("SMTP_HOST")
    smtp_port = int(os.getenv("SMTP_PORT", "587"))
    smtp_username = os.getenv("SMTP_USERNAME")
    smtp_password = os.getenv("SMTP_PASSWORD")
    sender_email = os.getenv("SENDER_EMAIL")

    if not all([smtp_host, smtp_username, smtp_password, sender_email]):
        raise ValueError("SMTP configuration is incomplete.")

    message = EmailMessage()
    message["From"] = sender_email
    message["To"] = email_data["to"]
    message["Subject"] = email_data["subject"]
    message.set_content(email_data["body"])

    with smtplib.SMTP(smtp_host, smtp_port, timeout=30) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.send_message(message)

    logger.info("Email sent successfully to %s", email_data["to"])
    return {
        "recipient": email_data["to"],
        "subject": email_data["subject"],
        "status": "Sent",
        "message": "Email sent successfully."
    }
