library(nycflights13)  # podaci o letovima
library(ggplot2)       # crtanje grafikona
library(gapminder)     # podaci o državama
library(dplyr)

alaska_flights <- flights |> filter(carrier == "AS")

ggplot(data = alaska_flights, 
       aes(x = dep_delay, y = arr_delay)) + 
    geom_point(alpha = 0.2) # Preklapaju se tacke pa im smanjujemo vidljivost

ggplot(data = alaska_flights, 
       aes(x = dep_delay, y = arr_delay)) +
  geom_jitter(width = 30, height = 30) # Razdvaja
