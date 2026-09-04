import pandas as pd

df = pd.read_csv("books.csv")


def negative_value(column):
    negative_values = df[(df[column] < 0)]
    print("Negative values for the column are:", negative_values.filter(items=['title', 'author', column]))

negative_value("ratings_count")
negative_value("price")
negative_value("page_count")
negative_value("dimensions_width")
negative_value("dimensions_thickness")
negative_value("dimensions_height")

