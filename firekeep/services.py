from typing import Any

from sqlalchemy.orm import Session


def assign_tenant_to_room(
    room_number: str, room_id: int, tenant_id: int, session_object: Session
) -> Any:
    with session_object as session:
        print(room_number)

    return room_number, tenant_id
