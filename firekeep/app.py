import functools
from typing import Any, Callable, Dict, Optional, Type

from flask import Flask, abort, jsonify, request
from flask.wrappers import Response
from flask_cors import CORS
from pydantic import BaseModel, ValidationError

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


def keep(
    response_model: Optional[Type[BaseModel]],
    request_model: Optional[Type[BaseModel]] = None,
) -> Callable:
    def validate(func) -> Callable:
        @functools.wraps(func)
        def validate_with_pydantic_wrapper(*args, **kwargs):
            request_data = request.json
            try:
                if request_model:
                    request_model(**request_data)
            except ValidationError as e:
                return abort(400, description=e)
            else:
                response_data = func(*args, **kwargs)
                response_validated = response_model(**response_data)
                return jsonify(response_validated.dict())

        return validate_with_pydantic_wrapper

    return validate


@app.get("/api/rocket-engines")
@keep(response_model=RocketEngineResponse)
def get_rocket_engines():
    return {
        "name": "RD-180",
        "manufacturer": "NPO Energomash",
        "thrust_to_weight_ratio": 78,
        "id": 2020,
        "country": "Russia",
    }


@app.post("/api/rocket-engines")
@keep(response_model=RocketEngineResponse, request_model=RocketEngineCreate)
def create_rocket_engine():
    return {
        "name": "raptor",
        "manufacturer": "spacex",
        "thrust_to_weight_ratio": 107,
        "id": 2021,
        "country": "USA",
    }
