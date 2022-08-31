#  Here we are having methods for CRUD operation
#  -------------------------------------------------------------------------------

from sqlalchemy.orm import Session
import model
import schema
from geopy.geocoders import Nominatim


def get_address_by_address_id(db: Session, address_id: str):
    """
    This method will return single address details based on address_id
    :param db: database session object
    :param address_id: address id only
    :return: data row if exist else None
    """
    return db.query(model.Addresses).filter(model.Addresses.address_id == address_id).first()


def get_address_by_id(db: Session, sl_id: int):
    """
    This method will return single address details based on id
    :param db: database session object
    :param sl_id: serial id of record or Primary Key
    :return: data row if exist else None
    """
    return db.query(model.Addresses).filter(model.Addresses.id == sl_id).first()


def get_address(db: Session, skip: int = 0, limit: int = 100):
    """
    This method will return all address details which are present in database
    :param db: database session object
    :param skip: the number of rows to skip before including them in the result
    :param limit: to specify the maximum number of results to be returned
    :return: all the row from database
    """
    return db.query(model.Addresses).offset(skip).limit(limit).all()


def add_address_details_to_db(db: Session, address: schema.AddressAdd):
    """
    this method will add a new record to database. and perform the commit and refresh operation to db
    :param db: database session object
    :param address: Object of class schema.AddressAdd
    :return: a dictionary object of the record which has inserted
    """
    geolocator = Nominatim(user_agent="MyApp")

    location = geolocator.geocode(address.city)

    mv_details = model.Addresses(
        address_id=address.address_id,
        name=address.name,
        detailAddress=address.detailAddress,
        country=address.country,
        state=address.state,
        city=address.city,
        longitude=location.longitude,
        latitude=location.latitude,
    )
    db.add(mv_details)
    db.commit()
    db.refresh(mv_details)
    return model.Addresses(**address.dict())


def update_address_details(db: Session, sl_id: int, details: schema.UpdateAddress):
    """
    this method will update the database
    :param db: database session object
    :param sl_id: serial id of record or Primary Key
    :param details: Object of class schema.UpdateAddress
    :return: updated address record
    """
    db.query(model.Addresses).filter(model.Addresses.id == sl_id).update(vars(details))
    db.commit()
    return db.query(model.Addresses).filter(model.Addresses.id == sl_id).first()


def delete_address_details_by_id(db: Session, sl_id: int):
    """
    This will delete the record from database based on primary key
    :param db: database session object
    :param sl_id: serial id of record or Primary Key
    :return: None
    """
    try:
        db.query(model.Addresses).filter(model.Addresses.id == sl_id).delete()
        db.commit()
    except Exception as e:
        raise Exception(e)
