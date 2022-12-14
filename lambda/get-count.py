import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('counting_table')

def lambda_handler(event, context):
    response = table.get_item(Key={
       'record_id':'0'
    })
    
    return response['Item']['record_count']