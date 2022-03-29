product_name = "\"Toilet Paper\""
product_price = 5.00
delivery_cost = 50

print("#"*30)
print(product_name, ":", product_price)

answer = input("Do you want to buy? (y/n)").lower().strip()
if answer == '':
    answer = "n"
if answer[0] == "y":
    order_quantity = input("How many? ")
    if order_quantity.isnumeric():
        order_cost = int(order_quantity) * product_price

        print("-"*30)
        print("Order Info")
        print(product_name, "x", order_quantity, "=", order_cost)

        answer = input("Do you want delivery? (y/n)").lower().strip()
        if answer == '':
            answer = "n"
        if answer[0] == "y":
            order_cost += delivery_cost
            print("Order cost (including delivery)", order_cost)
        else:
            print("Order cost ", order_cost)
    else:
        print("Too bad :(")
else:
    print("Bye :(")