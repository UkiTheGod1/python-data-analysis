library(nycflights13)
library(ggplot2)
library(dplyr)

early_january_weather <- weather |> filter(origin == "EWR" & month == 1 & day <= 15)

ggplot(data = early_january_weather,
       aes(x = time_hour,
           y = temp)) + 
  geom_line()
