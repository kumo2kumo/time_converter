import json
import os
from converter import Converter
from nacl.signing import VerifyKey
from nacl.exceptions import BadSignatureError

APPLICATION_PUBLIC_KEY = os.environ['APPLICATION_PUBLIC_KEY']
verify_key = VerifyKey(bytes.fromhex(APPLICATION_PUBLIC_KEY))
token = os.environ['TOKEN']


def verify(signature: str, timestamp: str, body: str) -> bool:
    try:
        verify_key.verify(f"{timestamp}{body}".encode(), bytes.fromhex(signature))
    except Exception as e:
        print(f"failed to verify request: {e}")
        return False

    return True


def lambda_handler(event: dict, context: dict):
    headers: dict = {k.lower(): v for k, v in event['headers'].items()}
    rawBody: str = event['body']

    # validate request
    signature = headers.get('x-signature-ed25519')
    timestamp = headers.get('x-signature-timestamp')
    # リクエストの署名を検証
    if not verify(signature, timestamp, rawBody):
        return {
            "cookies": [],
            "isBase64Encoded": False,
            "statusCode": 401,
            "headers": {},
            "body": ""
        }

    req: dict = json.loads(rawBody)
    print(req)
    if req['type'] == 1:  # InteractionType.Ping
        return {
            "type": 1  # InteractionResponseType.Pong
        }
    elif req['type'] == 2:  # InteractionType.ApplicationCommand
        # command options list -> dict
        area = req['data']['options'][0]['value']
        time = req['data']['options'][1]['value']

        converter = Converter(area, time)
        converterd_time = converter.convert()

        return {
            'type': 4,
            'data': {
                'content': f'{area}の{time}は\n{converterd_time}',
            }

        }