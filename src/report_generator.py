import pandas as pd
from pathlib import Path

def generate_report(results, output_path):
    """Save email automation results as a CSV report."""
    columns = [
        "reminder_id",
        "contact_id",
        "recipient",
        "subject",
        "status",
        "execution_time",
        "message"
    ]
    report = pd.DataFrame(results, columns=columns)
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    report.to_csv(output_path, index=False)
    return report
