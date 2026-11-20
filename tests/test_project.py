import unittest
import tempfile
import shutil
from pathlib import Path
import pandas as pd

from src.data_loader import load_contacts, load_reminders, get_eligible_contacts
from src.email_generator import load_template, generate_email
from src.scheduler import process_due_reminders
from src.report_generator import generate_report

PROJECT_DIR = Path(__file__).resolve().parents[1]

class EmailAutomationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.test_dir = Path(self.temp.name)
        for folder in ["data", "templates", "outputs", "logs"]:
            (self.test_dir / folder).mkdir(parents=True)
        shutil.copy2(PROJECT_DIR / "data" / "contacts.csv", self.test_dir / "data" / "contacts.csv")
        shutil.copy2(PROJECT_DIR / "data" / "reminders.csv", self.test_dir / "data" / "reminders.csv")
        shutil.copy2(PROJECT_DIR / "templates" / "email_template.txt", self.test_dir / "templates" / "email_template.txt")
        reminders = pd.read_csv(self.test_dir / "data" / "reminders.csv")
        reminders["scheduled_date"] = "2000-01-01"
        reminders["scheduled_time"] = "00:00"
        reminders["status"] = "Pending"
        reminders.to_csv(self.test_dir / "data" / "reminders.csv", index=False)

    def tearDown(self):
        self.temp.cleanup()

    def test_data_loading(self):
        contacts = load_contacts(self.test_dir / "data" / "contacts.csv")
        reminders = load_reminders(self.test_dir / "data" / "reminders.csv")
        self.assertEqual(len(contacts), 8)
        self.assertEqual(len(reminders), 7)

    def test_consent_filtering(self):
        contacts = load_contacts(self.test_dir / "data" / "contacts.csv")
        eligible = get_eligible_contacts(contacts)
        self.assertEqual(len(eligible), 7)
        self.assertNotIn("C006", eligible["contact_id"].values)

    def test_email_generation(self):
        contacts = load_contacts(self.test_dir / "data" / "contacts.csv")
        reminders = load_reminders(self.test_dir / "data" / "reminders.csv")
        eligible = get_eligible_contacts(contacts)
        template = load_template(self.test_dir / "templates" / "email_template.txt")
        email_data = generate_email(eligible.iloc[0], reminders.iloc[0], template)
        self.assertTrue(email_data["to"])
        self.assertTrue(email_data["subject"])
        self.assertIn("Hello", email_data["body"])

    def test_scheduler_processing(self):
        results = process_due_reminders(self.test_dir, dry_run=True)
        self.assertEqual(len(results), 7)
        self.assertTrue(all(item["status"] == "Simulated" for item in results))

    def test_duplicate_prevention(self):
        first_run = process_due_reminders(self.test_dir, dry_run=True)
        second_run = process_due_reminders(self.test_dir, dry_run=True)
        self.assertEqual(len(first_run), 7)
        self.assertEqual(len(second_run), 0)

    def test_report_generation(self):
        results = process_due_reminders(self.test_dir, dry_run=True)
        report_path = self.test_dir / "outputs" / "email_report.csv"
        report = generate_report(results, report_path)
        self.assertEqual(len(report), 7)
        self.assertTrue(report_path.exists())

if __name__ == "__main__":
    unittest.main()
