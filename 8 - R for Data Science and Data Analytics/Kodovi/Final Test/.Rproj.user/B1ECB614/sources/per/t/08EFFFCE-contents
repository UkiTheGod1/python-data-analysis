library(nycflights13)
library(tidyverse)
library(dplyr)

flights2 <- flights |>
  select(year, time_hour, origin, dest, tailnum, carrier)

flights2 |> left_join(airlines) # Dodaje name iz Airlines

flights2 |> right_join(airlines) # Retko se koristi, airlines je glavna i na nju se dodaje flights2

flights2 |> inner_join(airlines) # Prikazuje samo poklapanja (presek)

flights2 |> full_join(airlines) # Spaja full


# Joinamo po kolonama koje imaju drugacije im, a iste vrednosti
flights2 |> left_join(airports, join_by(dest == faa))

flights2 |> left_join(airports, join_by(origin == faa))
