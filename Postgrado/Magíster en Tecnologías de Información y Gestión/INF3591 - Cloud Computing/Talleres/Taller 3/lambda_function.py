import boto3
import os
import uuid
from urllib.parse import unquote_plus
from PIL import Image

s3_client = boto3.client('s3')
writable_files_folder = '/tmp/'

def resize_image(image_path, resized_path):
  with Image.open(image_path) as image:
      image.thumbnail(tuple(x / 2 for x in image.size))
      image.save(resized_path)

def lambda_handler(event, context):
  for record in event['Records']:
      origin_bucket = record['s3']['bucket']['name']
      result_bucket = os.environ['BUCKET_NAME']
      key = unquote_plus(record['s3']['object']['key'])
      tmpkey = key.replace('/', '')
      download_path = f'{writable_files_folder}{uuid.uuid4()}{tmpkey}'
      upload_path = f'{writable_files_folder}resized-{tmpkey}'
      s3_client.download_file(origin_bucket, key, download_path)
      resize_image(download_path, upload_path)
      s3_client.upload_file(upload_path, result_bucket, key)