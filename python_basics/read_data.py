file_path = "/etc/hosts"

f = open(file_path,"r")

for line in f.readlines():
    print(line.strip())
    
f.close()