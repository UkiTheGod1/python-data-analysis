library(readr)
library(tidyverse)
library(dplyr)

# Uvoz podataka dobijenih datasetova
books <- read_csv("books_2.0.csv")
users <- read_csv("users.csv")
rentals <- read_csv("rentals.csv")

glimpse(books) # Tip kolone "published" nije dobar i postoji nepotrebna kolona
glimpse(users) # Tip kolone "member_since" nije dobar
glimpse(rentals) # Tipovi kolona "return_date_1" i "return_date_2" nisu dobri

# Ispravak
books <- read_csv("books_2.0.csv",
                  na = c("N/A", ""),
                  col_types = cols(
                    id = col_double(),
                    title = col_character(),
                    author = col_character(),
                    published = col_integer(),
                    genre = col_character(),
                    '???' = col_skip(),
                    dummy_score = col_double()
                  )
)

users <- read_csv("users.csv", na = c("N/A", ""))
users$member_since <- as.Date(users$member_since, format = "%d.%m.%Y") # Formatiramo datum

rentals <- read_csv("rentals.csv", na = c("N/A", ""))
rentals$return_date_1 <- as.Date(rentals$return_date_1, format = "%d.%m.%Y")
rentals$return_date_2 <- as.Date(rentals$return_date_2, format = "%d.%m.%Y")


# Spremanje rentals
rentals_tidy <- rentals |>
  pivot_longer(
    cols = c(ends_with("_1"), ends_with("_2")),
    names_to = c(".value", "book_number"),
    names_pattern = "(.*)_(\\d)",
    values_drop_na = TRUE
  )

# Spajanje rentals_tidy i users
rentals_users <- rentals_tidy |> left_join(users, by="user_id")
count(rentals_tidy) # 200 redova
count(rentals_users) # 208 redova
n_distinct(users$user_id) # 94 unikatne vrednosti ID usera, a 100 redova
# Zakljucak - Neki user_id se ponavljaju u users dataframe-u tj. razliciti korisnici dele isti user_id

# Spajanje rentals_users i books
full_df <- rentals_users |> left_join(books, join_by(book_id == id))
# full_df ima 3 vise reda u odnosu na rentals_users -
books |> count(id) |> filter(n > 1) # Ima 38 knjiga koje dele 19 ID-a (2 knjige - 1 ID)
# Ako je neko iznajmio knjigu sa ID koji odgovara vise knjiga, pisace da je iznajmio obe knjige

# Provera korisnika u rentals
anti_join(rentals, users, by="user_id")
# Ima 10 korisnika u rentals koji ne postoje u users (user 86 i korisnici nakon broja 100)

# Radne tabele
rentals_per_user <- full_df |> group_by(user_id) |> summarise(count = n())
rentals_per_genre <- full_df |> group_by(genre) |> summarise(count = n())

# ZADACI

# Koji zanrovi su najpopularniji - i od koga?
full_df_genre <- full_df |> filter(!is.na(genre))
genres_per_users <- full_df_genre |> group_by(user_id, genre) |> summarise(rentals_count = n(), .groups= "drop")
# Definisali smo koji korisnik je citao koji zanr, a u rentals_per_genre imamo ukupan broj iznajmljivanja po zanru

# Kako se broj iznajmljenih knjiga menja po mesecima?
rentals_tidy <- rentals_tidy |> mutate(month = month(return_date, label = TRUE, abbr = FALSE)) # Nova kolona "month"
rentals_per_month <- rentals_tidy |> group_by(month) |> summarise(count = n())

# Imamo li korisnike koji se vraćaju po slične knjige?
loyal_readers <- full_df_genre |> group_by(user_id, genre) |> 
  summarise(rentals_count = n(), .groups = "drop") |> filter(rentals_count > 1) # Samo trojica

# A one koji dođu jednom i nestanu?
phantom_readers <- full_df |>  group_by(user_id) |> 
  summarise(rentals_count = n(), .groups = "drop") |> filter(rentals_count == 1) # Samo dvojica

# Stanovnici koje države najčešće posećuju biblioteku?
rentals_per_country <- rentals_users |> group_by(country) |> summarise(count = n(), .groups = "drop")
rentals_per_country <- rentals_per_country |> filter(!is.na(country)) # USA ima najvise (52)

# Možemo li napraviti tabelu: jedan red po korisniku, kolone po žanru, vrednosti kao broj iznajmljivanja?
custom_df <- full_df_genre |> group_by (user_id, genre) |> summarise(n = n(), .groups = "drop") |>
  pivot_wider(
    names_from = genre,
    values_from = n,
    values_fill = 0
)
