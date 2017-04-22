#! /usr/bin/python3
"""
yourCMDB2 main module

This is the main module of yourCMDB2, wich starts the application

:license: MIT, see LICENSE for more details
:copyright: (c) 2017 by Michael Batz, see AUTORS for more details
"""
import web.gunicornsupport
import web.dispatcher

def main():
    webapp_conf = {
        "bind": "0.0.0.0:5000",
        "workers": "2"
    }
    webapp = web.gunicornsupport.WebApplication(web.dispatcher.app, webapp_conf)
    webapp.run()
    print("Hello World")



if __name__ == "__main__":
    main()
