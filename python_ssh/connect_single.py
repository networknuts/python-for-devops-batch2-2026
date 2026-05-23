from paramiko.client import SSHClient
from paramiko.client import AutoAddPolicy

server_address = "example1.networknuts.lab"
server_user = "student"
server_password = "redhat"
server_command = "uptime"

client = SSHClient()
client.set_missing_host_key_policy(AutoAddPolicy)
client.connect(server_address,username=server_user,password=server_password)
stdin, stdout, stderr = client.exec_command(server_command)
print(f"{server_address}\nOUTPUT:\n")
print(stdout.read().decode())
client.close()

print("Connection closed successfully!")