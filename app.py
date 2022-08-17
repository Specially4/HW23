import os

from flask import Flask, request, jsonify
from werkzeug.exceptions import BadRequest

from constants import DATA_DIR
from utils import query

app = Flask(__name__)


@app.route("/perform_query", methods=["POST"])
def perform_query():
    data: dict = request.json
    file_name: str = data['file_name']

    if not os.path.exists(os.path.join(DATA_DIR, file_name)):
        raise BadRequest

    return jsonify(query(data)), 200

    # return app.response_class('', content_type="text/plain")


if __name__ == '__main__':
    app.run()
