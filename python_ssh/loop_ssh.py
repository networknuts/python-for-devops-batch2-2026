from connect_multi import run_ssh_command

f = open("inventory.txt","r")
hosts = f.readlines()
for host in hosts:
    result = run_ssh_command(
        host.strip(),
        "student",
        key_file="/home/aryan/.ssh/id_rsa",
        command="dff -h"
    )
    print(f"HOST: {result['host']}")
    if result['stdout']:
        print("STDOUT\n")
        print(result['stdout']) 
    
    if result['error']:
        print("STDERR\n")
        print(result['error'])
