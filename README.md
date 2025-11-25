# Best-Selling Books Data Analysis

A Python data analysis project that explores best-selling books to uncover trends in authors, genres, ratings, and yearly patterns.

## Overview

This project analyzes a dataset of best-selling books using pandas for data manipulation and matplotlib for visualization. The goals include identifying frequent authors, understanding rating distributions, examining genre trends, analyzing the relationship between ratings and reviews, and exploring how best-selling books change across years.

## Project Structure

best_selling_books_analysis/
│
├── bestsellers.csv          # Dataset containing the book data
├── analyze_books.py         # Main analysis script
└── .venv/                   # Virtual environment (not uploaded to GitHub)

## Technologies Used

- Python 3  
- pandas for data loading and cleaning  
- matplotlib for visualizations  
- VS Code for development  
- Virtual environment (.venv) for package isolation  

## Features and Analysis

### Dataset Loading and Inspection
- Loading the CSV file  
- Displaying initial rows  
- Showing data types and summary statistics  

### Data Cleaning
- Converting columns to numeric types  
- Removing or handling malformed rows  

### Author Frequency Analysis
- Identifying the most common bestselling authors  
- Generating bar charts  

### Rating Distribution
- Visualizing histograms of user ratings  
- Computing rating statistics  

### Rating vs. Reviews Correlation
- Creating scatter plots  
- Calculating correlation coefficients  

### Genre Analysis
- Comparing average ratings across genres  
- Visualizing results with bar charts  

### Bestsellers Over Time
- Counting bestsellers per year  
- Plotting historical trends  

## How to Run the Project

1. Clone or download this repository.
2. Open the folder in VS Code.
3. In the terminal, create and activate a virtual environment:

python -m venv .venv
.venv\Scripts\activate

4. Install the required Python libraries:

pip install pandas matplotlib

5. Run the analysis script:

python analyze_books.py

6. View results in the terminal and in the generated plots.

## Dataset

The file bestsellers.csv contains the following columns:

- Name (book title)  
- Author  
- User Rating  
- Reviews  
- Price  
- Year (bestseller year)  
- Genre (Fiction or Non-Fiction)  

## License

This project is intended for educational and analytical use.

Created using Python, pandas, and matplotlib.
