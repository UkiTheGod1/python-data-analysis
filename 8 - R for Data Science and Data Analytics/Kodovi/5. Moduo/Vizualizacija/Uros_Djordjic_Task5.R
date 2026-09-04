library(ggplot2)
library(dplyr)
library(readr)

# Uvoz podataka
country_distribution <- read_csv("country_distribution.csv")
genre_by_user <- read_csv("genre_by_user.csv")
ghost_users <- read_csv("ghost_users.csv")
monthly_rentals <- read_csv("monthly_rentals.csv")


# Korisnik-zanr sa brojem iznajmljivanja
ggplot(data = genre_by_user,
       aes(x = user_id,
           y = count,
           fill = genre)) +
  scale_x_continuous(breaks = seq(1, 30)) +
  geom_col() +
  labs(x = "User ID",
       y = "Rental Count",
       fill = "Genre",
       title = "Genre Rentals per User")+
  theme_minimal()


# Promena broja iznajmljivanja po mesecima
ggplot(data = monthly_rentals,
       aes(x = month,
           y = rental_count)) +
  scale_x_continuous(breaks = seq(1, 12)) +
  scale_y_continuous(breaks = seq(0, 35, by = 5)) +
  geom_line(color = "steelblue", size = 1.2) +
  geom_point(color = "navy", size = 2) +
  labs(x = "Month",
       y = "Rental Count",
       title = "Rental Count per Month")+
  theme_minimal()


# Broj korisnika po drzavi
ggplot(data = country_distribution,
       aes(x = country,
           y = user_count,
           fill = country)) +
  geom_col(width = 0.75) +
  scale_y_continuous(breaks = seq(0, 80, by = 10), limits = c(0, 80)) +
  labs(x = "Country",
       y = "User Count",
       title = "Users per Country")+ 
  theme_minimal() +
  theme(legend.position = "none")


# Odnos fantomskih i vernih citalaca
ghost_users <- ghost_users |> mutate(loyalty = ifelse(rental_count >= 10, "Loyal", "Phantom"))

ggplot(data = ghost_users,
       aes(x = loyalty,
           fill = loyalty)) +
  geom_bar(width = 0.5) +
  scale_y_continuous(breaks = seq(0, 100, by= 10), limits = c(0,100)) +
  labs(x = "User Type",
       y = "User Count",
       title = "Number Difference between Loyal and Phantom Users") +
  theme_minimal() +
  theme(legend.position = "none")


# Najpopularniji zanrovi
genre_by_user <- genre_by_user |> 
  group_by(user_id) |> 
  mutate(total_rentals = sum(count)) |> 
  ungroup() |> 
  mutate(loyalty = ifelse(total_rentals >= 3, "Loyal", "Phantom"))

genre_summary <- genre_by_user |>
  group_by(loyalty, genre) |>
  summarise(total = sum(count), .groups = "drop")

ggplot(genre_summary, aes(x = genre, y = total, fill = loyalty)) +
  geom_col(position = "dodge") +
  scale_y_continuous(breaks = seq(0, 16, by= 2)) +
  labs(title = "Genre popularity per User Type",
       x = "Genre",
       y = "Rental Count",
       fill = "User Type") +
  theme_minimal()

# Nisam bio siguran sta se misli pod "po TIPU korisnika" pa sam opet napravio lojalnost.
# Popularni zanrovi su oni koji imaju najvise iznajmljivanja i oni koje iznajmljuju oba tipa korisnika.
# Najpopularniji bi bio Non-Fiction jer, za razliku od Management, iznajmljen je od oba tipa korisnika.
