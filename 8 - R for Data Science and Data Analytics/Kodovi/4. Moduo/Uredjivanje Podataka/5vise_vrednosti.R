library(tidyverse)
library(dplyr)

df <- tribble(
  ~id, ~measurement, ~value,
  "A",        "bp1",    100,
  "B",        "bp1",    140,
  "B",        "bp2",    115,
  "A",        "bp2",    120,
  "A",        "bp3",    105
)


df_wider <- df |> pivot_wider(
  names_from = measurement,
  values_from = value
)

# Radi sve full - ali sta kad imamo vise vrednosti za istu kombinaciju?

df2 <- tribble(
  ~id, ~measurement, ~value,
  "A", "bp1", 100,
  "A", "bp1", 102,
  "A", "bp2", 120,
  "B", "bp1", 140,
  "B", "bp2", 115
)

df2_wider <- df2 |> pivot_wider(
    names_from = measurement,
    values_from = value
)

# Radi, ali pravi listu unutar jedne celije

df2 |> count(id, measurement) |> filter(n > 1)
# Kombinacija A i BP1 se pojavljuce 2 puta

df2_avg <- df2 |> group_by(id, measurement) |> summarise(avg_value = mean(value), .groups = "drop")
# Spojili smo 2 vrednosti u jednu prosecnu

df2_avg_wider <- df2_avg |> pivot_wider(
  names_from = measurement,
  values_from = avg_value
)
