library(readr)
library(ggplot2)
library(dplyr)

# Koji faktori najbolje predviđaju IMDb ocenu sadržaja?

certifications <- read_csv("certifications.csv")
countries <- read_csv("countries.csv")
genres <- read_csv("genres.csv")
ratings <- read_csv("ratings.csv")
titles <- read_csv("titles.csv")

titles_genres <- titles |> left_join(genres)
titles_countries <- titles_genres |> left_join(countries)
titles_complete <- titles_countries |> left_join(ratings)

# Filtriramo drzave koje se pojavljuju bar 5 puta (zbog predikcija)
country_counts <- table(titles_complete$production_country)
valid_countries <- names(country_counts[country_counts >= 5])
titles_filtered <- titles_complete[titles_complete$production_country %in% valid_countries, ]

# Uklanjamo NA vrednosti
titles_filtered <- titles_filtered %>%
  filter(!is.na(imdb_score), 
         !is.na(genre), 
         !is.na(runtime), 
         !is.na(release_year), 
         !is.na(production_country))

# Definisanje train i test
set.seed(123)
n <- nrow(titles_filtered)
train_index <- sample(1:n, size = n * 0.8)
train_data <- titles_filtered[train_index, ]
test_data <- titles_filtered[-train_index, ]

# Definisanje modela
model <-  lm(imdb_score ~ genre + runtime + release_year + production_country, data = train_data)
summary(model)

# Predikcije
predictions <- predict(model, newdata = test_data)

# Razlika predikcija i stvarnih vrednosti
actuals <- test_data$imdb_score
mae <- mean(abs(predictions - actuals))
mae

# Nove predikcije
new_data <- data.frame(
  genre = c("drama", "comedy", "action"),
  runtime = c(100, 85, 120),
  release_year = c(2025, 2024, 2023),
  production_country = c("US", "IN", "FR")
)

predict(model, newdata = new_data) # Predvidjene ocene su 6.3, 6.2 i 5.95

# Crtanje grafika

ggplot(titles_filtered, 
       aes(x = genre, 
           y = imdb_score)) +
  geom_boxplot(fill = "lightblue", outlier.color = "red", outlier.alpha = 0.5) +
  labs(title = "Distribution of IMDb Scores by Genre",
       x = "Genre",
       y = "IMDb Score") +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))


results <- data.frame(
  actual = actuals,
  predicted = predictions
)

ggplot(results, 
       aes(x = actual, 
           y = predicted)) +
  geom_point(alpha = 0.6, color = "navyblue") +
  geom_abline(linewidth = 1, color = "red") +
  labs(title = "Predicted vs Actual IMDb Scores",
       x = "Actual Score",
       y = "Predicted Score") +
  theme_minimal()

