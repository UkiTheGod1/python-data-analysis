library(dplyr)
library(knitr)
library(DBI)
library(RMySQL)

con <- dbConnect(
  RMySQL::MySQL(),
  dbname = "library",
  host = "localhost",
  user = "root",
  password = "DbSb3272GlObEaBb")

# Prikaz svih tabela u bazi:
dbListTables(con)

# Prikaz kolona u određenoj tabeli (npr. book):
dbListFields(con, "book")

# Prikaz podataka iz tabele:
books <- dbGetQuery(con, "SELECT * FROM book LIMIT 10")
glimpse(books)