import io
from unittest import TestCase

import boto3
from botocore.response import StreamingBody
from botocore.stub import Stubber

from app.s3_service import execute


def get_response(content_file):

    return {
        'ContentLength': 500,
        'Body': StreamingBody(
            raw_stream=io.BytesIO(content_file),
            content_length=len(content_file)
        )
    }


class TestS3Service(TestCase):

    def test_execute(self):

        s3_client = boto3.client('s3')
        assert s3_client is not None

        # prepara um stubber
        with Stubber(s3_client) as stubber:
            # simula um conteudo qualquer
            content_file = b'sfsd-sdfgfd dgd fgdf-g dgdfgdfgd-d gdfgdfgd'
            bucket_test = 'bucket-test'
            key_test = 'arquivo-test.txt'
            # recupera a resposta esperada da execucao do metodo s3_client.get_object()
            response = get_response(content_file)
            # esses sao os parametros enviados ao metodo s3_client.get_object()
            expected_params = {'Bucket': bucket_test, 'Key': key_test}
            stubber.add_response('get_object', response, expected_params)
            stubber.activate()
            # recebe a resposta do metodo contendo o conteudo e o tamanho do arquivo
            service_response, content_length = execute(s3_client=s3_client, bucket=bucket_test, key=key_test)
            assert service_response == content_file
            assert content_length == 500
