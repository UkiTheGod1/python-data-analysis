import requests

title = 'To Kill a Mockingbird'
author = 'Harper Lee'
url = f'https://openlibrary.org/search.json?title={title}&author={author}'
response = requests.get(url)
data = response.json()

# Ako knjiga mozda ne postoji
if(data["num_found"] > 0):
    first_book = data["docs"][0] # Na primer
else:
    print('Book not found')

# Knjiga postoji ali ne i odredjeni podaci
if(data["num_found"] > 0):
    first_book = data["docs"][0]
 
    if "first_sentence" in first_book:
        print(first_book["first_sentence"]) # Ne printuje jer ne postoji podatak
     
    if "subject" in first_book:
        print(first_book["subject"]) # Ne printuje jer ne postoji podatak
 
    if "place" in first_book:  
        print(first_book["place"]) # Ne printuje jer ne postoji podatak
 
    if "time" in first_book:  
        print(first_book["time"]) # Ne printuje jer ne postoji podatak
else: 
    print('Book not found') 

# Los URL 
# url = f'https://openlibrary.org/find.json?movie={title}&author={author}'
if "error" in data:
    print(data['error'])
else:
    first_book = data["docs"][0]

# Servis nema kontakt - Sve zajedno
try:
 
    response = requests.get(url)
    data = response.json()
 
    if "error" in data:
        print(data['error'])
         
    elif(data["num_found"] > 0):
        first_book = data["docs"][0]
 
        if "first_sentence" in first_book:
            print(first_book["first_sentence"])
         
        if "subject" in first_book:
            print(first_book["subject"])
 
        if "place" in first_book:  
            print(first_book["place"])
 
        if "time" in first_book:  
            print(first_book["time"])
 
    else:
        print('Book not found')
 
except requests.exceptions.ConnectionError:
    print("Error: The server is unavailable or the URL is invalid.")
except requests.exceptions.Timeout:
    print("Error: The request has timed out.")
except requests.exceptions.RequestException as e:
    print(f"Request error: {e}")
except Exception as e:
    print(f"Unexpected error:: {e}")

# ConnectionError je greška do koje dolazi kada klijent ne može da uspostavi konekciju sa serverom. 
# Razlozi mogu biti: nedostupan server, pogrešan URL ili domen, problem sa mrežnom konekcijom klijenta…

# Timeout je greška do koje dolazi kada server ne odgovori u zadatom vremenskom okviru. 
# To se često dešava zbog preopterećenja servera ili sporih mreža.

# RequestException je generički tip greške koji obuhvata sve moguće probleme u vezi sa klijentskim zahtevom koji nisu obuhvaćeni specifičnijim izuzecima (npr. ConnectionError, Timeout…).

# Exception je osnovna klasa u Pythonu iz koje proizilaze sve druge klase izuzetaka. 
# Stoga će se except blok sa ovakvim izuzetkom aktivirati samo onda kada dođe do izuzetka koji nije uhvaćen prethodno definisanim specifičnim blokovima. 
# To je neka vrsta poslednje linije odbrane za hvatanje svih neočekivanih grešaka koje nisu obuhvaćene specifičnim izuzecima.
