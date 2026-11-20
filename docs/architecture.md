# System Architecture

## Project
Email Automation & Reminder System

## Overview
This project is a Python-based automation system that
processes scheduled reminders, generates personalized
email messages, supports safe email simulation, and
creates execution reports.

## Architecture Components

### 1. Data Layer
- contacts.csv stores recipient information.
- reminders.csv stores scheduled reminder records.
- data_loader.py loads and validates CSV data.
- Contacts must be active and have email consent.

### 2. Email Generation Layer
- email_template.txt stores the reusable message template.
- email_generator.py personalizes messages using contact
  and reminder information.

### 3. Email Delivery Layer
- email_sender.py handles dry-run simulation and SMTP
  delivery functionality.
- Real email delivery requires explicit configuration.
- Dry-run mode is used by default for safe testing.

### 4. Scheduling Layer
- scheduler.py checks scheduled dates and times.
- Only pending and due reminders are processed.
- Processed reminders have their status updated.

### 5. Logging Layer
- logger_config.py configures application logging.
- Execution events are recorded in logs/automation.log.

### 6. Reporting Layer
- report_generator.py creates CSV execution reports.
- Reports include recipient, subject, status,
      execution time, and processing message.

### 7. Main Application
- main.py integrates all application modules.

## Processing Flow

      1. Load contacts and reminders.
      2. Validate input data.
      3. Filter eligible contacts.
      4. Identify due pending reminders.
      5. Generate personalized messages.
      6. Simulate or send messages.
      7. Update reminder statuses.
      8. Generate execution reports.
      9. Record application logs.

      ## Technology Stack
      - Python
      - Pandas
      - smtplib
      - email.message
      - schedule
      - datetime
      - logging
      - python-dotenv

      ## Safety
      The application uses dry-run mode for testing.
      Real email delivery requires explicit SMTP configuration.
      