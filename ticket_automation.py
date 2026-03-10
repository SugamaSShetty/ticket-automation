import pandas as pd
import re
import uuid
from datetime import timedelta
import os
from collections import Counter

if not os.path.exists("output"):
    os.makedirs("output")

df = pd.read_csv("input/tickets.csv")

processed = []
rejected = []

routing = {
    "wifi": "Network",
    "login": "IT Support",
    "software": "Applications",
    "hardware": "Infrastructure",
    "other": "General"
}

priorities = ["low", "medium", "high"]

def valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, str(email))

seen = {}

for index, row in df.iterrows():
    email = str(row["Email"]).lower().strip()
    issue = str(row["Issue Type"]).lower().strip()
    priority = str(row["Priority"]).lower().strip()
    timestamp = pd.to_datetime(row["Timestamp"])

    if not valid_email(email):
        row["Reason"] = "Invalid Email"
        rejected.append(row)
        continue

    if priority not in priorities:
        row["Reason"] = "Invalid Priority"
        rejected.append(row)
        continue

    if issue not in routing:
        row["Reason"] = "Unknown Issue"
        rejected.append(row)
        continue

    key = (email, issue)
    if key in seen:
        if (timestamp - seen[key]).total_seconds() < 86400:
            row["Reason"] = "Duplicate Ticket"
            rejected.append(row)
            continue
    seen[key] = timestamp

    ticket_id = row["Ticket ID"]
    if pd.isna(ticket_id) or ticket_id == "":
        ticket_id = "TCKT-" + str(uuid.uuid4())[:6]

    team = routing[issue]

    if priority == "high":
        sla = timestamp + timedelta(hours=4)
    elif priority == "medium":
        sla = timestamp + timedelta(hours=24)
    else:
        sla = timestamp + timedelta(hours=72)

    row["Ticket ID"] = ticket_id
    row["Assigned Team"] = team
    row["SLA Deadline"] = sla

    processed.append(row)

pd.DataFrame(processed).to_csv("output/processed_tickets.csv", index=False)
pd.DataFrame(rejected).to_csv("output/rejected_tickets.csv", index=False)

summary = {
    "Total Tickets": len(df),
    "Processed": len(processed),
    "Rejected": len(rejected)
}
summary_df = pd.DataFrame(list(summary.items()), columns=["Metric", "Value"])
summary_df.to_csv("output/summary_report.csv", index=False)

team_counts = Counter([row["Assigned Team"] for row in processed])
team_summary_df = pd.DataFrame(list(team_counts.items()), columns=["Team", "Tickets Assigned"])
team_summary_df.to_csv("output/team_summary.csv", index=False)

print("Automation Completed. All files are in the 'output' folder.")