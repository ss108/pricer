from flask import Flask
from soup_test import get_prices_for_product


app = Flask(__name__)

@app.route('/')
def index():
    return "welcome"

@app.route('/price')
def price():
    s = "asus-video-card-r9270xdc22gd5"
    prices = get_prices_for_product(s) 
    return str(prices)

if __name__ == '__main__':
    app.debug = True
    app.run()
