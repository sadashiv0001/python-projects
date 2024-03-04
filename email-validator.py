import re

def validate_email(email):
    pattern = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w+$')
    return bool(pattern.match(email))

# List of emails
emails = ["email1@example.com", "email2@@invalid", "email3@example.com", "email4@invalid"]

for email in emails:
    if validate_email(email):
        print(f"The email '{email}' is valid.")
    else:
        print(f"The email '{email}' is not valid.")
