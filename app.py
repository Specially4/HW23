import os
from typing import Dict, Tuple, Any, Optional, Union

from flask import Flask, request, jsonify, Response
from werkzeug.exceptions import BadRequest

from constants import DATA_DIR
from utils import query

app = Flask(__name__)


@app.route("/perform_query", methods=["POST"])
def perform_query() -> Tuple[Response, int]:
    try:
        data: Dict[str, str] = request.json
        file_name = data['file_name']
    except KeyError:
        raise BadRequest

    if not os.path.exists(os.path.join(DATA_DIR, file_name)):
        raise BadRequest

    return app.response_class(query(data), content_type='text/plain'), 200


if __name__ == '__main__':
    app.run()
