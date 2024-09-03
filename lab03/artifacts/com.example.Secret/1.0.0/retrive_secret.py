import json
import sys
import traceback
import awsiot.greengrasscoreipc
from awsiot.greengrasscoreipc.model import (
    GetSecretValueRequest
)

TIMEOUT = 10

if len(sys.argv) == 1:
    print('Set SecretArn in the component configuration.', file=sys.stdout)
    exit(1)

secret_id = sys.argv[1]

try:
    ipc_client = awsiot.greengrasscoreipc.connect()

    request = GetSecretValueRequest()
    request.secret_id = secret_id
    operation = ipc_client.new_get_secret_value()
    operation.activate(request)
    future_response = operation.get_response()

    response = future_response.result(TIMEOUT)
    secret_json = json.loads(response.secret_value.secret_string)
    print('Secret value: ' + str(secret_json))
    
except Exception:
    print('Error.', file=sys.stderr)
