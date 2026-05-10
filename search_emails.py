import re 

f = open("/home/aryan/python-may3-2026/python-for-devops/email-list.txt","r")
email_data = f.read()
f.close()

# FIRST EXAMPLE - BOBBY AND ROBBY
#result = re.search(r"[r,b]obb[i,y]",email_data)

# SECOND EXAMPLE - CHR??
#result = re.search(r"chr[a-z][a-z]",email_data)
#print(result)

# THIRD EXAMPLE - ARTxxxxxxx
#result = re.search(r"art[a-z]+",email_data)
#print(result)

# EMAIL ADDRESS EXAMPLE - CLASSIC APPROACH
#result = re.search(r"[a-zA-Z0-9_]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+",email_data)
#print(result)

# EMAIL ADDRESS EXAMPLE - MODERN APPROACH
#result = re.search(r"\w+@\w+\.\w+",email_data)
#print(result)

# GET ALL MATCHES
matches = re.findall(r"\w+@\w+\.\w+",email_data)
print(matches)