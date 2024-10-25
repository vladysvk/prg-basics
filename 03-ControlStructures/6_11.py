current_price = 140
previous_price = 200
percentage = (previous_price - current_price) / previous_price * 100
if percentage >= 10:
    print("Buy the product")
    print(f"Product price reduced by {int(percentage)}%")