from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():

    return "Malicious Node Running"


@app.route("/prepare")
def fake():

    print("MALICIOUS PREPARE SENT")

    return {
        "txn": "FAKE_TXN"
    }


@app.route("/commit")
def drop():

    print("COMMIT DROPPED")

    return {
        "status": "ignored"
    }


app.run(
    host="0.0.0.0",
    port=5000
)