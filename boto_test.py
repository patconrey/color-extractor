import boto3
import random
import string

N = 15
OUTPUT_FILENAME = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(N))

s3 = boto3.resource('s3')
data = open('image-3.jpg', 'rb')
s3.Bucket('color-palette-twitter-bot').put_object(Key=OUTPUT_FILENAME + '.jpg', Body=data)