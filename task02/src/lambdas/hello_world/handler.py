from commons.log_helper import get_logger
from commons.abstract_lambda import AbstractLambda

import boto3

_LOG = get_logger('HelloWorld-handler')


class HelloWorld(AbstractLambda):

    def validate_request(self, event) -> dict:
        pass
        
    def handle_request(self, event, context):
        """
        Explain incoming event here
        """
        # todo implement business logic
        message = 'Hello {} {}!'.format(event['first_name'], event['last_name'])
        return {
            'message' : message
        }


        # Get the Http Method from API Request
        http_method = event['requestContext']['http']['method']

        # Get the Path details from API Request
        path = event['requestContext']['http']['path']

        if http_method == "GET" &&  path == "/hello":
            _LOG.info('Handling Customer API - Get request')

            return {
                'statusCode': 200,
                'message' : 'Hello from Lambda'
            }

        else:
            message = 'Bad request syntax or unsupported method. Request path: {}. HTTP method: {}'.format(path, http_method)
            return {
                'statusCode': 400,
                'message' : message
            }

HANDLER = HelloWorld()


def lambda_handler(event, context):
    return HANDLER.lambda_handler(event=event, context=context)
