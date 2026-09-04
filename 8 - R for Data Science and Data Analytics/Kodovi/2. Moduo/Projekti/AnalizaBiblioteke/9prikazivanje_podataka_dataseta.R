library(nycflights13)  # Data on flights from New York – test data frame
library(dplyr)  # Favorite tools for data manipulation and filtering
library(knitr)  # To display results in a neat and readable format

glimpse(flights) # Pregled dataseta
View(flights) # Ceo dataset kao sheet
head(flights) # Prvi redovi
tail(flights) # Poslednji redovi

flights$flight # Pristupamo jednoj koloni dataseta

?flights # Prikazuje informacije dataseta dole desno u "help"