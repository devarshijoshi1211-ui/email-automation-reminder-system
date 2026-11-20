from pathlib import Path

def load_template(template_path):
    """Read an email template from a text file."""
    return Path(template_path).read_text(encoding="utf-8")

def generate_email(contact, reminder, template):
    """Generate a personalized email for one reminder."""
    placeholders = {
        "name": contact["name"],
        "company": contact["company"],
        "reminder_type": reminder["reminder_type"],
        "subject": reminder["subject"],
        "scheduled_date": reminder["scheduled_date"],
        "scheduled_time": reminder["scheduled_time"]
    }
    body = template.format(**placeholders)
    return {
        "to": contact["email"],
        "subject": reminder["subject"],
        "body": body
    }
