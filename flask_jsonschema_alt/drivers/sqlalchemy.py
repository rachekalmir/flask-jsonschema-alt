from sqlalchemy import String, Integer
from sqlalchemy.orm.attributes import InstrumentedAttribute


def convert_entity(entity):
    print(entity)


def convert_field(field: InstrumentedAttribute):
    pass
