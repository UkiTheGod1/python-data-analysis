# sales_data.py
# Weekly sales data: [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]
sales_data = [230, 200, 310, 290, 400, 150, 180]
print(f"Sales data for the week: {sales_data}")

def total_sales(data):
    total = sum(data)
    print(f"Total sales for the week: {total}")

def average_sales(data):
    average = sum(data) / len(data)
    print(f'Average sale for the week: {average}')

total_sales(sales_data)
average_sales(sales_data)