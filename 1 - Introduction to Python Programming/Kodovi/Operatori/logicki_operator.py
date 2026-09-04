cus_jan = 135
avg_feb = 47.5

ans = cus_jan > 100 and avg_feb < 50
print(ans)

ans = cus_jan > 100 or avg_feb > 50
print(ans)

ans = not(avg_feb > 50)
print(ans)

# cus_jan != 1200       ova dva su ista
# not(cus_jan == 1200)