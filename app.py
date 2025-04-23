from flask import Flask, jsonify
from pnl import get_pnl

app = Flask(__name__)

@app.route('/v1/pnl/<string:strategy_id>', methods=['GET'])
def pnl_endpoint(strategy_id):
    """
    HTTP GET /v1/pnl/{strategy_id}
    """
    result = get_pnl(strategy_id)
    return jsonify(result), 200

if __name__ == '__main__':
    # for production you’d use gunicorn/uwsgi, but for local testing:
    app.run(host='0.0.0.0', port=5000, debug=True)