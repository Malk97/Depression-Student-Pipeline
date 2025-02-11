

def encoder_ver(data):
    gender_map = {'Male': 1, 'Female': 0}
    # Apply mapping
    data['Gender'] = data['Gender'].map(gender_map)

    Sleep_Duration_map = {'Less than 5 hours': 1, '7-8 hours': 2, '5-6 hours': 3, 'More than 8 hours': 4, 'Others': 1}
    # Apply mapping
    data['Sleep_Duration'] = data['Sleep_Duration'].map(Sleep_Duration_map)

    Family_History_Mental_Illness_map = {'No': 0, 'Yes': 1}
    # Apply mapping
    data['Family_History_Mental_Illness'] = data['Family_History_Mental_Illness'].map(Family_History_Mental_Illness_map)

    Suicidal_Thoughts_map = {'No': 0, 'Yes': 1}
    # Apply mapping
    data['Suicidal_Thoughts'] = data['Suicidal_Thoughts'].map(Suicidal_Thoughts_map)



    # Given data with frequency
    category_counts = {
        "Class 12": 6080, "B.Ed": 1867, "B.Com": 1506, "B.Arch": 1478, "BCA": 1433, "MSc": 1190, "B.Tech": 1152,
        "MCA": 1044, "M.Tech": 1022, "BHM": 925, "BSc": 888, "M.Ed": 821, "B.Pharm": 810, "M.Com": 734,
        "MBBS": 696, "BBA": 696, "LLB": 671, "BE": 613, "BA": 600, "M.Pharm": 582, "MD": 572, "MBA": 562,
        "MA": 544, "PhD": 522, "LLM": 482, "MHM": 191, "ME": 185, "Others": 35
    }

    data['Degree'] = data['Degree'].map(category_counts)


    Dietary_Habits_map = {
        'Unhealthy': 1,  # Least healthy
        'Moderate': 2,   # In between
        'Healthy': 3,    # Most healthy
        'Others': 1      # Undefined category
    }

    # Apply mapping
    data['Dietary_Habits'] = data['Dietary_Habits'].map(Dietary_Habits_map)


    city_counts = {
        "Kalyan": 1573, "Srinagar": 1374, "Hyderabad": 1340, "Vasai-Virar": 1291, "Lucknow": 1156,
        "Thane": 1142, "Ludhiana": 1113, "Agra": 1095, "Surat": 1078, "Kolkata": 1067, "Jaipur": 1037,
        "Patna": 1009, "Visakhapatnam": 971, "Pune": 968, "Ahmedabad": 951, "Bhopal": 935, "Chennai": 886,
        "Meerut": 825, "Rajkot": 816, "Delhi": 769, "Bangalore": 768, "Ghaziabad": 745, "Mumbai": 699,
        "Vadodara": 694, "Indore": 644, "Kanpur": 609, "Nashik": 547, "Faridabad": 462, "Nagpur": 456,'others': 1,"Varanasi":685
    }

    data['City'] = data['City'].map(city_counts)

    #drop column
    data = data.drop(columns=['Profession'])


    return data
