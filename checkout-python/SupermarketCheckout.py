class SupermarketCheckout:
    def __init__(self):
        self.pricing = {
            'A': {'unit_price': 50, 'special_price': 130, 'special_qty': 3},
            'B': {'unit_price': 30, 'special_price': 45, 'special_qty': 2},
            'C': {'unit_price': 20},
            'D': {'unit_price': 15},
        }
        self.item_counts = {}

    def scan_item(self, item):
        if item in self.item_counts:
            self.item_counts[item] += 1
        else:
            self.item_counts[item] = 1

    def calculate_total_price(self):
        total_price = 0

        for item, count in self.item_counts.items():
            if item in self.pricing:
                unit_price = self.pricing[item]['unit_price']
                special_price = self.pricing[item].get('special_price')
                special_qty = self.pricing[item].get('special_qty')

                if special_price and count >= special_qty:
                    total_price += (count // special_qty) * special_price + (count % special_qty) * unit_price
                else:
                    total_price += count * unit_price

        return total_price

# Usage example:
checkout = SupermarketCheckout()
checkout.scan_item('A')
checkout.scan_item('B')
checkout.scan_item('A')
total_price = checkout.calculate_total_price()
print("Total Price:", total_price)
