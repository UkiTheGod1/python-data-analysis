promotions_damage = 4000

jan_customers = 135
avg_jan = 52.75

feb_customers = 120
avg_feb = 47.5

total_customers = jan_customers + feb_customers
print("Ukupni kupci za januar i februar su: ", total_customers)

total_avg = avg_jan + avg_feb
print("Prosecna prodaja za januar i februar je:", total_avg)

mar_customers = 140
avg_mar = 48.25

total_customers += mar_customers
print("Ukupni kupci za januar,februar i mart su:", total_customers)

total_avg += avg_mar
print("Prosecna prodaja za januar, februar i mart je:",total_avg)

total_sales = total_customers * total_avg
print("Ukupna prodaja je:", total_sales)

total_sales -= promotions_damage
print("Ukupna prodaja nakon troskova promocija je:", total_sales)





