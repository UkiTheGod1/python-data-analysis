visits <- c(145, 212, 198, 180, 90, 30, 25)
visits[1]
visits[1:3]
visits[c(2, 5, 7)]

books <- c(5, 12, 8, 15, 20)
books <- books + 1 # Radi kao for i in range
books

head(visits) # Printuje prvih 6
length(visits)    # Broj dana
min(visits)       # Najmanji broj poseta
max(visits)       # Najveći broj poseta
sum(visits)       # Ukupan broj poseta
mean(visits) 

which(visits > 100)
greater_than_100 <- visits > 100
visits[greater_than_100] # Prikazuju posete vece od 100 (log)

filmovi_eng <- c(
  "The Godfather",
  "The Dark Knight",
  "Pulp Fiction",
  "The Lord of the Rings: The Fellowship of the Ring",
  "Inception",
  "Fight Club",
  "Forrest Gump",
  "The Matrix",
  "Interstellar",
  "The Shawshank Redemption",
  "Gladiator",
  "The Departed"
)

head(filmovi_eng, 5) # Prikazuje prvih 5