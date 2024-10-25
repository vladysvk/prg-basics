number_of_products = int(input("Number of products purchased: "))
product_price = int(input("Product price: "))

discount_products = number_of_products // 3

discount = discount_products * product_price * 0.25

amount_to_pay = number_of_products * product_price - discount

print(f"Amount to pay: {amount_to_pay: .2f}$")