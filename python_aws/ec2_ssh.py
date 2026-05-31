import boto3
from paramiko.client import SSHClient, AutoAddPolicy

# CONFIGURATION

REGION = "ap-south-1"

TAG_KEY = "environment"
TAG_VALUE = "development"

USERNAME = "ubuntu"

COMMAND = "lsblkk"

# STEP 1: INSTANCE DISCOVERY

def get_instances():
    ec2 = boto3.client("ec2",region_name=REGION)
    response = ec2.describe_instances(
        Filters=[
            {
                "Name": "instance-state-name",
                "Values": ["running"]
            },
            {
                "Name": f"tag:{TAG_KEY}",
                "Values": [TAG_VALUE]
            }
        ]
    )
    instances = []

    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            key_name = instance.get('KeyName')
            public_ip = instance.get('PublicIpAddress')
            private_ip = instance.get('PrivateIpAddress')

            instances.append({
                "instance_id": instance_id,
                "public_ipv4": public_ip,
                "private_ipv4": private_ip,
                "key_name": key_name
            })

    return instances 

# STEP 2: CREATE YOUR SSH KEY
def create_pem_file(key_name):
    pem_file = f"{key_name}.pem"
    return pem_file


# STEP 3: SSH COMMAND EXECUTION
def run_ssh_command(host,username,pem_file,command):
    client = SSHClient()
    client.set_missing_host_key_policy(AutoAddPolicy)
    try:
        print(f"\nConnecting to {host}")
        client.connect(
            hostname=host,
            username=username,
            key_filename=pem_file,
            timeout=10
        )
        stdin, stdout, stderr = client.exec_command(command)
        output = stdout.read().decode()
        error = stderr.read().decode()
        return {
            "host": host,
            "output": output,
            "error": error 
        }
    except Exception as e:
        return {
            "host": host,
            "output": "",
            "error": str(e)
        }
    finally:
        client.close()

# MAIN PROGRAM WHICH COMBINES ABOVE 3 FUNCTIONS

instances = get_instances()

if not instances:
    print("No instances matching given tags")
    exit()

for instance in instances:
    instance_id = instance['instance_id']
    ip_address = instance['public_ipv4']
    key_name = instance['key_name']

    print("="*60)
    print(f"Instance ID: {instance_id}")
    print(f"IP Address: {ip_address}")
    print(f"SSH Key Name: {key_name}")

    pem_file = create_pem_file(key_name)

    result = run_ssh_command(
        host=ip_address,
        username=USERNAME,
        pem_file=pem_file,
        command=COMMAND
    )

    print("\nCommand Output:")
    print(result['output'])

    if result['error']:
        print("\nCommand Error:")
        print(result['error'])
    print("="*60)