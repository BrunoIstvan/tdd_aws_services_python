import boto3


def execute(bucket, key):

    client = boto3.client('s3')

    result = client.get_object(Bucket=bucket, Key=key)

    if result is None:
        raise Exception('Arquivo não encontrado')

    if result['ContentLength'] > 0:

        file = result['Body']
        file = file.read()  # .decode('utf8')

        print(file)

        return file

    return None
