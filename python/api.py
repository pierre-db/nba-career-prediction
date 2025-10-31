#!/usr/bin/env python3
"""
An API to query the dataframe and make predictions
Usage:
    From project root: uvicorn python.api:app --reload
"""
from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import numpy as np
import pickle
from pathlib import Path

# Get the project root directory (parent of python/ folder)
current_dir = Path(__file__).parent
project_root = current_dir.parent

# we import our dataset to allow us to query by name
dataset = pd.read_csv(
    project_root / "data" / "nba_logreg.csv",
    usecols=['Name', 'FT%', 'AST', 'BLK', 'STL', 'FG%', 'TOV',
            'DREB', 'FTA', 'REB', 'FGA', 'FTM', 'OREB',
            'MIN', 'PTS', 'FGM', 'GP', 'TARGET_5Yrs']
)

# Remove exact duplicates and entries with duplicate names
dataset = dataset.drop_duplicates()
dataset = dataset[~dataset['Name'].duplicated(keep='last')]

# Set Name as index after cleaning
dataset = dataset.set_index('Name')
# we import our model
model = pickle.load(open(project_root / "data" / "players_classifier.pkl", 'rb'))

# we start our app
app = FastAPI()

class Input(BaseModel):
    name: str = None
    GP: int = 0
    MIN: float = 0.0
    PTS: float = 0.0
    FGM: float = 0.0
    FGA: float = 0.0
    FTM: float = 0.0
    FTA: float = 0.0
    OREB: float = 0.0
    DREB: float = 0.0
    REB: float = 0.0
    AST: float = 0.0
    STL: float = 0.0
    BLK: float = 0.0
    TOV: float = 0.0

class Output(BaseModel):
    prediction: int
    prediction_proba: float
    warnings: str = ""


@app.post("/")
def read_post(item: Input):
    if item.name:
        # if we received a name in argument we return the player's stats
        if(item.name in dataset.index):
            return dataset.loc[item.name].to_json()
        else:
            # in case the name is not in our dataset, we return a warning
            return Output(
                prediction=-1,
                prediction_proba=-1.0,
                warnings='Unknown player'
            )
    else:
        # if we received some stats we make a prediction and return our results
        X = np.array([val for key, val in item.dict().items() if key != 'name']).reshape(1, -1)
        y_pred = int(model.predict(X))
        y_pred_proba = model.predict_proba(X)[0][y_pred]

        # we generate the warnings
        warnings = ""
        for key, val in item.dict().items():
            if val == 0:
                warnings += f"Received param {key} = 0\n"

        # we generate and return the output
        return Output(
            prediction=y_pred,
            prediction_proba=y_pred_proba,
            warnings=warnings
        )
