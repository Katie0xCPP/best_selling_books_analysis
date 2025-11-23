Best-Selling Books Data Analysis

A Python data analysis project that explores best-selling books to uncover trends in authors, genres, ratings, and yearly patterns.

Overview

This project analyzes a dataset of best-selling books using pandas for data manipulation and matplotlib for visualization.
The goal is to understand patterns such as:

Which authors appear most frequently

Rating distributions and review behavior

Average ratings by genre

Trends in best-sellers across years

Correlations between ratings and review counts

Everything is reproducible in a clean VS Code environment using a virtual environment.

Project Structure
best_selling_books_analysis/
│
├── bestsellers.csv          # Dataset containing the book data
├── analyze_books.py         # Main analysis script
└── .venv/                   # Virtual environment (not uploaded to GitHub)

Technologies Used

Python 3

pandas — data loading and cleaning

matplotlib — visualizations

VS Code — development environment

Virtual Environment (.venv) — isolated package management

Features and Analysis

The analysis includes:

Dataset Loading and Inspection

Previewing rows

Checking data types

Summary statistics

Data Cleaning

Ensuring numeric types (Ratings, Reviews, Price, Year)

Handling missing or malformed rows

Author Frequency Analysis

Top 10 most common bestselling authors

Bar chart visualization

Rating Distribution

Histograms of user ratings

Summary statistics

Rating vs. Reviews Correlation

Scatter plots

Calculated correlation coefficient

Genre Analysis

Average rating per genre

Genre comparison bar chart

Bestsellers Over Time

Number of bestselling books per year

Line graph showing historical patterns

How to Run the Project

Clone or download the repository

Open the folder in VS Code

In the terminal, create and activate a virtual environment:

python -m venv .venv
.venv\Scripts\activate


Install required libraries:

pip install pandas matplotlib


Run the main analysis script:

python analyze_books.py


View results directly in the terminal and through generated plots.

Data

The dataset bestsellers.csv includes:

Name — Book title

Author

User Rating

Reviews

Price

Year (bestseller year)

Genre (Fiction / Non-Fiction)

License

This project is for educational and analytical purposes.
