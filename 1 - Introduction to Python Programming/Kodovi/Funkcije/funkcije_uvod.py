def odluka_za_oblacenje(x):
    if x == "kiša":
        return "Ponesi kišobran!"
    elif x == "sunce":
        return "Stavi naočare za sunce!"
    else:
        return "Oblačno je, ali ne treba ništa specijalno."

trenutno_vreme = "sunce"
preporuka = odluka_za_oblacenje(trenutno_vreme)
print(preporuka)
