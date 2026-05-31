import boto3

BUCKET_NAME = "networknuts.example.com"

def upload_to_s3(file_path,bucket_name,file_name):
    s3 = boto3.client("s3")
    try:
        s3.upload_file(file_path,bucket_name,file_name)
        print(f"{file_path} -----> {bucket_name}")
    except Exception as e:
        print(f"Error: {e}")

upload_to_s3("/etc/hosts",BUCKET_NAME,"hosts")