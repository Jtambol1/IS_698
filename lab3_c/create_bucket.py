import boto3

s3 = boto3.client('s3')
bucket_name = 'javed-new-new-bucket'  # must be globally unique

response = s3.create_bucket(
    Bucket=bucket_name
)

print(f'Bucket {bucket_name} created successfully!')
