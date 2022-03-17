"""
Nicholas Nguyen
Infinite Dungeon
highScore.py

File to handle writing and reading high scores
"""
from pathlib import Path
import csv
import pandas as pd


def getHighScores():
    """Function to read from the highScore.txt file"""
    # https://www.analyticsvidhya.com/blog/2021/08/python-tutorial-working-with-csv-file-for-data-science/
    path = Path("resources")
    fileToOpen = path / "highScore.csv"
    f = pd.read_csv(fileToOpen)
    f.sort_values(["Score"], 0, [False], True)
    """
    f = open(fileToOpen)
    csvReader = csv.reader(f)
    header = []
    header = next(csvReader)
    rows = []
    for row in csvReader:
        rows.append(row)
    """
    return f
