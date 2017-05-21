#! /usr/bin/python3
"""temporary test module"""

import json
import yourcmdb2.controller.objecttypecontroller as objecttypecontroller

def main():

    # create objecttype
    type_router = {}
    type_router["summarystring"] = ""
    type_router["label"] = "router"
    type_router["comment"] = "a comment on all router objects"
    type_router["fields"] = {}
    type_router["fields"]["hostname"] = {
        "group" : "management",
        "order" : 1,
        "label" : "Hostname",
        "type" : "text",
        "summary" : True,
        "constraint" : ""
    }
    type_router["fields"]["ip"] = {
        "group" : "management",
        "order" : 2,
        "label" : "Management-IP",
        "type" : "text",
        "summary" : True,
        "constraint" : ""
    }
    type_router["fields"]["monitoring"] = {
        "group" : "management",
        "order" : 3,
        "label" : "Monitoring",
        "type" : "text",
        "summary" : False,
        "constraint" : ""
    }
    type_router["fields"]["serial"] = {
        "group" : "hardware",
        "order" : 1,
        "label" : "Serial",
        "type" : "text",
        "summary" : False,
        "constraint" : ""
    }
    type_router["links"] = []
    type_router["links"].append({
        "order" : 1,
        "label" : "Monitoring",
        "url" : "https://monitoring.example.net/host=%hostname%"
    })

    print(json.dumps(type_router, indent=4))
    controller = objecttypecontroller.ObjectTypeController()
    controller.create(json.dumps(type_router))


if __name__ == "__main__":
    main()
