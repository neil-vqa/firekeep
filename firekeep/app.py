from flask import Flask, abort, jsonify, request
from flask.wrappers import Response
from flask_cors import CORS

from firekeep.keep import RoomCreate, RoomResponse, TenantCreate, TenantResponse, keep

app = Flask(__name__)

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


@app.get("/api/tenants")
@keep(response_model=TenantResponse)
def get_tenant_list():

    tenants = [
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

    return jsonify(tenants)


@app.get("/api/tenants/<int:id>")
@keep(response_model=TenantResponse)
def get_tenant(id: int):

    tenant = {
        "first_name": "wins",
        "last_name": "sabellona",
        "student_id_number": 963,
        "id": id,
    }

    return jsonify(tenant)


@app.post("/api/rooms")
@keep(response_model=RoomResponse, request_model=RoomCreate)
def create_room():
    request.json["id"] = 951

    return request.json
