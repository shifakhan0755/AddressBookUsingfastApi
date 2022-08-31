# A schema is a collection of database objects that are logically grouped together.
# These can be anything, tables, views, stored procedure etc.
# Schemas are typically used to logically group objects in a database.
#  ---------------------------------------------------------------------------------
from typing import Optional
from pydantic import BaseModel


class AddressBase(BaseModel):
    name: str
    detailAddress: str
    country: str
    state: str
    city: str
    longitude: float
    latitude: float


class AddressAdd(AddressBase):
    address_id: str
    
    # Behaviour of pydantic can be controlled via the Config class on a model
    # to support models that map to ORM objects. Config property orm_mode must be set to True
    class Config:
        orm_mode = True


class Address(AddressAdd):
    id: int

    # Behaviour of pydantic can be controlled via the Config class on a model
    # to support models that map to ORM objects. Config property orm_mode must be set to True
    class Config:
        orm_mode = True


class UpdateAddress(BaseModel):
    # Optional[str] is just a shorthand or alias for Union[str, None].
    # It exists mostly as a convenience to help function signatures look a little cleaner.
    name: Optional[str] = None
    city:Optional[str] = None

    # Behaviour of pydantic can be controlled via the Config class on a model
    # to support models that map to ORM objects. Config property orm_mode must be set to True
    class Config:
        orm_mode = True
