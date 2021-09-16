from app import process

def lambda_handler(event, context):

    return process.execute(event)

