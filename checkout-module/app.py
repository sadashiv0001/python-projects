# App.py
from flask import Flask, render_template, request, jsonify
from checkoutKata.ShopCheckout import ShopCheckout
import csv

app = Flask(__name__, template_folder='templates')
checkout = ShopCheckout('items.csv')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def scan_item():
    data = request.get_json()
    items = data.get('items', '')

    # If items is a string, convert it to a list of characters
    if isinstance(items, str):
        items = list(items)

    # Validate if all items are available
    for item in items:
        if item not in checkout.items:
            return jsonify({'message': f"Item '{item}' not available. Please remove it and scan again."}), 400

    # Scan each item individually
    for item in items:
        checkout.scan_item(item)

    return jsonify({'message': 'Items scanned successfully'}), 200



@app.route('/total', methods=['GET'])
def get_total_price():
    items = checkout.get_scanned_items()
    total_price = checkout.calculate_total_price()
    total_info = [{'Item': item, 'Qty': qty, 'Actual Price': checkout.items[item]['unit_price'],
                   'Offer Price': checkout.items[item].get('special_price', 0)} for item, qty in items.items()]
    return jsonify({'items': total_info, 'total_price': total_price}), 200

@app.route('/item_list', methods=['GET'])
def get_item_list():
    items = checkout.get_scanned_items()
    return jsonify({'items': [{'Item': item, 'Qty': qty} for item, qty in items.items()]}), 200

@app.route('/reset', methods=['POST'])
def reset_checkout():
    checkout.reset_checkout()
    return jsonify({'message': 'Checkout reset successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)