library(DBI)
library(RMySQL)

con <- dbConnect(
  RMySQL::MySQL(),
  dbname = "library",
  host = "localhost",
  user = "root",
  password = "DbSb3272GlObEaBb")
  
dbIsValid(con)