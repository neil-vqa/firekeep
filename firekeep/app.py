import functools
from typing import Any, Callable, Dict, Optional, Type

from flask import Flask, abort, after_this_request, json, jsonify, request
from flask.wrappers import Response
from flask_cors import CORS
from pydantic import BaseModel, ValidationError

app = Flask(__name__)

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


class RocketEngineBase(BaseModel):
    name: str
    manufacturer: str
    thrust_to_weight_ratio: int


class RocketEngineNew(RocketEngineBase):
    class Config:
        extra = "forbid"


class RocketEngineResponse(RocketEngineBase):
    id: int


def keep(
    response_model: Optional[Type[BaseModel]],
    request_model: Optional[Type[BaseModel]] = None,
) -> Callable:
    def validate(func) -> Callable:
        @functools.wraps(func)
        def validate_with_pydantic_wrapper(*args, **kwargs):
            try:
                if request_model:
                    request_model(**request.json)

                @after_this_request
                def validate_response(response):
                    if isinstance(response.json, list):
                        return response
                    else:
                        response_validated = response_model(**response.json)
                        return jsonify(response_validated.dict())

                return func(*args, **kwargs)

            except ValidationError as e:
                return abort(400, description=e)

        return validate_with_pydantic_wrapper

    return validate


@app.get("/api/rocket-engines")
@keep(response_model=RocketEngineResponse)
def get_rocket_engines():

    return jsonify(
        [
            {
                "name": "RD-180",
                "manufacturer": "NPO Energomash",
                "thrust_to_weight_ratio": 78,
                "id": 2020,
                "country": "Russia",
                "gibberish": 12312312,
            },
            {
                "name": "RD-180",
                "manufacturer": "NPO Energomash",
                "thrust_to_weight_ratio": 78,
                "id": 2020,
                "country": "Russia",
                "gibberish": 12312312,
            },
        ]
    )


@app.post("/api/rocket-engines")
@keep(response_model=RocketEngineResponse, request_model=RocketEngineNew)
def create_rocket_engine():
    request.json["id"] = 951

    return request.json
