import pandas as pd

def extract_data(file_name):
    return pd.read_csv(file_name)

# Filtriramo podatke tako da samo filmovi prvih 10 filmova iz odjredjene drzave sa najvecom zaradom su prikazani
def filter_usa(data):
    mask = data["country"] == "USA"
    return data[mask].head(10)
    
def filter_russia(data):
    mask = data["country"] == "Russia"
    return data[mask].head(10)

def filter_uk(data):
    mask = data["country"] == "UK"
    return data[mask].head(10)

def filter_korea(data):
    mask = data["country"] == "South Korea"
    return data[mask].head(10)
# Nisam smislio nacin da napravim univerzalnu funkciju

# Sortiramo i stavljamo "False" kako bi najveca vrednost bila prva
def sort_data(data):
    data["box_office"] = pd.to_numeric(data["box_office"], errors="coerce") 
    # Uspesno smo pretvorili kolonu box_office u numericki tip podataka.
    # Nismo mogli koristiti komandu .astype() jer ima polja koja su "unknown" i string ne moze pretvoriti u broj
    balance = data["box_office"] - data["budget"]
    data["balance"] = balance
    # Napravili smo novu kolonu balance koja pokazuje razliku budzeta i zarade
    return data.sort_values(by="balance", ascending=False)

def remove_columns(data):
    return data.drop(["language", "country", "duration", "budget", "box_office"], axis=1)
