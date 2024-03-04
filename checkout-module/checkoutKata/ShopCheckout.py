import csv

class ShopCheckout:
    def __init__(self, items):
        self.items = self.load_items_from_csv(items)
        self.item_counts = {}

    def load_items_from_csv(self, csv_path):
        items = {}
        with open(csv_path, newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                item_name = row['Item']
                unit_price = int(row['Actual Price'])
                special_price = int(row['Offer Price']) if row['Offer Price'] else None
                special_qty = int(row['Special Qty']) if 'Special Qty' in row and row['Special Qty'] else None

                items[item_name] = {
                    'unit_price': unit_price,
                    'special_price': special_price,
                    'special_qty': special_qty,
                }
        return items

    def scan_item(self, item):
        if item not in self.items:
            return f"Item '{item}' not available"

        if item in self.item_counts:
            self.item_counts[item] += 1
        else:
            self.item_counts[item] = 1

    def calculate_total_price(self):
        total_price = 0

        for item, count in self.item_counts.items():
            if item in self.items:
                unit_price = self.items[item]['unit_price']
                special_price = self.items[item].get('special_price')
                special_qty = self.items[item].get('special_qty')

                if special_price and count >= special_qty:
                    total_price += (count // special_qty) * special_price + (count % special_qty) * unit_price
                else:
                    total_price += count * unit_price

        return total_price

    def get_scanned_items(self):
        return self.item_counts

    def reset_checkout(self):
        self.item_counts = {}
