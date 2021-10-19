# from firekeep import __version__
from firekeep.models import (
    MaximumNumberOfOccupantsReached,
    Room,
    Tenant,
    assign_to_room,
)
import pytest

# def test_version():
# assert __version__ == '0.1.0'


def test_assign_tenant_to_room():
    tenant = Tenant("Neil", "Alino", 20120065)
    room = Room("GF-001", 5)

    assign_to_room(tenant, room)

    assert tenant in room.occupants


def test_raise_max_number_of_occupants_reached_if_cannot_assign():
    tenants = [
        Tenant("Neil", "Alino", 20120065),
        Tenant("Jefford", "Librado", 20120055),
        Tenant("Ed", "Decena", 20120045),
        Tenant("Wins", "Sabellona", 20120035),
    ]

    room = Room("1F-001", 2)

    with pytest.raises(MaximumNumberOfOccupantsReached):
        for tenant in tenants:
            assign_to_room(tenant, room)
