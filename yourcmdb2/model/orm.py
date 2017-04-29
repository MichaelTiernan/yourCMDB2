"""
yourCMDB2 model orm module

This is the orm module of yourCMDB2 model

:license: MIT, see LICENSE for more details
:copyright: (c) 2017 by Michael Batz, see AUTORS for more details
"""

import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from .. import config
from .ormbase import Base
from . import daoobjecttype


class OrmHelper(object):

    def __init__(self):
         # get yourCMDB2 configuration
        appconf = config.FileConfig()
        self.__engine = sqlalchemy.create_engine(appconf.get_value("DatabaseConnection", "url", ""))

    def create_dbstructure(self):
        Base.metadata.create_all(self.__engine)

    def create_session(self):
        Session = sqlalchemy.orm.sessionmaker()
        Session.configure(bind=self.__engine)
        return Session()
