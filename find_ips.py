import re 

raw_ip_logfile = input("Enter the raw file containing IP data: ")

f = open(raw_ip_logfile,"r")
ip_logdata = f.read()
f.close()

matches = re.findall(r"\d+\.\d+\.\d+\.\d+",ip_logdata)
print(matches)