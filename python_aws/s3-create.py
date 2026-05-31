import boto3
from botocore.exceptions import ClientError

# INITIALIZE BOTO3 CLIENT 
client = boto3.client('s3')

# CREATE BUCKET FUNCTION
def create_s3_bucket(bucket_name,bucket_region):
    try:
        response = client.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={
                'LocationConstraint': bucket_region
            }
        )
        return response
    except ClientError as e:
        error_code = e.response['Error']['Code']
        if error_code == "BucketAlreadyExists":
            print(f"Bucket {bucket_name} aleady exists, please choose a different name.")

result = create_s3_bucket("networknuts.example.com","ap-south-1")
print(result)