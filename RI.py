import boto3
import json
from datetime import datetime

client = boto3.client('ec2')
ids = {}
def lambda_handler(event, context):
    response = client.describe_reserved_instances()
    for i in response['ReservedInstances']:
        reserved_id = i['ReservedInstancesId']
        expires = i['End']
        end_date = expires.date()
        ids[reserved_id] = end_date
    for id in ids:
        expiry_date = ids[id]
        todays_date = datetime.now().date()
        date = expiry_date - todays_date
        if date.days == 30:
            c = str(id)
            sns = boto3.client("sns", region_name="us-east-1")
            sns.publish(
              TopicArn="arn:aws:sns:us-east-1:686878367233:public_Bucket",
              Message=json.dumps(c), 
              Subject="Instance will expire in a month"
            )  
