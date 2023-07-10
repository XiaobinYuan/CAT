from flask import Flask, request, Response
from prometheus_client import Counter

import prometheus_client
import random

app = Flask(__name__)
rolling_times = Counter('dice_rolling_times', 'Counter of dice rolling requests' )

@app.route('/dices', methods=['GET'])
def dices_rolling():
    dice_numbers = int(request.args.get('dice_nubmers'))
    print(dice_numbers)
    results = []
    dice_index = 0
    while dice_index < dice_numbers:
        results.append(random.randint(1, 6))
        dice_index += 1
    rolling_times.inc()
    return {"results": results}

@app.route('/', methods=['GET'])
def dice_rolling():
    rolling_times.inc()
    return {"result": random.randint(1, 6)}

@app.route('/metrics')
def metrics():
    return Response(prometheus_client.generate_latest(rolling_times), mimetype="text/plain")

app.run(host='0.0.0.0')