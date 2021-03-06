from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from flask_jsonschema_ext.drivers import sqlalchemy

Base = declarative_base()


class Post(Base):
    __tablename__ = 'post'
    post_id = Column(Integer, primary_key=True)
    post_value = Column(String)
    author_id = Column(Integer, ForeignKey('author.author_id'))


class Author(Base):
    __tablename__ = 'author'
    author_id = Column(Integer, primary_key=True)
    author_name = Column(String)

    posts = relationship(Post, backref='author')


def test_sqlalchemy_entity():
    assert sqlalchemy.SqlAlchemyDriver().convert_entity(Post) == \
           {
               'additionalProperties': False,
               'properties': {'post_id': {'type': 'number'},
                              'author_id': {'type': 'number'},
                              'post_value': {'type': 'string'}
                              },
               'type': 'object'
           }


def test_sqlalchemy_recursive():
    assert sqlalchemy.SqlAlchemyDriver().convert_entity_tree(Post) == \
           {
               'type': 'object',
               'additionalProperties': False,
               'properties': {'post_id': {'type': 'number'},
                              'author_id': {'type': 'number'},
                              'post_value': {'type': 'string'},
                              'author': {'additionalProperties': False,
                                         'type': 'object',
                                         'properties': {'author_name': {'type': 'string'},
                                                        'author_id': {'type': 'number'}
                                                        }
                                         }
                              }
           }


def test_sqlalchemy_recursive_inverse():
    assert sqlalchemy.SqlAlchemyDriver().convert_entity_tree(Author) == \
           {

               'type': 'object',
               'additionalProperties': False,
               'properties': {'author_name': {'type': 'string'},
                              'author_id': {'type': 'number'},
                              'posts': {'type': 'array',
                                        'items': {'additionalProperties': False,
                                                  'type': 'object',
                                                  'properties': {'post_id': {'type': 'number'},
                                                                 'author_id': {'type': 'number'},
                                                                 'post_value': {'type': 'string'}
                                                                 }
                                                  }
                                        },
                              }
           }
