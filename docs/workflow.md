# System Workflow

## Project
Email Automation & Reminder System

## Overview
The system processes scheduled reminders using contact
data, reusable email templates, and Python automation.

## Execution Workflow

### Step 1: Start the Application
The main.py file starts the application and initializes
the logger.

### Step 2: Load Input Data
The data_loader.py module loads:
- contacts.csv
- reminders.csv

### Step 3: Filter Eligible Contacts
Only contacts meeting both conditions are eligible:
- Status is Active.
- Email consent (email_opt_in) is Yes.

### Step 4: Check Scheduled Reminders
The scheduler.py module checks each reminder:
- Its status must be Pending.
- Its scheduled date and time must be due.

Future reminders and previously processed reminders
are skipped.

### Step 5: Generate Personalized Emails
The email_generator.py module uses the email template
and contact/reminder details to generate personalized
messages.

### Step 6: Process Email Delivery
The email_sender.py module handles email processing.

By default, the application uses dry-run mode.
This simulates email delivery without sending actual
emails.

### Step 7: Update Reminder Status
After successful simulation, the reminder status is
updated to Simulated.

If processing fails, its status is updated to Failed.

### Step 8: Generate Execution Report
The report_generator.py module creates:

outputs/email_report.csv

The report contains:
- Reminder ID
- Contact ID
- Recipient
- Subject
- Status
- Execution time
- Processing message

### Step 9: Record Logs
Application events and processing information are
recorded in:

logs/automation.log

## Duplicate Processing Prevention
The scheduler processes only reminders with Pending
status. Once a reminder is processed, its status changes
to Simulated or Failed, so it is skipped on subsequent
runs.

## Final Demonstration
The project was tested using seven sample reminders.

Results:
- Total reminders processed: 7
- Emails simulated: 7
- Failures: 0
- Actual emails sent: 0

## Important Safety Note
All demonstration emails use dry-run mode.
No real emails are sent during the project demonstration.
