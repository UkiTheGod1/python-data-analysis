import pandas as pd
import numpy as np
import difflib
def convert_to_numeric(df):
    df['times_borrowed'] = df['times_borrowed'].astype('Int32')
    df['page_count'] = df['page_count'].astype('Int32')
    df['total_copies'] = pd.to_numeric(df['total_copies'], errors='coerce')
    df['total_copies'] = df['total_copies'].astype('Int16')
    df['year_published'] = pd.to_numeric(df['year_published'], errors='coerce')
    df['year_published'] = df['year_published'].astype('Int16')
    return df
def convert_to_datetime(df):
    df['last_borrowed_date'] = pd.to_datetime(
        df['last_borrowed_date'], format='%d_%b_%y', errors='coerce')
    return df
def convert_to_category(df):
    df['genre'] = df['genre'].astype('category')
    df['section'] = df['section'].astype('category')
    df['language'] = df['language'].astype('category')
    return df

def parse_rating(text):
    if pd.isna(text) or str(text).strip().lower() == "no rating available":
        return np.nan
     
    parts = str(text).split()
     
    try:
        return float(parts[0])
    except (ValueError, IndexError):
        return np.nan
    
def parse_ratings_counts(text):
    if pd.isna(text) or str(text).strip().lower() == "no reviews":
        return np.nan
    
    parts = str(text).split()

    try:
        return int(parts[0])
    except (ValueError, IndexError):
        return np.nan
    
def parse_price(text):
    if pd.isna(text) or str(text).strip().lower() == "price not available":
        return np.nan
    try:
        price_str = str(text).replace('$', '').strip()
        return float(price_str)
    except ValueError:
        return np.nan
    
def extract_numerical_values(df):
    df['rating'] = df['rating'].apply(parse_rating)
    df['ratings_count'] = df['ratings_count'].apply(parse_ratings_counts)
    df['price'] = df['price'].apply(parse_price)
    return df

def extract_dimensions(df):
    df[['dimensions_width', 'dimensions_thickness', 'dimensions_height']] = df['dimensions'].str.replace("inches", "").str.replace(" ", "").str.split('x', expand=True).astype(float)
    return df.drop('dimensions', axis=1)

def extract_catalog(df):
    df[['catalog_shelf', 'catalog_row', 'catalog_number']] = df['catalog_position'].str.split("-", expand=True)
    return df

def data_standarization(df):
    mapping = {
        'eng': 'en',
        'En': 'en',
        "pt-BR": "br",
        "zh-CN": "cn"
    }
 
    df['language'] = df['language'].astype(object).replace(mapping).astype("category")

    mapping = {
        "Children's": "Children",
        "Children's Fiction": "Children",
        "Young Adult (YA)": "Young Adult"
    }

    df["section"] = df["section"].astype(object).replace(mapping).astype("category")

    mapping = {
        'Lev Tolstoy': 'Leo Tolstoy',
        'Winston S. Churchill': 'Winston Churchill',
        'Plato': 'Platon',
        'Will Shakespeare': 'William Shakespeare'
    }
 
    df['author'] = df['author'].replace(mapping)

    mapping = {
        "Classic": "Classics",
        "Classic Literature": "Classics",
        "Novel": "Novels",
        "Religion, Spirituality": "Religion & Spirituality",
        "Spirituality": "Religion & Spirituality",
        "Historical": "History",
        "Religious Fiction": "Religion & Spirituality",
        "Religion": "Religion & Spirituality",
        "Utopian Fiction": "Utopian",
        "Utopian Literature": "Utopian",
        "Natural History": "History",
        "Children's Stories": "Children's Fiction",
        "Children's Literature": "Children's Fiction",
        "Music/Songbooks": "Music",
        "Epic Poetry": "Poetry"
    }
    
    df['genre'] = df['genre'].astype(object).replace(mapping).astype("category")
    return df
def prepare_data(df):
    return df.pipe(convert_to_numeric).pipe(convert_to_datetime).pipe(convert_to_category).pipe(extract_numerical_values).pipe(extract_dimensions).pipe(
        extract_catalog).pipe(data_standarization)

# import pandas as pd
# from preprocessing import prepare_data
# data = pd.read_csv('books.csv')
# df = prepare_data(data) Automatski sve kolone pretvara u ispravan tip podataka