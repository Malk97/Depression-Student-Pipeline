import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split


def fill_value1(data):
    valid_cities = ['Visakhapatnam', 'Bangalore', 'Srinagar', 'Varanasi', 'Jaipur',
                'Pune', 'Thane', 'Chennai', 'Nagpur', 'Nashik', 'Vadodara',
                'Kalyan', 'Rajkot', 'Ahmedabad', 'Kolkata', 'Mumbai', 'Lucknow',
                'Indore', 'Surat', 'Ludhiana', 'Bhopal', 'Meerut', 'Agra',
                'Ghaziabad', 'Hyderabad', 'Vasai-Virar', 'Kanpur', 'Patna',
                'Faridabad', 'Delhi']
    data['City'] = data['City'].apply(lambda x: x if x in valid_cities else np.nan)

    # Prepare the data
    known_data = data[data['City'].notna()]
    missing_data = data[data['City'].isna()]

    X = known_data.drop('City', axis=1)  # Features
    y = known_data['City']              # Target

    # One-hot encode categorical variables
    X_encoded = pd.get_dummies(X)
    missing_data_encoded = pd.get_dummies(missing_data.drop('City', axis=1))

    # Align the columns of both datasets
    missing_data_encoded = missing_data_encoded.reindex(columns=X_encoded.columns, fill_value=0)

    # Train a RandomForestClassifier
    model = RandomForestClassifier(random_state=42)
    model.fit(X_encoded, y)

    # Predict missing values
    data.loc[data['City'].isna(), 'City'] = model.predict(missing_data_encoded)



    return data

