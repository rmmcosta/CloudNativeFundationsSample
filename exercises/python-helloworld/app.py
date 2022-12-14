from flask import Flask
import logging
import logging.config
import yaml
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def hello():
    logging_endpoint("hello")
    return "Hello World!"


@app.route("/status")
def status():
    logging_endpoint("status")
    return {
        "result": "OK - healthy"
    }
    # return Response("{result: OK - healthy}", mimetype="application/json")


@app.route("/metrics")
def metrics():
    logging_endpoint("metrics")
    return {
        "data": {
            "UserCount": 140,
            "UserCountActive": 23
        }
    }
    # return Response("{data: {UserCount: 140, UserCountActive: 23}}", mimetype="application/json")


def logging_endpoint(enpoint_name):
    app.logger.info("%s, %s endpoint was reached",
                    datetime.now(), enpoint_name)


# if __name__ == "__main__":
#     logging.config.dictConfig(yaml.load(open('logging.conf')))
#     logfile = logging.getLogger('file')
#     logconsole = logging.getLogger('console')
#     logfile.debug("Debug FILE")
#     logconsole.debug("Debug CONSOLE")
#     from waitress import serve
#     serve(app, host="0.0.0.0", port=5000)
    #app.run(host='0.0.0.0')

#https://stackoverflow.com/questions/51025893/flask-at-first-run-do-not-use-the-development-server-in-a-production-environmen
def create_app():
    logging.config.dictConfig(yaml.load(open('logging.conf')))
    logfile = logging.getLogger('file')
    logconsole = logging.getLogger('console')
    logfile.debug("Debug FILE")
    logconsole.debug("Debug CONSOLE")
    #waitress-serve --port=5000 --call app:create_app
    return app
