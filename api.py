from flask import Flask, request, jsonify
from flask.ext.cors import CORS
from pc_pp import get_part_info, get_average_price


app = Flask(__name__)
CORS(app)

def _get_q_type(json_payload):
    try:
        return json_payload["q_type"]
    except KeyError:
        return ""

@app.route('/')
def index():
    return "welcome"

@app.route('/price', methods=['POST'])
def price():
    try:
        # return request
        query_type = _get_q_type(request.get_json(force=True)) 

        if query_type == "keyword":
            #some stuff
            pass
        else:
            code = request.get_json(force=True)["part_no"]

        return str(get_average_price(code))
    except Exception as ex:
        return "0"


if __name__ == '__main__':
    app.debug = True
    app.run()
