total_sales = 1000
 
def update_sales(new_sale):
    global total_sales # Pristupa globalnog promenljivoj da ne moramo opet da je definisemo na lokalnom nivou
    total_sales += new_sale # Ne mozemo dodati na promenljivu koja nije definisana (sa "global" jeste)
 
update_sales(500)
print(total_sales)