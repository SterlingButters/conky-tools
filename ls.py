import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

LECTURES_PATH = os.environ.get("LECTURES_PATH")

lectures = []
labs = []
for file in os.listdir(LECTURES_PATH):
    if file.startswith("Lecture"):
        lectures.append(file.split(".")[0])
    elif file.startswith("Lab"):
        labs.append(file.split(".")[0])

lectures.sort()
labs.sort()

if len(lectures) > len(labs):
    for a in range(len(lectures) - len(labs)):
        labs.append(" ")
else:
    for b in range(len(labs) - len(lectures)):
        lectures.append(" ")

DICT = {"Lectures": lectures, "Labs": labs}

df = pd.DataFrame(DICT)
print(df.to_string(index=False))