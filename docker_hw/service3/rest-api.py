import json
import os
from time import sleep
import psycopg2
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    for i in range(int(os.environ["MAX_RECONNECT_ITER"])):
        try:
            connection = psycopg2.connect(
                dbname=os.environ["POSTGRES_DB"],
                user=os.environ["POSTGRES_USER"],
                password=os.environ["POSTGRES_PASSWORD"],
                host="localhost",
                port=int(os.environ["POSTGRES_PORT"])
            )
            break
        except:
            sleep(float(os.environ["RECONNECT_SLEEP_TIME"]))
    else:
        raise TimeoutError("Couldn't connect to postgres database at this port!")
    cursor = connection.cursor()
    try:
        cursor.execute(f"SELECT * FROM {os.environ['TABLE_NAME']}")
        result = []
        for res in cursor:
            result.append(res)
        connection.close()
        return json.dumps({'success': True, 'data': result}), 200, {'ContentType': 'application/json'}
    except:
        return json.dumps({'success': False, 'data': []}), 500, {'ContentType': 'application/json'}


@app.route('/health', methods=["GET"])
def healthcheck():
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}


@app.errorhandler(404)
def page_not_found():
    return "Request not supported!", 404


if __name__ == '__main__':
    app.run(debug=True, port=os.environ["WEB_SERVER_PORT"])
