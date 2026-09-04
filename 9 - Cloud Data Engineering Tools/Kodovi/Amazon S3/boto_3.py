import boto3
import pandas as pd
from IPython.display import display
# Omogućavaju da pristupiš javnim bucketima bez korisničkog imena i lozinke (dakle, bez naloga).
from botocore import UNSIGNED
from botocore.config import Config 
 
# Create anonymous (unsigned) S3 client
s3 = boto3.client('s3', config=Config(signature_version=UNSIGNED))
 
# (2) Specify the bucket name
bucket_name = 'music-top-charts-preview'
 
# (3) Retrieve the list of objects in the bucket
response = s3.list_objects_v2(Bucket=bucket_name)

# (4) Print the file names (Key = file/object name)
if 'Contents' in response:
    for obj in response['Contents']:
        print(obj['Key'])
else:
    print("The bucket is empty or you don't have access.")


if 'Contents' in response:
    for obj in response['Contents']:
        url = f"https://music-top-charts-preview.s3.eu-north-1.amazonaws.com/{obj['Key']}"
        df = pd.read_csv(url)
        display(df)
else:
    print("The bucket is empty or you don't have access.")