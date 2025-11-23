import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the data
csv_path = "bestsellers.csv"  # make sure the name matches your file
df = pd.read_csv(csv_path)

# 2. Quick look at the data
print("First 5 rows:")
print(df.head(), "\n")

print("Info:")
print(df.info(), "\n")

print("Summary statistics for numeric columns:")
print(df.describe(), "\n")

# Example: make sure Year is integer
if "Year" in df.columns:
    df["Year"] = df["Year"].astype(int)

# Example: ensure Reviews is integer
if "Reviews" in df.columns:
    df["Reviews"] = df["Reviews"].astype(int)

# Example: ensure User Rating is float
if "User Rating" in df.columns:
    df["User Rating"] = df["User Rating"].astype(float)

print("Data types after cleaning:")
print(df.dtypes, "\n")

print("Top 10 authors by number of bestsellers:")
if "Author" in df.columns:
    author_counts = df["Author"].value_counts().head(10)
    print(author_counts, "\n")

    # Plot
    author_counts.plot(kind="bar")
    plt.title("Top 10 Authors by Number of Bestselling Books")
    plt.xlabel("Author")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.show()
else:
    print("No 'Author' column found.\n")

print("Rating statistics:")
if "User Rating" in df.columns:
    print(df["User Rating"].describe(), "\n")

    plt.hist(df["User Rating"], bins=10, edgecolor='black')
    plt.title("Distribution of User Ratings")
    plt.xlabel("Rating")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.show()
else:
    print("No 'User Rating' column found.\n")

print("Correlation between rating and reviews:")
if "User Rating" in df.columns and "Reviews" in df.columns:
    correlation = df["User Rating"].corr(df["Reviews"])
    print(f"Correlation: {correlation:.3f}\n")

    plt.scatter(df["Reviews"], df["User Rating"])
    plt.title("User Rating vs Number of Reviews")
    plt.xlabel("Number of Reviews")
    plt.ylabel("User Rating")
    plt.tight_layout()
    plt.show()
else:
    print("Need both 'User Rating' and 'Reviews' columns.\n")

if "Genre" in df.columns and "User Rating" in df.columns:
    print("Average rating by genre:")
    genre_rating = df.groupby("Genre")["User Rating"].mean()
    print(genre_rating, "\n")

    genre_rating.plot(kind="bar")
    plt.title("Average User Rating by Genre")
    plt.xlabel("Genre")
    plt.ylabel("Average Rating")
    plt.ylim(0, 5)  # because ratings are usually 0-5
    plt.tight_layout()
    plt.show()
else:
    print("Need 'Genre' and 'User Rating' columns for genre analysis.\n")

if "Year" in df.columns:
    print("Number of bestsellers per year:")
    books_per_year = df["Year"].value_counts().sort_index()
    print(books_per_year, "\n")

    books_per_year.plot(kind="line", marker="o")
    plt.title("Number of Bestsellers per Year")
    plt.xlabel("Year")
    plt.ylabel("Count of Bestsellers")
    plt.tight_layout()
    plt.show()
else:
    print("No 'Year' column found for trend analysis.\n")
