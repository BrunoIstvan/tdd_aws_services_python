
def validate_params_by_service(service, params):

    if service == 's3':
        if 'bucket' not in params or 'key' not in params or params['bucket'] == '' or params['key'] == '':
            raise ValueError('Para o serviço s3 é necessário enviar os parâmetros '
                             'bucket e key com seus devidos valores')

        else:
            return params['bucket'], params['key']

    return None
