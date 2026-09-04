library(readr)
books <- read_csv("books.csv",  na = c("N/A", "")) # Izbacuje NA vrednosti (bice zapravo prazne)

books <- books |>
  rename(catalog_id = catalog_position) # Preimenovanje kolone


glimpse(books)

read_csv("The first line of metadata
The second line of metadata
x,y,z
1,2,3", skip = 2) # Skipuje prva dva reda


read_csv("# komentar koji ne treba da bude pročitan
x,y,z
1,2,3", comment = "#")


read_csv("1,2,3
4,5,6", col_names = FALSE) # Imenuje kolone (X1, X2...)


# read_csv()	Kad su podaci razdvojeni zarezima
# read_csv2()	Kada su podaci razdvojeni tačkama i zarezima (;) – čest slučaj u EU Excel fajlovima
# read_tsv()	Kad su podaci razdvojeni tabulatorima
# read_delim()	Kada delimiter nije standardan – npr. - "	`read_delim("data.txt", delim = "
# read_fwf()	Za fajlove sa fiksnom širinom kolona -	read_fwf("fixed.txt", fwf_widths(c(5, 10, 3)))
# read_table()	Varijacija za razmake kao delimiter -	read_table("space_data.txt")
# read_log()	Kad analiziramo Apache log fajlove -	read_log("access.log")