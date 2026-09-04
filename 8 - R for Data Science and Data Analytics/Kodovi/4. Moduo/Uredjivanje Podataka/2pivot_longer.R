library(tidyverse)
library(billboard)
View(billboard)

#pivot_longer: kad kolone postaju redovi, a tabela postaje priča.

billboard |> pivot_longer(
    cols = starts_with("wk"),
    names_to = "week",
    values_to = "rank",
    values_drop_na = TRUE # Dropuje NA vrednosti logicno
  )

# cols = starts_with("wk")
# Ovde kažemo R-u: uzmi sve kolone koje počinju sa „wk”.
# To su kolone koje predstavljaju nedelje – i one nisu tidy.

# names_to = "week"
# Naziv nove kolone gde ćemo smestiti ono što su ranije bili nazivi kolona.
# Dakle, wk1, wk2… sad postaju vrednosti u koloni week.

# values_to = "rank"
# Ovde ulazi stvarna pozicija pesme – ono što je bilo unutar ćelija u tabeli, sad ide u novu kolonu rank.

billboard_longer <- billboard |> pivot_longer(
    cols = starts_with("wk"),
    names_to = "week",
    values_to = "rank",
    values_drop_na = TRUE
  ) |>
  mutate(
    week = parse_number(week) # Automatski parsiranje brojeva iz stringa (w12 -> 12)
  )
