total_revenue = 0
orders = [100, 150, 450, 340, 230, 500]

def total():
    global total_revenue
    total_revenue = sum(orders)
    print(f'Total revenue: {total_revenue}')

def add_next():
    while True:
        try:
            x = int(input("Unesi broj narudzbina za sledeci dan: "))
            if x >= 0:
                orders.append(x)
                break
        except ValueError:
            print("Niste uneli integer!")

def add_total():
    add_next()
    total()

add_next()
total()
add_total()
