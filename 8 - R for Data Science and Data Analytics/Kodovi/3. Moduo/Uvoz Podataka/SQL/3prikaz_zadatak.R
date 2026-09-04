library(dplyr)
library(knitr)
library(DBI)
library(RMySQL)

# Konetujes se na bazu

dbListTables(con)

dbListFields(con, "rental")

query_book <- dbGetQuery(con, "SELECT * FROM book LIMIT 5")
glimpse(query_book)
query_author <- dbGetQuery(con, "SELECT * FROM author LIMIT 5")
glimpse(query_author)
query_city <- dbGetQuery(con, "SELECT * FROM city LIMIT 5")
glimpse(query_city)
query_genre <- dbGetQuery(con, "SELECT * FROM genre LIMIT 5")
glimpse(query_genre)
query_rental <- dbGetQuery(con, "SELECT * FROM rental LIMIT 5")
glimpse(query_rental)
query_user <- dbGetQuery(con, "SELECT * FROM user LIMIT 5")
glimpse(query_user)