from flask import Flask, request, jsonify
from flask.ext.cors import CORS
from pc_pp import get_part_info, get_average_price


app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return "welcome"

# @app.route('/item', methods = ['POST'])
# def item():
    # code = request.form.get('code')

@app.route('/price', methods=['POST'])
def price():
    code = request.get_json()["part_no"]
    return str(get_average_price(code))
    # return jsonify(get_average_price(code)) 

if __name__ == '__main__':
    app.debug = True
    app.run()
