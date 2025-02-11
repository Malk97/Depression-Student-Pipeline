

def rename(data):
    # Dictionary to rename columns
    new_column_names = {
        'id': 'ID',
        'Gender': 'Gender',
        'Age': 'Age',
        'City': 'City',
        'Profession': 'Profession',
        'Academic Pressure': 'Academic_Pressure',
        'Work Pressure': 'Work_Pressure',
        'CGPA': 'CGPA',
        'Study Satisfaction': 'Study_Satisfaction',
        'Job Satisfaction': 'Job_Satisfaction',
        'Sleep Duration': 'Sleep_Duration',
        'Dietary Habits': 'Dietary_Habits',
        'Degree': 'Degree',
        'Have you ever had suicidal thoughts ?': 'Suicidal_Thoughts',
        'Work/Study Hours': 'Work_Study_Hours',
        'Financial Stress': 'Financial_Stress',
        'Family History of Mental Illness': 'Family_History_Mental_Illness',
        'Depression': 'Depression'
    }

    # Renaming the columns
    data.rename(columns=new_column_names, inplace=True)

    # Displaying the updated columns

    return data
