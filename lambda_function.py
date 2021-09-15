import json
import base64
import app.s3_service


def lambda_handler(event, context):

    content = app.s3_service.execute(bucket='bicmsystems-s3-transfer-poc',
                                     key='log.txt')

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
