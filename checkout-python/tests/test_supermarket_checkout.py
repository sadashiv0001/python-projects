from SupermarketCheckout import SupermarketCheckout

def test_calculate_total_price():
    checkout = SupermarketCheckout()

    # Test case 1
    checkout.scan_item('A')
    assert checkout.calculate_total_price() == 50

    # Test case 2
    checkout.scan_item('A')
    checkout.scan_item('A')
    assert checkout.calculate_total_price() == 130

    # Add more test cases as needed
