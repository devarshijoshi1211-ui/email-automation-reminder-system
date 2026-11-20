import pandas as pd
from pathlib import Path

def load_contacts(file_path):
    """Load and validate contact records."""
    contacts = pd.read_csv(file_path)
    required_columns = [
        "contact_id", "name", "email", 
        "department", "company", "status", "email_opt_in"
    ]
    missing = set(required_columns) - set(contacts.columns)
    if missing:
        raise ValueError(f"Missing contact columns: {sorted(missing)}")
    return contacts

def load_reminders(file_path):
    """Load and validate reminder records."""
    reminders = pd.read_csv(file_path)
    required_columns = [
        "reminder_id", "contact_id", "reminder_type", 
        "subject", "scheduled_date", "scheduled_time", 
        "status", "template_name"
    ]
    missing = set(required_columns) - set(reminders.columns)
    if missing:
        raise ValueError(f"Missing reminder columns: {sorted(missing)}")
    return reminders

def validate_reminder_contacts(contacts, reminders):
    """Ensure every reminder references an existing contact."""
    valid_ids = set(contacts["contact_id"])
    invalid = reminders[~reminders["contact_id"].isin(valid_ids)]
    if not invalid.empty:
        raise ValueError(f"Unknown contact IDs in reminders: {invalid['contact_id'].tolist()}")
    return True

def get_eligible_contacts(contacts):
    """Return only active contacts who have opted in."""
    eligible = contacts[
        (contacts["status"].str.strip().str.lower() == "active") &
        (contacts["email_opt_in"].str.strip().str.lower() == "yes")
    ].copy()
    return eligible
