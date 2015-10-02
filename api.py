from flask import Flask, request, jsonify
from flask.ext.cors import CORS

app = Flask(__name__)
CORS(app)



# TODO: support keyword lookup (or else this tool will suck mucho : ))))
# def _get_q_type(json_payload):
#     try:
#         return json_payload["q_type"]
#     except KeyError:
#         return ""


@app.route('/')
def index():
    return "welcome"

@app.route('/price', methods=['POST'])
def price():
    try:
        code = request.get_json(force=True)["part_no"]
        cat_no = request.get_json(force=True)["cat_no"]
        #all sources for category from db
        #instantiate classes based on info from db
        #call "calc_average_price" on all of them and average the result
        #return that
        return str(get_average_price(code))
    except Exception as ex:
        return "0"


if __name__ == '__main__':
    app.debug = True
    app.run()
