library(readr)
library(tidyverse)
cms_patient_experience <- read_csv("4cms_patient_experience.csv")

cms_wider <- cms_patient_experience |> pivot_wider(
    id_cols = starts_with("org"),
    names_from = measure_cd,
    values_from = prf_rate
)

# id_cols = starts_with("org")
# Tako R zna koji redovi pripadaju istoj organizaciji – koristi kolone koje počinju sa org kao identifikatore.

# names_from = measure_cd
# Iz ove kolone se prave nazivi novih kolona. Znači, svaka mera ankete postaje posebna kolona.

# values_from = prf_rate
# Ove vrednosti (ocene) idu u te nove kolone – znači, ovo je ono što želimo da rasporedimo.

count(cms_patient_experience) # Koliko redova ima dataset
unique(cms_patient_experience$org_nm) # Koliko unikatnih imena organizacija (69)
