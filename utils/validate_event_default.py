def validate_event(event):

    if 'queryStringParameters' not in event:
        raise AttributeError('O evento informado não contém os parâmetros necessários')

    if 'service' not in event['queryStringParameters']:
        raise AttributeError('O evento informado não contém o parâmetro service')

    return event['queryStringParameters']['service']
