library(readr)
library(dplyr)
library(ggplot2)
# lm(price ~ size) -> regresija
# glm(late ~ age, family = binomal) -> klasifikacija

apartments <- read_csv("apartment_prices.csv")

set.seed(123)

n <- nrow(apartments)

train_index <- sample(1:n, size = 0.8 * n)

train_data <- apartments[train_index, ]

test_data <- apartments[-train_index, ]

model <- lm(price_eur ~ apartment_size_m2 + floor + distance_to_center_km, data = train_data)

predictions <- predict(model, newdata = test_data)
head(predictions)

actuals <- test_data$price_eur

mae <- mean(abs(predictions - actuals))

mae

summary(model)


ggplot(data = apartments,
       aes(x = apartment_size_m2,
           y = price_eur,
           color = floor)) +
  geom_point(alpha = 0.8) +
  geom_smooth(method = "lm", se = FALSE, color="red", linewidth=1.2) +
  labs(title = "Apartment Price vs Size",
       x = "Apartment Size",
       y = "Price (EUR)",
       color = "Floor")
