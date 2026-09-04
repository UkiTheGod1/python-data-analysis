product1 <- list(
  name = "Bottle",
  price = 4.99,
  in_stock = FALSE,
  category = "Utensils",
  ratings = c(5, 4, 4, 5)
)
  
product2 <- list(
  name = "Cup",
  price = 7.99,
  in_stock = TRUE,
  category = "Utensils",
  ratings = c(4, 3, 3, 2, 5)
)

products <- list(product1, product2)

products[[2]]$name
mean(products[[1]]$ratings)

product3 <- list(
  name = "Book",
  price = 9.99,
  in_stock = TRUE,
  category = "Books",
  ratings = c(5, 5, 4, 5, 4)
)

products <- append(products, list(product3))