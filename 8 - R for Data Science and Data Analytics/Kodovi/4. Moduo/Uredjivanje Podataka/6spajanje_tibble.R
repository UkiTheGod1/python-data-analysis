library(tidyverse)
library(nycflights13)

# left_join()
# right_join()
# inner_join()
# full_join()
# semi_join()
# anti_join()

# join_function(x, y, by = ...)
# x i y su tabele koje spajamo;
# by definiše kolonu (ili kolone) koje su povezane;
# rezultat: novi data frame.

x <- tibble(id = c(1, 2, 3), name = c("Alex", "Marc", "Nico"))

y <- tibble(id = c(1, 3), age = c(25, 30))

left_join(x, y, by = "id") # Dodaje sve iz X i ono sto se spaja sa Y
