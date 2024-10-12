import os
import requests
from dotenv import load_dotenv
load_dotenv()

request = requests.post(
    'https://api.bfl.ml/v1/flux-pro-1.1',
    headers={
        'accept': 'application/json',
        'x-key': os.environ.get("BFL_API_KEY"),
        'Content-Type': 'application/json',
    },
    json={
        'prompt': 'A cat on its back legs running like a human is holding a big silver fish with its arms. The cat is running away from the shop owner and has a panicked look on his face. The scene is situated in a crowded market.',
        'width': 1024,
        'height': 768,
    },
).json()
print(request)
request_id = request["id"]

import time

while True:
    time.sleep(0.5)
    result = requests.get(
        'https://api.bfl.ml/v1/get_result',
        headers={
            'accept': 'application/json',
            'x-key': os.environ.get("BFL_API_KEY"),
        },
        params={
            'id': request_id,
        },
    ).json()
    if result["status"] == "Ready":
        print(f"Result: {result['result']['sample']}")
        break
    else:
        print(f"Status: {result['status']}")