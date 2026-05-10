import re

raw_email_file = input("Enter file path containing mail logs: ")

f = open(raw_email_file,"r")
email_logs = f.read()
f.close()

email_matches = re.findall(r"\w+@\w+\.\w+",email_logs)
print(email_matches)