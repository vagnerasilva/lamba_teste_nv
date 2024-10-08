from src.app import processor


def lambda_handler(event, context):
    response = processor.processor_lambda(event, context)


    return response


print(lambda_handler({}, {}))