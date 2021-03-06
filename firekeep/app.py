from flask import Flask, jsonify, request
from flask_cors import CORS

from firekeep import orm, services
from firekeep.db_session import Session
from firekeep.keep import RoomCreate, RoomResponse, TenantCreate, TenantResponse, keep

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
orm.run_mappers()


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


@app.post("/api/assign")
def assign_tenant():
    try:
        msg = services.assign_tenant_to_room(
            request.json["room_number"],
            request.json["room_id"],
            request.json["tenant_id"],
            Session(),
        )
        return jsonify(msg)
    except Exception:
        raise
