proizvod_a <- list(
  naziv = "A",
  dan = c(1, 2, 3, 4, 5),
  cene = c(99, 24.50, 18.75, 22.00, 20.30),
  kolicine = c(5, 8, 4, 7, 6)
)

proizvod_b <- list(
  naziv = "B",
  dan = c(1, 2, 3, 4, 5),
  cene = c(0, 16.50, 14.75, 17.00, 15.80),
  kolicine = c(10, 9, 12, 8, 11)
)

# Stvaramo listu sa oba proizvoda
shop_data <- list(proizvod_a, proizvod_b)

# Izracunavamo prihod oba proizvoda
prihod_a <- proizvod_a$cene * proizvod_a$kolicine 
prihod_b <- proizvod_b$cene * proizvod_b$kolicine

# Trazimo maksimume prihoda
which.max(prihod_a) # Dan 1
max(prihod_a) # 495
which.max(prihod_b) # Dan 3
max(prihod_b) # 177

# Trazimo prosecnu kolicinu
mean(proizvod_a$kolicine) # 6
mean(proizvod_b$kolicine) # 10

# Dodajemo ukupne prihode u glavnu listu
shop_data[[1]]$ukupni_prihod <- sum(prihod_a)
shop_data[[2]]$ukupni_prihod <- sum(prihod_b)

# Trazimo najuspesniji proizvod
sum(prihod_a) # 1041.8 - uspesniji
sum(prihod_b) # 635.3

# Pravimo dataframe
df_a = data.frame(proizvod_a)
df_a$prihod = prihod_a
df_b = data.frame(proizvod_b)
df_b$prihod = prihod_b

df_sales = rbind(df_a, df_b)

# Izracunavanje ukupnog prihoda i prosecne ocene
tapply(df_sales$prihod, df_sales$naziv, sum) # A je veci (1041.8 > 635.3)
tapply(df_sales$cene, df_sales$naziv, mean) # A je veci (36.91 > 12.81)


# Najuspesniji proizvod je proizvod A definitivno
# Iznenadilo me jedino koliko je jednostavno bili raditi - mislio sam da je komplikovanije
# Sledeci korak - eventualno exportovati podatke u Excel ili CSV fajl

