import abc

from firekeep.models import Room


class AbstractBaseRepository(abc.ABC):
    @abc.abstractmethod
    def get(self, room_number: str):
        raise NotImplementedError

    @abc.abstractmethod
    def assign(self, room: Room):
        raise NotImplementedError


class SQLAlchemyRepository(AbstractBaseRepository):
    def __init__(self, session) -> None:
        self.session = session

    def get(self, room_number: str):
        pass

    def assign(self, room: Room):
        pass
