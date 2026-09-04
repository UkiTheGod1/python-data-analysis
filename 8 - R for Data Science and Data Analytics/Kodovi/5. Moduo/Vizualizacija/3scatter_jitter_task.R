library(nycflights13)
library(ggplot2)
library(dplyr)

united_airlines <- flights |> filter(carrier == "UA")

ggplot(data = united_airlines,
       aes(x = dep_delay,
           y = air_time)) +
  geom_point(alpha = 0.1)

ggplot(data = united_airlines,
       aes(x = dep_delay,
           y = air_time)) +
  geom_jitter(height = 50, width = 50)

