library(ggplot2)
library(readr)
library(dplyr)

users <- read_csv("library_books_read.csv")

# Definisanje podataka za treniranje i za test
set.seed(123)
n <- nrow(users)
train_index <- sample(1:n, size = n * 0.8)
train_data <- users[train_index, ]
test_data <- users[-train_index, ]

# Definisanje modela i predikcija
model <- lm(books_read ~ member_age + membership_years, data = train_data)
predictions <- predict(model, newdata = test_data)

# Provera modela
summary(model) # Mala pozitivna povezanost sa godinama - pozitivna povezanost sa duzinom clanstva (R = 82%)

# Racunanje prosecnog odstupanja modela
actuals <- test_data$books_read
mae <- mean(abs(predictions - actuals)) # mae = 3.48

# Crtanje grafika
ggplot(data = users, 
       aes(x = books_read,
           y = membership_years,
           color = member_age)) +
  geom_point(alpha = 0.6) +
  geom_smooth(method = "lm", se = FALSE, color="royalblue", linewidth=1.1) +
  scale_color_gradient(low = "beige", high = "red") +
  labs(title = "Do Age and Membership Affect Reading Habits?",
       x = "Number of read books",
       y = "Membership years",
       color = "Age") +
  theme_minimal()

# Definisanje novih clanova
novi_clanovi <- data.frame(
  member_age = c(18, 25, 40, 60),
  membership_years = c(1, 3, 5, 7)
)

# Predvidjamo broj procitanih knjiga za nove clanove
predikcije <- predict(model, newdata = novi_clanovi)
rezultati <- cbind(novi_clanovi, books_predicted = round(predikcije))
head(rezultati)

write_csv(rezultati, "predictions.csv")
