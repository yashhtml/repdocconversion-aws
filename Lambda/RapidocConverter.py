import json
import boto3
import urllib.parse

s3 = boto3.client('s3')
textract = boto3.client('textract')

OUTPUT_BUCKET = "rapidoc-**-bucket"

def lambda_handler(event, context):

    # Get file info from S3 trigger
    record = event['Records'][0]
    bucket = record['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(record['s3']['object']['key'])

    # Call Textract
    response = textract.detect_document_text(
        Document={
            'S3Object': {
                'Bucket': bucket,
                'Name': key
            }
        }
    )

    # Extract text
    extracted_text = ""
    for block in response['Blocks']:
        if block['BlockType'] == 'LINE':
            extracted_text += block['Text'] + "\n"

    # Save output
    output_key = key.rsplit('.', 1)[0] + ".txt"

    s3.put_object(
        Bucket=OUTPUT_BUCKET,
        Key=output_key,
        Body=extracted_text.encode('utf-8')
    )

    return {
        "statusCode": 200,
        "body": "Document converted successfully"
    }