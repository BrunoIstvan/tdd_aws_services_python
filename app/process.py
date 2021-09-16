import base64
import json

from app.s3_service import execute as s3_execute, get_s3_client
from utils.validate_event_default import validate_event
from utils.validate_params_by_service_type import validate_params_by_service
from utils.validate_service import validate_service


def execute(event):

    try:

        # valida se o evento veio preenchido
        service = validate_event(event)

        # valida se o parametro service foi informado e se é um service tratado por esse processamento
        validate_service(service)

        # valida os parametros por tipo de service
        params = validate_params_by_service(service, event['queryStringParameters'])

        return execute_by_service_type(service, params)

    except AttributeError as ae:
        return {'statusCode': 500, 'body': json.dumps(ae)}

    except TypeError as te:
        return {'statusCode': 500, 'body': json.dumps(te)}

    except ValueError as ve:
        return {'statusCode': 500, 'body': json.dumps(ve)}


def execute_by_service_type(service, params):

    if service == 's3':

        bucket = params[0]
        key = params[1]

        s3_client = get_s3_client()
        content, _ = s3_execute(s3_client=s3_client, bucket=bucket, key=key)

        if content is not None:

            return {
                'headers': {
                    'Content-Type': 'text/plan; charset=utf-8'
                },
                'statusCode': 200,
                'body': base64.b64encode(content).decode('utf-8'),
                'isBase64Encoded': True
            }

        else:

            return {
                'statusCode': 404,
                'body': json.dumps('File not found')
            }

