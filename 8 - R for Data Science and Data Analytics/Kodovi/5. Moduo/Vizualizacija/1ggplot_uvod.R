library(nycflights13)  # podaci o letovima
library(ggplot2)       # crtanje grafikona
library(gapminder)     # podaci o državama
library(dplyr)

gapminder_2007 <- filter(gapminder, year == 2007) # Filtracija

# data = ...	koji skup podataka koristiš
# aes(...)	koje varijable mapiraš i na šta
# geom_*()	kako prikazuješ podatke (tačke, linije)
# +	dodaješ slojeve kao u rečenici

ggplot(data = gapminder_2007, aes(x = gdpPercap,
                           y = lifeExp,
                           size = pop,
                           color = continent)) +
  geom_point(alpha=0.7) +
  scale_x_log10() +
  labs(title = "lifeExp vs BDP (2007)",
       x = "BDP (log)",
       y = "lifeEXP (years)",
       size = "Population",
       color = "Continent")

# alpha=0.7 - prozirnost tacaka (0.7 = 70% opacity)
# scale_x_log10() - ova funkcija transformiše x osu (gdpPercap) u logaritam po bazi 10
