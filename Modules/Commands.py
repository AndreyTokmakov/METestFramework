import json
from typing import Dict

if __name__ == '__main__':
    message: Dict = {
        "action": "markets",
        "pair": "BTC/USDT",
        "data": [
            {"marketId": 111222333444, "marketCode": "BTC-USD"}
        ]
    }

    payload: str = json.dumps(message, indent=3)
    print(payload)
