# try:
# kod koji mislimo da ima gresku (ako nema ostaje zabelezen)
 
# except:
# kod koji se ispisuje ako greska postoji (npr print("Postoji greska"))

# finally:
# kod koji ce se ispisati nevezano ni za sta (osim ako nema greske u kodu)

try:
    x=100/0
except NameError:
    print("You won't see me!")
except ZeroDivisionError:
    print("Hey, you can't divide by zero!")
except Exception:
    print("I'm here just in case you didn't find anything")
finally:
    print("Ja se uvek ispisujem idgaf")