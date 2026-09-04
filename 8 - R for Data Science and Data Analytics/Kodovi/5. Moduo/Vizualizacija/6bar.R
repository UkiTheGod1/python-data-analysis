library(nycflights13)
library(ggplot2)
library(dplyr)  # ako bude grupisanja

# Neprebrojani podaci (geom_bar)
ggplot(flights, 
       aes(x = carrier)) +
  geom_bar(fill = "steelblue") +
  labs(title = "Flights number per carrier",
    x = "Carrier",
    y = "Flight number" ) +
  theme_minimal() # Uklanja visak elemenata na slici, npr. pozadinu

# Prebrojani podaci (geom_col)
origin_summary <- flights |> group_by(origin) |> summarise(broj_letova = n())

ggplot(origin_summary, 
       aes(x = origin, 
           y = broj_letova)) +
  geom_col(fill = "darkorange") +
  labs( title = "Flights number per carrier",
    x = "Carrier",
    y = "Flight number") +
  theme_minimal()

# Stacked Barplot
ggplot(flights, 
       aes(x = carrier, fill = origin)) + 
  geom_bar()

# Dodge Barplot - preglednije
ggplot(flights, 
       aes(x = carrier, fill = origin)) + 
  geom_bar(position = "dodge")

# Panel Barplot
ggplot(flights, aes(x = carrier)) +
  geom_bar() +
  facet_wrap(~ origin, ncol = 1)
