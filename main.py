from pathlib import Path
import sys

from src.scheduler import process_due_reminders
from src.logger_config import setup_logger
from src.report_generator import generate_report

PROJECT_DIR = Path(__file__).resolve().parent

def main():
    logger = setup_logger(PROJECT_DIR / "logs" / "automation.log")
    logger.info("Email Automation & Reminder System started.")
    
    try:
        results = process_due_reminders(PROJECT_DIR, dry_run=True)
        report_path = PROJECT_DIR / "outputs" / "email_report.csv"
        report = generate_report(results, report_path)
        
        simulated = sum(1 for result in results if result["status"] == "Simulated")
        failed = sum(1 for result in results if result["status"] == "Failed")
        
        logger.info("Processing completed.")
        logger.info("Reminders processed: %s", len(results))
        logger.info("Simulated: %s", simulated)
        logger.info("Failed: %s", failed)
        
        print("\nEMAIL AUTOMATION SYSTEM")
        print("=======================")
        print("Reminders processed:", len(results))
        print("Emails simulated:", simulated)
        print("Failures:", failed)
        print("Report saved:", report_path)
        
        print("\nEXECUTION REPORT:")
        if report.empty:
            print("No due reminders found.")
        else:
            print(report.to_string(index=False))
            
    except Exception:
        logger.exception("Application execution failed.")
        raise

if __name__ == "__main__":
    main()
