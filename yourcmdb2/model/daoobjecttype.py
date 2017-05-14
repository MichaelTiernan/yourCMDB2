"""
yourCMDB2 model cmdbobjecttype module

This module is part of the yourCMDB2 model and defines the CMDB Object Types

:license: MIT, see LICENSE for more details
:copyright: (c) 2017 by Michael Batz, see AUTHORS for more details
"""

from sqlalchemy import ForeignKey, ForeignKeyConstraint, Column, String, Integer
from sqlalchemy.types import Boolean
from sqlalchemy.orm import relationship
from .ormbase import Base

class CmdbObjectType(Base):

    __tablename__ = "objecttype"

    objecttype_id = Column(Integer, primary_key=True)
    objecttype_summarystring = Column(String)
    objecttype_label = Column(String)
    objecttype_comment = Column(String)

    related_fields = relationship("CmdbObjectTypeField", cascade="all, delete-orphan")
    related_links = relationship("CmdbObjectTypeLink", cascade="all, delete-orphan")
    related_objects = relationship("CmdbObject", cascade="all, delete-orphan")


class CmdbObjectTypeField(Base):

    __tablename__ = "objecttype_field"

    field_objecttype = Column(Integer, ForeignKey("objecttype.objecttype_id"), primary_key=True)
    field_name = Column(String, primary_key=True)
    field_group = Column(String)
    field_order = Column(Integer)
    field_label = Column(String)
    field_type = Column(String)
    field_summary = Column(Boolean)
    field_constraint = Column(String)

    related_objecttype = relationship("CmdbObjectType")
    related_objectfields = relationship("CmdbObjectField", cascade="all, delete-orphan") 


class CmdbObjectTypeLink(Base):

    __tablename__ = "objecttype_link"

    link_id = Column(Integer, primary_key=True)
    link_objecttype = Column(Integer, ForeignKey("objecttype.objecttype_id"), primary_key=True)
    link_order = Column(Integer)
    link_label = Column(String)
    link_url = Column(String)

    related_objecttype = relationship("CmdbObjectType")
