def total_sold(lista):
    values = lista.values()
    return sum(values)

def most_sold(lista):
 return max(lista, key=lambda item: lista[item]) # 3. Lambda

def least_sold(lista):
 return min(lista, key=lambda item: lista[item]) # 3. Lambda

def critical(lista):
    below_50 = list(filter(lambda x: lista[x] < 50, lista)) # 6.  filter i lambda
    return below_50

def validate_sales_data(lista):
    invalid = False
    for product, value in lista.items():
        if value < 0:
            print(f"Proizvod {product} ima negativnu vrednost: {value}")
            invalid = True
        elif value > 100000:
           print(f'Proizvod {product} ima neuobicajeno visoku vrednost: {value}')
    if not invalid:
        print("Svi proizvodi imaju pozitivnu vrednost")

# Nova funkcija get_product_sales() koja, pretpostavlja, vraća vrednost unetog proizvoda iz unete liste:
def get_product_sales(lista, product):
    try:
        product = product.title()
        value = lista[product]
        if value < 0:
            print(f"Greska: Proizvod {product} ima nerealnu vrednost: {value}")
        else:
            print(f'Proizvod {product} je prodat {value} puta')
    except KeyError:
        print("Proizvod koji ste uneli ne postoji.")