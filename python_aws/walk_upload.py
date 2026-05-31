import os
import boto3

def walking(parent_path,bucket_name):
    s3 = boto3.client("s3")
    print(f"Starting directory walk on {parent_path}")
    children = os.listdir(parent_path)
    for child in children:
        child_path = os.path.join(parent_path,child)
        if os.path.isfile(child_path):
            s3.upload_file(child_path,bucket_name,child)
            print(f"{child_path} ---> {bucket_name} --> {child}")
        if os.path.isdir(child_path):
            print(f"Skipping {child_path}. Directory spotted.")

walking("/home/aryan","networknuts.example.com")