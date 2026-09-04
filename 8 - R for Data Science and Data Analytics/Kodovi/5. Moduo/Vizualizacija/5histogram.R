library(nycflights13)
library(ggplot2)
library(dplyr)

# Uvod
ggplot(data = weather,
      aes(x = temp)) + 
  geom_histogram(color = "black")


# Malo opsirnije
ggplot(data = weather, 
       aes(x = temp)) +
  geom_histogram(binwidth = 2, color = "white", fill = "steelblue") +
  scale_x_continuous(breaks = seq(10, 100, by = 5)) +
  labs(x = "Temp (°F)", y = "Count")

ggplot(data = weather, 
       aes(x = temp)) +
  geom_histogram(bins = 40, color = "white") # Kontrola broja stubova
