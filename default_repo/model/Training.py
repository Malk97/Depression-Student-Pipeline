import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score


def randomforestmodel(data):
    X_train, X_test, y_train, y_test = data
    # Define model and hyperparameter grid
    param_grid = {
        "n_estimators": [50, 100, 150],
        "max_depth": [5, 10, 15],
        "min_samples_split": [2, 5, 10]
    }

    # Initialize the classifier
    rf = RandomForestClassifier(random_state=42)

    # Grid search for hyperparameter tuning
    grid_search = GridSearchCV(rf, param_grid, cv=3, scoring="accuracy", n_jobs=-1)
    grid_search.fit(X_train, y_train)

    # Get best model and predictions
    best_model = grid_search.best_estimator_

   
    return  best_model
