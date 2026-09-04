import boto3
from botocore.exceptions import ClientError, EndpointConnectionError, NoCredentialsError

# Create S3 client
s3 = boto3.client('s3')
 
# Specify the bucket name
bucket_name = 'music-top-charts'
 
try:
    # Try to retrieve the list of objects in the bucket
    response = s3.list_objects_v2(Bucket=bucket_name)
 
    # Print the file names (Key = file/object name)
    if 'Contents' in response:
        for obj in response['Contents']:
            print(obj['Key'])
    else:
        print("The bucket is empty or you don't have access.")
 
except ClientError as e:
    print(f"ClientError: {e.response['Error']['Message']}")
except EndpointConnectionError:
    print("Network error: Unable to connect to the endpoint.")
except NoCredentialsError:
    print("Credentials are missing or invalid.")
except Exception as e:
    print(f"Unexpected error: {str(e)}")