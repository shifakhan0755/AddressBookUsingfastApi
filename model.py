# A data model in a database should be relational which means it is described by tables.
# The data describes how the data is stored and organized.
# A data model may belong to one or more schemas, usually, it just belongs to one schema
#  --------------------------------------------------------------------------------------------
from sqlalchemy import Boolean, Column, Integer, String, Float
from db_handler import Base


class Addresses(Base):
    """
    This is a model class. which is having the address table structure with all the constraint
    """
    __tablename__ = "address"
    
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    address_id = Column(String, unique=True, index=True, nullable=False)
    name = Column(String(100), index=True, nullable=False)
    detailAddress = Column(String(255), index=True, nullable=False)
    country = Column(String(100), index=True, nullable=False)
    state = Column(String(100), index=True, nullable=False)
    city = Column(String(100), index=True, nullable=False)
    longitude = Column(Float)
    latitude = Column(Float)

