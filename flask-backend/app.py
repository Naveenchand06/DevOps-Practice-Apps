from flask import Flask, jsonify
import random
import string

app = Flask(__name__)


@app.route('/healthz', methods=['GET'])
def health_check():
    return jsonify(status='ok'), 200


@app.route('/data1', methods=['GET'])
def get_data1():
    # Generate a random JSON structure
    data = {
        'id': ''.join(random.choices(string.ascii_lowercase + string.digits, k=8)),
        'value': random.randint(1, 100),
        'tags': random.sample(['alpha', 'beta', 'gamma', 'delta', 'epsilon'], k=3)
    }
    return jsonify(data)


@app.route('/data2', methods=['GET'])
def get_data2():
    # Generate another random JSON structure
    items = []
    for _ in range(random.randint(2, 5)):
        items.append({
            'name': ''.join(random.choices(string.ascii_lowercase, k=5)),
            'score': round(random.random() * 10, 2)
        })
    response = {
        'count': len(items),
        'items': items
    }
    return jsonify(response)


if __name__ == '__main__':
    # Listen on all interfaces to work inside Docker
    app.run(host='0.0.0.0', port=5000)
