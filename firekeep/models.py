class MaximumNumberOfOccupantsReached(Exception):
    pass


class Tenant:
    def __init__(self, first_name: str, last_name: str, student_id_number: int) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.student_id_number = student_id_number

    @property
    def full_name(self) -> str:
        return self.first_name + self.last_name


class Room:
    def __init__(self, room_number: str, max_capacity: int) -> None:
        self.room_number = room_number
        self.max_capacity = max_capacity
        self.occupants = set()

    @property
    def number_of_occupants(self) -> int:
        return len(self.occupants)

    def add_occupant(self, occupant: Tenant):
        if self.can_add_more_occupants:
            self.occupants.add(occupant)
        else:
            raise MaximumNumberOfOccupantsReached

    @property
    def can_add_more_occupants(self) -> bool:
        return self.number_of_occupants < self.max_capacity


def assign_to_room(tenant: Tenant, room: Room):
    try:
        room.add_occupant(tenant)
    except MaximumNumberOfOccupantsReached:
        raise MaximumNumberOfOccupantsReached(
            f"Can no longer add {tenant.full_name} to Room {room.room_number}."
        )
