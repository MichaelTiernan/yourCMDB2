"""
yourCMDB2 model cmdbobjecttype module

This module is part of the yourCMDB2 model and defines the CMDB Object Types

:license: MIT, see LICENSE for more details
:copyright: (c) 2017 by Michael Batz, see AUTORS for more details
"""

import sqlalchemy
from .ormbase import Base

class CmdbObjectType(Base):

    __tablename__ = "cmdbobject_type"

    cmdbobjecttype_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    cmdbobjecttype_label = sqlalchemy.Column(sqlalchemy.String)
