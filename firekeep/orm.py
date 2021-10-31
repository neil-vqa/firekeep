from sqlalchemy import Column, Table
from sqlalchemy.orm import registry, relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String

from firekeep.models import Room, Tenant

mapper_registry = registry()

room_table = Table(
    "room",
    mapper_registry.metadata,
    Column("id", Integer, primary_key=True),
    Column("room_number", String(8)),
    Column("max_capacity", Integer),
)

tenant_table = Table(
    "tenant",
    mapper_registry.metadata,
    Column("id", Integer, primary_key=True),
    Column("first_name", String(20)),
    Column("last_name", String(20)),
    Column("student_id_number", Integer),
    Column("room_id", Integer, ForeignKey("room.id")),
)

mapper_registry.map_iteratively(Room, room_table)
mapper_registry.map_iteratively(
    Room, room_table, properties={"occupants": relationship(Tenant, backref="room")}
)
mapper_registry.map_iteratively(Tenant, tenant_table)
