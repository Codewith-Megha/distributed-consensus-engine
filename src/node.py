import random
import os
from flask import Flask, request, jsonify
from crypto_utils import generate_keys, sign_message
app = Flask(__name__)

NODE_ID = os.getenv("NODE_ID", "1")

private_key, public_key = generate_keys()

ledger = []

leader_id = 1

@app.route("/elect")
def elect():

    global leader_id

    leader_id = random.randint(1,5)

    print(f"New Leader Elected: Node {leader_id}")

    return {
        "leader": leader_id
    }

@app.route("/")
def home():

    return f"Node {NODE_ID} Running"


@app.route("/leader")
def leader():

    return {
        "leader": leader_id
    }


@app.route("/transaction", methods=["POST"])
def transaction():

    data = request.json

    ledger.append(data)

    print(f"Transaction Added: {data}")

    return {
        "status": "success",
        "ledger_size": len(ledger)
    }


@app.route("/prepare")
def prepare():

    print("PAXOS -> PREPARE")

    return {
        "message": "PROMISE"
    }


@app.route("/accept")
def accept():

    print("PAXOS -> ACCEPT")

    return {
        "message": "ACCEPTED"
    }


@app.route("/commit")
def commit():

    print("PAXOS -> COMMIT")

    return {
        "status": "committed"
    }


@app.route("/preprepare")
def preprepare():

    print("PBFT -> PRE-PREPARE")

    return {
        "status": "ok"
    }


@app.route("/preparepbft")
def prepare_pbft():

    print("PBFT -> PREPARE")

    return {
        "status": "ok"
    }


@app.route("/commitpbft")
def commit_pbft():

    print("PBFT -> COMMIT")

    return {
        "status": "ok"
    }


@app.route("/sign")
def sign():

    msg = "PBFT_MESSAGE"

    signature = sign_message(private_key, msg)

    return {
        "signed": True,
        "length": len(signature)
    }


app.run(
    host="0.0.0.0",
    port=5000
)