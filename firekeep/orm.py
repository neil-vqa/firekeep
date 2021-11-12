from sqlalchemy import Column, MetaData, Table
from sqlalchemy.orm import registry, relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String

from firekeep.models import Room, Tenant

mapper_registry = registry()
metadata_obj = MetaData()

room_table = Table(
    "room",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("room_number", String(8)),
    Column("max_capacity", Integer),
)

tenant_table = Table(
    "tenant",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("first_name", String(20)),
    Column("last_name", String(20)),
    Column("student_id_number", Integer),
    Column("room_id", Integer, ForeignKey("room.id")),
)


def run_mappers():
    mapper_registry.map_imperatively(
        Room, room_table, properties={"occupants": relationship(Tenant, backref="room")}
    )
    mapper_registry.map_imperatively(Tenant, tenant_table)
