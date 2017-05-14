"""
yourCMDB2 model cmdbobject module

This module is part of the yourCMDB2 model and defines the CMDB Object

:license: MIT, see LICENSE for more details
:copyright: (c) 2017 by Michael Batz, see AUTHORS for more details
"""

from sqlalchemy import ForeignKey, ForeignKeyConstraint, Column, String, Integer, DateTime
from sqlalchemy.types import Boolean
from sqlalchemy.orm import relationship
from .ormbase import Base

class CmdbObject(Base):

    __tablename__ = "object"

    object_id = Column(Integer, primary_key=True)
    object_type = Column(Integer, ForeignKey("objecttype.objecttype_id"))
    object_state = Column(String)

    related_fields = relationship("CmdbObjectField", cascade="all, delete-orphan")
    related_tags = relationship("CmdbObjectTagRelation", cascade="all, delete-orphan")
    related_logs = relationship("CmdbObjectLogEntry", cascade="all, delete-orphan")


class CmdbObjectField(Base):

    __tablename__ = "object_field"
    __table_args__ = (ForeignKeyConstraint(["field_objecttype", "field_name"],
                                           ["objecttype_field.field_objecttype", "objecttype_field.field_name"]), {})

    field_object = Column(Integer, ForeignKey("object.object_id"), primary_key=True)
    field_objecttype = Column(Integer)
    field_name = Column(String, primary_key=True)
    field_value = Column(String)

    related_object = relationship("CmdbObject")
    related_objecttypefield = relationship("CmdbObjectTypeField")


class CmdbObjectTag(Base):

    __tablename__ = "objecttag"

    tag_id = Column(Integer, primary_key=True)
    tag_label = Column(String)
    tag_color = Column(String)
    tag_icon = Column(String)


class CmdbObjectTagRelation(Base):

    __tablename__ = "objecttag_relation"

    tag_id = Column(Integer, ForeignKey("objecttag.tag_id"), primary_key=True)
    object_id = Column(Integer, ForeignKey("object.object_id"), primary_key=True)


class CmdbObjectLogEntry(Base):

    __tablename__ = "objectlog"

    log_id = Column(Integer, primary_key=True)
    log_object = Column(Integer, ForeignKey("object.object_id"))
    log_time = Column(DateTime)
    log_user = Column(String)
    log_action = Column(String)
    log_description = Column(String)

    related_object = relationship("CmdbObject")
