library(tidyr)
library(tibble)

drinks_smaller <- tibble(
  country = c("China", "Italy", "Saudi Arabia", "USA"),
  beer = c(79, 85, 0, 249),
  spirit = c(192, 42, 5, 158),
  wine = c(8, 237, 0, 84)
)

drinks_longer <- drinks_smaller |> pivot_longer(
  cols = c(beer, spirit, wine),
  names_to = "type",
  values_to = "count"
)
