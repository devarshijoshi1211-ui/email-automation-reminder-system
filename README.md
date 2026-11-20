# Email Automation & Reminder System

A Python-based automation project that processes scheduled reminders, generates personalized email messages, simulates email delivery, and creates execution reports.

## Project Overview

The Email Automation & Reminder System helps automate routine reminder workflows for departments such as HR, Sales, Finance, Operations, and Training.

It uses CSV files to manage contacts and reminders, reusable email templates to personalize messages, and Python modules to process due reminders.

Safety: The project uses dry-run mode by default. No actual emails are sent during the demonstration.

## Features

- Load contact and reminder data from CSV files.
- Validate required input columns.
- Filter inactive and non-consenting contacts.
- Identify pending reminders that are due.
- Generate personalized email messages.
- Simulate email delivery safely.
- Support configurable SMTP delivery functionality.
- Prevent previously processed reminders from being processed again in normal repeated runs.
- Record application logs.
- Generate CSV execution reports.
- Include automated unit tests.

## Technology Stack

- Python
- Pandas
- smtplib
- email.message
- datetime
- logging
- python-dotenv

### Project Structure

Email-Automation-Reminder-System/
├── data/
│   ├── contacts.csv
│   ├── reminders.csv
│   └── reminders_backup.csv
├── templates/
│   └── email_template.txt
├── src/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── email_generator.py
│   ├── email_sender.py
│   ├── scheduler.py
│   ├── report_generator.py
│   └── logger_config.py
├── outputs/
│   └── email_report.csv
├── images/
│   ├── Email report.png
│   ├── Execution.png
│   ├── Project structure.png
│   └── System architecture.png
├── docs/
│   ├── architecture.md
│   └── workflow.md
├── tests/
│   └── test_project.py
├── main.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md

## How It Works

1. Load contacts and reminder records.
2. Filter contacts based on active status and email consent.
3. Identify reminders that are pending and due.
4. Generate personalized messages using the email template.
5. Simulate email processing.
6. Update reminder statuses.
7. Generate an execution report.
8. Record events in the application log.

## Installation

Install the required dependencies:

pip install -r requirements.txt

## Run the Application

python main.py

The application currently runs in dry-run mode by default.

In Google Colab, the project can also be executed using the notebook developed for the project.

## Testing

Run the automated test suite:

python -m unittest discover -s tests -v

The project includes six tests covering data loading, consent filtering, email generation, scheduler processing, duplicate prevention, and report generation.

## Sample Demonstration Results

The final demonstration processed seven sample reminders successfully.

- Reminders processed: 7
- Emails simulated: 7
- Failures: 0
- Actual emails sent: 0

All seven sample reminders were successfully simulated.

## Screenshots

### Project Structure

"Project Structure" (images/Project%20structure.png)

### Application Execution

"Application Execution" (images/Execution.png)

### Email Execution Report

"Email Report" (images/Email%20report.png)

### System Architecture

"System Architecture" (images/System%20architecture.png)

## Limitations

1. The application checks for due reminders when it is run; it is not currently a continuously running background service.
2. The execution report is regenerated on each run.
3. The demonstration uses simulated email delivery.
4. Reliable production email delivery would require additional monitoring, retry handling, and stronger delivery-state management.

Real email delivery requires explicit configuration and appropriate recipient consent.

## Future Improvements

1. Add a Streamlit dashboard.
2. Add a continuously running scheduler.
3. Add email delivery analytics.
4. Expand automated test coverage.
5. Add more advanced retry and failure handling.
6. Add database integration.

## GitHub Repository

"Email Automation & Reminder System" (https://github.com/devarshijoshi1211-ui/email-automation-reminder-system)

## Author

Devarshi Joshi
