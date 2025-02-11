
def convert_ty(data, *args, **kwargs):
    #full the null value for this column to convert the data type
    most_frequent_value = data['Financial Stress'].mode()[0]
    data['Financial Stress'].fillna(most_frequent_value, inplace=True)

    data['Age'] = data['Age'].astype(int)
    data['Academic Pressure'] = data['Academic Pressure'].astype(int)
    data['Work Pressure'] = data['Work Pressure'].astype(int)
    data['Study Satisfaction'] = data['Study Satisfaction'].astype(int)
    data['Job Satisfaction'] = data['Job Satisfaction'].astype(int)
    data['Financial Stress'] = data['Financial Stress'].astype(int)
    #df[''] = df[''].astype(int)    

    return data
