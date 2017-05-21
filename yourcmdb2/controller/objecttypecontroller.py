"""
yourCMDB2 controller objecttype module

This module controlls the access to the yourCMDB2 object type model

:license: MIT, see LICENSE for more details
:copyright: (c) 2017 by Michael Batz, see AUTHORS for more details
"""

import json
from ..model.orm import OrmHelper
from ..model.daoobjecttype import CmdbObjectType
from ..model.daoobjecttype import CmdbObjectTypeField
from ..model.daoobjecttype import CmdbObjectTypeLink

class ObjectTypeController(object):

    def create(self, input_json):
        # decode json and check input
        input_data = json.loads(input_json)

        # ToDo: check input, init with default values
        try:
            type_label = input_data["label"]
            type_summary = input_data["summarystring"]
            type_comment = input_data["comment"]
            type_fields = input_data["fields"]
            type_links = input_data["links"]
        except:
            # ToDo: error handling / exceptions
            return False

        # create object type
        orm_helper = OrmHelper()
        orm_session = orm_helper.create_session()
        created_type = CmdbObjectType(
            objecttype_label=type_label,
            objecttype_summarystring=type_summary,
            objecttype_comment=type_comment
        )
        orm_session.add(created_type)
        orm_session.flush()

        # create object type fields
        for type_field in type_fields:
            field_name = type_field
            field_type = type_fields[type_field]["type"]
            field_group = type_fields[type_field]["group"]
            field_label = type_fields[type_field]["label"]
            field_constraint = type_fields[type_field]["constraint"]
            field_summary = type_fields[type_field]["summary"]
            field_order = type_fields[type_field]["order"]
            created_field = CmdbObjectTypeField(
                field_objecttype=created_type.objecttype_id,
                field_name=field_name,
                field_group=field_group,
                field_order=field_order,
                field_label=field_label,
                field_type=field_type,
                field_summary=field_summary,
                field_constraint=field_constraint
            )
            orm_session.add(created_field)

        # create object type links
        for type_link in type_links:
            link_order = type_link["order"]
            link_label = type_link["label"]
            link_url = type_link["url"]
            created_link = CmdbObjectTypeLink(
                link_objecttype=created_type.objecttype_id,
                link_order=link_order,
                link_label=link_label,
                link_url=link_url
            )
            orm_session.add(created_link)

        # commit and close orm session
        orm_session.commit()
        orm_session.close()



    def read(self, type_id):
        pass


    def update(self, type_id, input_json):
        pass


    def delete(self, type_id):
        pass
