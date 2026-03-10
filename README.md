Internal IT Support Ticket Automation

Project Overview : -

In this project I tried to automate the IT support ticket process. In universities many students and staff raise issues like wifi not working, login problem, software install issue etc. Mostly these tickets are handled manually by IT team and sometimes it takes more time and also duplicate tickets may come.
So I thought to create a small automation using Python which can read ticket data and process it automatically.
What I Did in This Project
First I created a sample CSV file which contains ticket details. The fields I added are Ticket ID, Name, Email, Issue Type, Priority, Description and Timestamp.
After that I created a Python script and used pandas library to read the CSV file.
Then I added some validation checks.
First I checked the email format using regular expression. If email is not correct then the ticket is rejected.
Next I checked the priority value. Only Low, Medium and High priority tickets are accepted. If some other value is there then it will be rejected.
Then I converted some text fields like email, issue type and priority to lowercase so that data becomes clean.
I also added a logic for duplicate ticket checking. If same user raises same issue within 24 hours then it is considered as duplicate ticket and it will be rejected.
If the ticket id is missing, the system automatically generates a new ticket id.


Ticket Routing :-

After validation the ticket is assigned to the correct team based on issue type.
wifi → Network team
login → IT Support team
software → Applications team
hardware → Infrastructure team
other → General support team

SLA Calculation :-
Then I added SLA calculation based on ticket priority.
High priority → 4 hours
Medium priority → 24 hours
Low priority → 72 hours
The script calculates SLA deadline using timestamp.

Output Files:-
After running the script three output files are generated.
processed_tickets.csv
This file contains all valid tickets with assigned team and SLA deadline.
rejected_tickets.csv
This file contains rejected tickets with reason like invalid email, duplicate ticket etc.
summary_report.csv
This file shows summary like total tickets, processed tickets and rejected tickets.

Future Scope :-
This project is a basic automation. In future it can be improved more. For example tickets can come from a web form or helpdesk portal instead of CSV file.
Also we can connect it with database and email notifications so that support team will get alert when new ticket comes.

Conclusion:-
By doing this project I understood how automation can help in ticket management. Instead of doing everything manually the script can validate data, remove duplicates, assign tickets to correct team and generate reports automatically.
