# if <uslov koji se ispituje>:
#     <blok koda koji se izvršava ako je uslov tačan>
# else:
#     <blok koda koji se izvršava ako uslov nije tačan>

zalihe = int(input("Unesi broj zaliha: "))
if zalihe < 50:
    print("Upozorenje: Zalihe su niske.")
else:
    print("Zalihe su stabilne.")