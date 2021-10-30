import functools
from typing import Any, Callable, Dict, Optional, Type

from flask import Flask, abort, jsonify, request
from flask.wrappers import Response
from flask_cors import CORS

from firekeep.keep import RoomCreate, RoomResponse, TenantCreate, TenantResponse, keep

app = Flask(__name__)

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


@app.get("/api/tenants")
@keep(response_model=TenantResponse)
def get_tenant_list():

    return jsonify(
        [
            {
                "first_name": "jefford",
                "last_name": "librado",
                "student_id_number": 951,
                "id": 1,
            },
            {
                "first_name": "eds",
                "last_name": "decena",
                "student_id_number": 753,
                "id": 2,
            },
        ]
    )


@app.post("/api/rooms")
@keep(response_model=RoomResponse, request_model=RoomCreate)
def create_room():
    request.json["id"] = 951

    return request.json
