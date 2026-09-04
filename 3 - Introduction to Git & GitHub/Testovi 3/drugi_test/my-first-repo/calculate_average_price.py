def calculate_average():
    prices = []
    print("Enter price: (end for stop)")

    while True:
        user_input = input("Price: ")
        if user_input.lower() == 'end':
            break
        try:
            price = float(user_input)
            prices.append(price)
        except ValueError:
            print("Enter number or END for stop")

    if prices:
        average_price = sum(prices) / len(prices)
        print(f"Average price is: {average_price:.2f}")
    else:
        print("You not enter any price.")

#call function
calculate_average()
