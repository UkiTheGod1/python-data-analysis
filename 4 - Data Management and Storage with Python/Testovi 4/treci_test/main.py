import pandas as pd
import requests

df = pd.read_csv("movies_test.csv") # Promenio sam ime fajla jer movies.csv vec postoji
print(df) # Ucitavanje i ispisivanje podataka iz movies_test.csv 

# Pristupamo podacima sa web servisa
api_key = "f488d09c"
def get_movie_data(title, year):

    url = f"https://www.omdbapi.com/?t={title}&y={year}&apikey={api_key}"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status() # Proveramo status
        data = response.json()

        if data.get("Response") == "True":
            return {
                "imdb_rating": data.get("imdbRating", "N/A"),
                "actors": data.get("Actors", "N/A"),
                "imdb_votes": data.get("imdbVotes", "N/A")
            }
        else:
            print(f"Film '{title}' ({year}) nije pronadjen.")
            return None

    except requests.exceptions.ConnectionError:
        print("Greska: Problem sa serverom ili internet konekcijom.")
    except requests.exceptions.Timeout:
        print("Greska: Istekao je zahtev.")
    except requests.exceptions.RequestException as e:
        print(f"Greska: {e}")
    except Exception as e:
        print(f"Nepoznata greska: {e}")

    return None

# Cuvamo izvedene podatke
df["imdb_rating"] = ""
df["actors"] = ""
df["imdb_votes"] = ""

for index, row in df.iterrows():
    movie_data = get_movie_data(row["title"], row["release_year"])
    if movie_data:
        df.at[index, "imdb_rating"] = movie_data["imdb_rating"]
        df.at[index, "actors"] = movie_data["actors"]
        df.at[index, "imdb_votes"] = movie_data["imdb_votes"]

# Zapisujemo podatke u novi csv i xml
df.to_csv("movies_imdb.csv", index=False)
df.to_xml("movies_imdb.xml", parser="etree", root_name="movies", row_name="movie", index=False)

print(df.dtypes) # Proveravamo da li je imdb_rating interger ili float kako bismo mogli raditi sortirati
df["imdb_rating"] = pd.to_numeric(df["imdb_rating"], errors="coerce")
top_10 = df.sort_values(by="imdb_rating", ascending=False).head(10)
print(top_10[["title", "release_year", "imdb_rating", "imdb_votes"]]) 
# Printuje top 10 filmova sa najvecim IMDB rejtingom

# Nisam najbolje savladao ovo gradivo, radio sam zadatak uz pomoc.