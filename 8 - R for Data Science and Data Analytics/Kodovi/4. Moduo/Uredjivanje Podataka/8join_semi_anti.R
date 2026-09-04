library(nycflights13)
library(tidyverse)

flights2 <- flights |>   select(year, time_hour, origin, dest, tailnum, carrier)

airports |> left_join(flights2, join_by(faa == origin))

airports |> semi_join(flights2, join_by(faa == origin))

# semi_join(x, y) ➝ zadrži redove iz x koji imaju poklapanje u y;
# ne dodaje kolone iz y;
# ne menja strukturu – samo filtrira.

flights2 |> anti_join(planes, join_by(tailnum))

# anti_join() radi suprotno od semi_join():
# zadržava redove iz x koji nemaju poklapanje u y;
# koristi se kada tražiš izuzetke, rupe, nedostatke.