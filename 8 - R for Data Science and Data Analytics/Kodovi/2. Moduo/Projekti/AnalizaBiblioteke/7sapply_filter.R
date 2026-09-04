product1 <- list(
  name = "Bluetooth Headphones",
  price = 29.99,
  in_stock = TRUE,
  category = "Electronics",
  ratings = c(5, 4, 5, 4, 5)
)
product2 <- list(
  name = "Sports T-Shirt",
  price = 15.50,
  in_stock = FALSE,
  category = "Clothing",
  ratings = c(4, 3, 4, 5)
)
product3 <- list(
  name = "E-Book on Data Analysis",
  price = 9.99,
  in_stock = TRUE,
  category = "Books",
  ratings = c(5, 5, 4, 5, 4)
)
product4 <- list(
  name = "Smart Bracelet",
  price = 45.00,
  in_stock = TRUE,
  category = "Electronics",
  ratings = c(5, 4, 5, 5, 4)
)
product5 <- list(
  name = "Winter Jacket",
  price = 89.99,
  in_stock = FALSE,
  category = "Clothing",
  ratings = c(5, 5, 4, 4, 5)
)

products <- list(product1, product2, product3, product4, product5)

sapply(products, function(x) x$name) # Prolazi kroz elemente liste i izvlaci samo "name"

sapply(products, function(x) if (x$in_stock) x$name else NULL)
# Ako je in_stock = TRUE, vraca "name", ako je FALSE onda vraca NULL


# Korak 1: Filtriraj dostupne proizvode
available_products <- Filter(function(x) x$in_stock, products)
# Korak 2: Izvuci njihova imena
sapply(available_products, function(x) x$name)


str(products) # Prikazuju strukturu cele liste
