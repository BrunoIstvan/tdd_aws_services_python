def validate_service(service):

    if service not in ['s3', 'sqs', 'dynamodb']:
        raise TypeError('O evento informado não é tratado por esse processo')

    return True
