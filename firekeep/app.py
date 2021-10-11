import functools
from typing import Any, Dict

from flask import Flask, jsonify, request
from flask.wrappers import Response
from flask_cors import CORS
from pydantic import BaseModel
from pydantic.types import Json

app = Flask(__name__)

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


class RocketEngineBase(BaseModel):
    name: str
    manufacturer: str
    thrust_to_weight_ratio: int


class RocketEngineCreate(RocketEngineBase):
    pass


class RocketEngineResponse(RocketEngineBase):
    id: int


def response_content(content: Any) -> Response:
    return jsonify({"content": content})


@app.route("/api/rocket-engines")
# @firekeep(request_model="", response_model="")
def home():
    return
