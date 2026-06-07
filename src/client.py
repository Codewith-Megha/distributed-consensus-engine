import requests
import time

counter = 1

while True:

    txn = {
        "txn": f"TXN_{counter}"
    }

    try:

        response = requests.post(
            "http://node1:5000/transaction",
            json=txn
        )

        print(response.json())

    except Exception as e:

        print(e)

    counter += 1

    time.sleep(3)