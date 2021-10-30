"""
This module contains the keep function, and classes that mirror the domain models. 
The keep function is to be used as a decorator for view functions, and is provided with
appropriate response and request models.

The purpose of building this is to act as the first line of defense against the request data,
and the final layer of check for outgoing data in the response.

"""

import functools
from typing import Callable, List, Optional, Set, Type

from flask import abort, after_this_request, jsonify, request
from pydantic import BaseModel, ValidationError, parse_obj_as

from firekeep.models import Room


# Mirrored models from the domain inherit from this class. Sets global config.
class PydanticBase(BaseModel):
    class Config:
        extra = "forbid"


class TenantBaseModel(PydanticBase):
    first_name: str
    last_name: str
    student_id_number: int


class TenantResponse(TenantBaseModel):
    id: int

    class Config:
        extra = "ignore"  # set to avoid conflict with extra fields that the ORM might return


class TenantCreate(TenantBaseModel):
    pass


class RoomBaseModel(PydanticBase):
    room_number: str
    max_capacity: int


class RoomResponse(RoomBaseModel):
    occupants: Set[TenantResponse]

    class Config:
        extra = "ignore"


class RoomCreate(RoomBaseModel):
    occupants: Set[TenantCreate]


def keep(
    response_model: Optional[Type[BaseModel]],
    request_model: Optional[Type[BaseModel]] = None,
) -> Callable:
    def parser(func) -> Callable:
        @functools.wraps(func)
        def parse_with_pydantic_wrapper(*args, **kwargs):
            try:
                if request_model:
                    request_model(**request.json)  # parsing the request data

                @after_this_request
                def parse_response(response):
                    # check if response is a collection
                    if isinstance(response.json, list):
                        response_as_list_validated: List[response_model] = []

                        response_as_list_parsed = parse_obj_as(
                            List[response_model], response.json
                        )
                        for item in response_as_list_parsed:
                            response_as_list_validated.append(item.dict())

                        return jsonify(response_as_list_validated)
                    else:
                        response_validated = response_model(**response.json)
                        return jsonify(response_validated.dict())

                return func(*args, **kwargs)

            except ValidationError as e:
                return abort(400, description=e)

        return parse_with_pydantic_wrapper

    return parser
