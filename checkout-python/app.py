from flask import Flask, request, jsonify
from SupermarketCheckout import SupermarketCheckout

app = Flask(__name__)
checkout = SupermarketCheckout()

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/calculate_total', methods=['GET'])
def calculate_total():
    items = request.args.get('items', '')
    for item in items:
        checkout.scan_item(item)
    total_price = checkout.calculate_total_price()
    return jsonify({'total': total_price})

if __name__ == '__main__':
    app.run(debug=True)
