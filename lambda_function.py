import json
import base64
import app.s3_service


def lambda_handler(event, context):

    if 'queryStringParameters' not in event or \
            'bucket' not in event['queryStringParameters'] or \
            'key' not in event['queryStringParameters'] or \
            event['queryStringParameters']['bucket'] == '' or \
            event['queryStringParameters']['key'] == '':

        return {
            'statusCode': 500,
            'body': json.dumps('Parametros bucket e key devem ser informados')
        }

    bucket = event['queryStringParameters']['bucket']
    key = event['queryStringParameters']['key']

    content = app.s3_service.execute(bucket=bucket, key=key)

    if content is not None:

        return {
            'headers': {
                'Content-Type': 'text/plan; charset=utf-8'
            },
            'statusCode': 200,
            'body': base64.b64encode(content).decode('utf-8'),
            'isBase64Encoded': True
        }
        # return base64.b64encode(content).decode('utf-8')

    else:

        return {
            'statusCode': 404,
            'body': json.dumps('File not found')
        }

# if __name__ == '__main__':
#     lambda_handler('PyCharm', None)
