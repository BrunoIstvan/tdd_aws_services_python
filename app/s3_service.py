import boto3


def get_s3_client():
    return boto3.client('s3')


def execute(s3_client, bucket, key):

    # executa o metodo que recupera os dados de um arquivo
    result = s3_client.get_object(Bucket=bucket, Key=key)

    if result is None:
        raise Exception('Arquivo não encontrado')

    # retorna o conteudo e o tamanho do arquivo
    return result['Body'].read(), result['ContentLength']
