from pathlib import Path
from datetime import datetime
import pandas as pd

from src.data_loader import (
    load_contacts,
    load_reminders,
    get_eligible_contacts
)
from src.email_generator import load_template, generate_email
from src.email_sender import send_email

def process_due_reminders(project_dir, dry_run=True):
    """Process due reminders once and save their processing status."""
    project_dir = Path(project_dir)
    
    contacts_path = project_dir / "data" / "contacts.csv"
    reminders_path = project_dir / "data" / "reminders.csv"
    template_path = project_dir / "templates" / "email_template.txt"
    
    contacts = load_contacts(contacts_path)
    reminders = load_reminders(reminders_path)
    eligible = get_eligible_contacts(contacts)
    
    template = load_template(template_path)
    now = datetime.now()
    
    results = []
    
    for index, reminder in reminders.iterrows():
        if str(reminder["status"]).strip().lower() != "pending":
            continue
            
        scheduled = datetime.strptime(
            f"{reminder['scheduled_date']} {reminder['scheduled_time']}",
            "%Y-%m-%d %H:%M"
        )
        
        if scheduled > now:
            continue
            
        contact_rows = eligible[
            eligible["contact_id"] == reminder["contact_id"]
        ]
        
        if contact_rows.empty:
            continue
            
        contact = contact_rows.iloc[0]
        email_data = generate_email(contact, reminder, template)
        
        try:
            result = send_email(email_data, dry_run=dry_run)
            reminders.at[index, "status"] = result["status"]
            
            results.append({
                "reminder_id": reminder["reminder_id"],
                "contact_id": reminder["contact_id"],
                "recipient": result["recipient"],
                "subject": result["subject"],
                "status": result["status"],
                "execution_time": datetime.now().isoformat(timespec="seconds"),
                "message": result["message"]
            })
        except Exception as error:
            reminders.at[index, "status"] = "Failed"
            results.append({
                "reminder_id": reminder["reminder_id"],
                "contact_id": reminder["contact_id"],
                "recipient": contact["email"],
                "subject": reminder["subject"],
                "status": "Failed",
                "execution_time": datetime.now().isoformat(timespec="seconds"),
                "message": str(error)
            })
            
    reminders.to_csv(reminders_path, index=False)
    return results
