from excel_komande import *
df = extract_user_data('user_rentals.xlsx').pipe(filter_users).pipe(sort_data).pipe(add_new_column).pipe(remove_columns)
# load_data(df)

# U jednoj liniji smo sproveli sve funkcije (komande) pomocu PIPE (cevi).


# Funkcija pipe() ima sledeći potpis:
# pipe(func, *args, **kwargs)

# Parametri koje funkcija pipe() prihvata imaju sledeću ulogu:

# func je funkcija koja će se primeniti nad DataFrame ili Series skupom podataka; ova funkcija kao prvi argument treba da prihvati DataFrame ili Series skup podataka; kroz takav parametar, njoj se prosleđuje DataFrame ili Series skup podataka nad kojim je funkcija pipe() pozvana; ukoliko planiramo da ovu funkciju koristimo unutar lančane obrade, ona treba da kao svoju povratnu vrednost opet emituje DataFrame ili Series objekat; međutim, ukoliko je reč o poslednjoj operaciji unutar lanca, nije neophodno da funkcija vrati DataFrame ili Series, već to može biti bilo koja druga vrednost;
# *args – jedan ili više pozicionih parametara;
# **kwargs – jedan ili više imenovanih parametara.