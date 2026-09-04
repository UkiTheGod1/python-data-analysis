library(tidyverse)

table1 <- tibble(
  
  country = c("Afghanistan", "Afghanistan", "Brazil", "Brazil", "China", "China"),
  
  year = c(1999, 2000, 1999, 2000, 1999, 2000),
  
  readers = c(745, 2666, 37737, 80488, 212258, 213766),
  
  population = c(19987071, 20595360, 172006362, 174504898, 1272915272, 1280428583)
  
)

table1 |> mutate(rate = readers / population * 10000) # Pravi novu kolonu ali ne menja tibble

table1 |> group_by(year) |> summarize(total_readers = sum(readers)) # Grupacija
