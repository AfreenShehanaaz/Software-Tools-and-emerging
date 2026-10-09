## Step 1: Raw / Messy Code (Before Principles)

# Messy code – not modular, not reusable, hard to maintain



"""
🔴 Problems:

No functions (not modular).

Can’t reuse logic elsewhere.

Hard to extend (e.g., adding min/median).

Not scalable (works only for small lists).

No error handling (reliability issue).

No comments/documentation.
"""

## Step 2: Refactored Code (With Principles)

import random
from typing import List

def generate_numbers(count: int, lower: int = 1, upper: int = 100) -> List[int]:
    """Generate a list of random integers."""
    return [random.randint(lower, upper) for _ in range(count)]

def calculate_average(numbers: List[int]) -> float:
    """Return the average of a list of numbers."""
    if not numbers:
        raise ValueError("List of numbers cannot be empty")
    return sum(numbers) / len(numbers)

def find_max(numbers: List[int]) -> int:
    """Return the maximum number from a list."""
    if not numbers:
        raise ValueError("List of numbers cannot be empty")
    return max(numbers)

if __name__ == "__main__":
    # Example workflow (can be reused in other projects)
    nums = generate_numbers(10)
    print("Generated numbers:", nums)
    print("Average:", calculate_average(nums))
    print("Max:", find_max(nums))

"""
✅ Improvements:

Modularity: Code broken into functions.

Reusability: Functions can be used in any project.

Maintainability: Easy to add min/median later.

Scalability: Can handle larger datasets (just change count).

Reliability & Quality: Error handling included.

Security & Trust: Checks against empty input.

Collaboration: Docstrings/comments make it understandable for teams.
"""

import pandas as pd


def load_data(url: str) -> pd.DataFrame:
    """Load the Iris dataset from a CSV URL."""
    return pd.read_csv(url)


def calculate_average_sepal_length(df: pd.DataFrame) -> float:
    """Return the average sepal length."""
    if "sepal_length" not in df.columns:
        raise ValueError("Column 'sepal_length' not found")
    return df["sepal_length"].mean()


def find_max_petal_width(df: pd.DataFrame) -> float:
    """Return the maximum petal width."""
    if "petal_width" not in df.columns:
        raise ValueError("Column 'petal_width' not found")
    return df["petal_width"].max()


def filter_setosa(df: pd.DataFrame) -> pd.DataFrame:
    """Return rows where species is setosa."""
    if "species" not in df.columns:
        raise ValueError("Column 'species' not found")
    return df[df["species"] == "setosa"].head()


if __name__ == "__main__":
    url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"

    data = load_data(url)

    print("Average sepal length:",calculate_average_sepal_length(data))

    print("Max petal width:",find_max_petal_width(data))

    print(filter_setosa(data))