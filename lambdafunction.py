import json
#import os
#test4

def lambda_handler(event, context):
    print('My first aws lambda function with python!')
    return {
        'statusCode': 200,
        'body': json.dumps('Hellow from lambda')
    }
