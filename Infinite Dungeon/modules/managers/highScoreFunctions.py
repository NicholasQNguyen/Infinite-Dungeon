"""
Nicholas Nguyen
Infinite Dungeon
highScoreFunctions.py

File to handle writing and reading high scores
"""
from pathlib import Path
import pandas as pd


def getHighScores():
    """Function to read from the highScore.txt file"""
    # https://www.analyticsvidhya.com/blog/2021/08/python-tutorial-working-with-csv-file-for-data-science/
    # https://www.geeksforgeeks.org/how-to-sort-data-by-column-in-a-csv-file-in-python/
    path = Path("resources")
    fileToOpen = path / "highScore.csv"
    data = pd.read_csv(fileToOpen)
    data.sort_values(["Score"], axis=0, ascending=[False], inplace=True)
    print(data)
    return data.values.tolist()


def checkIfHighScore(listOfScores, newScore):
    """Checks if an inputted score would be a high score (Top 10)"""
    for i in range(10):
        # Look at the scores
        currentScore = listOfScores[i][1]
        if newScore > currentScore:
            listOfScores.insert(i, newScore)
            return listOfScores
    # If no high score, just return False
    return False

def writeToCSV(listOfScores):
    listOfScores.insert(0, ["Name", "Score"])
    dataFrame = pd.DataFrame(listOfScores)
    path = Path("resources")
    fileToWrite = path / "highScore.csv"
    dataFrame.to_csv(fileToWrite, index=False,header=False)
    listOfScores.pop(0)
