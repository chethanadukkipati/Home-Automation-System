import boto3
from botocore.client import Config
ACCESS_KEY_ID= 'AKIAJGJ3FWGDYUAU32RA'
ACCESS_SECRET_KEY='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'
BUCKET_NAME='projectcn1'
data=open('/home/pi/Documents/image9.jpg','rb')
s3=boto3.resource('s3',aws_access_key_id=ACCESS_KEY_ID,
                  aws_secret_access_key=ACCESS_SECRET_KEY,
                  config=Config(signature_version='s3v4')
                 )
s3.Bucket(BUCKET_NAME).put_object(Key='image9.jpg',Body=data)
print("done")
