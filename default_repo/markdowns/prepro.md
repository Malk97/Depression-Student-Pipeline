Here’s what you did in your data preprocessing as key points:

1- Handling Missing Values:

- Filled missing values in the Financial Stress column with the most frequent value.
- Replaced invalid cities with NaN.
- Used Random Forest Classifier to predict missing city values.

2- Data Type Conversion:

- Converted numerical categorical columns (Age, Academic Pressure, Work Pressure, etc.) to int.

3- Column Renaming:

- Renamed columns to be more readable and consistent (e.g., Academic Pressure → Academic_Pressure).

4- Encoding Categorical Variables:

- Gender Mapping: Male → 1, Female → 0.
- Sleep Duration Mapping: Different sleep categories mapped to numerical values.
- Family History of Mental Illness & Suicidal Thoughts Mapping: Yes → 1, No → 0.
- Dietary Habits Mapping: Unhealthy → 1, Moderate → 2, Healthy → 3.
- Degree & City Mapping: Converted categorical values to frequency-based numerical values.

5- Feature Engineering:

- Dropped the Profession column.
- Standardized degree names by mapping full names to shorter labels.
This process ensures a clean, structured, and machine-learning-friendly dataset. 