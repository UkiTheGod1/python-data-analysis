library(readr)
library(dplyr)
library(ggplot2)

rentals <- read_csv("user_rentals_clean.csv")

rentals <- rentals |> mutate(returned_late = as.factor(returned_late))

set.seed(123)
n <-  nrow(rentals)
train_index <- sample(1:n, size = n * 0.8)
train_data <- rentals[train_index, ]
test_data <- rentals[-train_index, ]

model <- glm(returned_late ~ days_borrowed + genre + user_age + city, 
             data = train_data,
             family = binomial)
summary(model)

probabilities <- predict(model, newdata = test_data, type = "response")
test_data$class <- ifelse(probabilities > 0.5, "yes", "no")

table(Predicted = test_data$class, Actual = test_data$returned_late)

test_data$predicited_class <- ifelse(test_data$class=="yes", 1, 0)
mean(test_data$predicited_class == test_data$returned_late)



x_vals <- seq(min(rentals$days_borrowed), max(rentals$days_borrowed), length.out = 100)
boundary <- data.frame(
  days_borrowed = x_vals,
  user_age = -(coef(model)[1] + coef(model)[2] * x_vals) / coef(model)[3]
)


# Plot
ggplot(rentals, aes(x = days_borrowed, y = user_age, color = returned_late)) +
  
  geom_point(alpha = 0.7) +
  
  # geom_line(data = boundary, aes(x = days_borrowed, y = user_age), color = "black", linetype = "dashed") +
  
  labs(
    
    title = "Who Returns Books Late?",
    
    x = "Days Borrowed",
    
    y = "User Age",
    
    color = "Returned Late"
    
  ) +
  
  theme_minimal()

novi_korisnik <- data.frame(
  days_borrowed = 18,
  genre = "Mystery",
  user_age = 26,
  city = "Hillview"
)

verovatnoca <- predict(model, newdata = novi_korisnik, type = "response")
ifelse(verovatnoca > 0.5, "Kasnice", "Nece Kasniti")