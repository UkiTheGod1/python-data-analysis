library(nycflights13)  # Data on flights from New York – test data frame
library(dplyr)  # Favorite tools for data manipulation and filtering
library(knitr)  # To display results in a neat and readable format

Chicago_airports <- airports[airports$tzone == "America/Chicago",
                             c("faa","name", "lat", "lon")] # Prikazuje samo odredjene kolone
head(Chicago_airports)
