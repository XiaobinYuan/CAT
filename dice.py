from flask import Flask, request
import json
import random

app = Flask(__name__)

@app.route('/dices', methods=['GET'])
def dices_rolling():
    dice_numbers = int(request.args.get('dice_nubmers'))
    print(dice_numbers)
    results = []
    dice_index = 0
    while dice_index < dice_numbers:
        results.append(random.randint(1, 6))
        dice_index += 1
    return {"results": results}

@app.route('/', methods=['GET'])
def dice_rolling():
    return {"result": random.randint(1, 6)}

app.run()