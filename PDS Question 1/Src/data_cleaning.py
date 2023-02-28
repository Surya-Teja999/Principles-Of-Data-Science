import pandas as pd
df = pd.read_csv('C:\\Users\\surya\\OneDrive\\Documents\\PDS\\Assignments\\Assg1\\assg_proj\\raw_data\\given_raw_data.csv')
df = df.rename(columns={"Height (Inches)": "Height", "Weight (Pounds)": "Weight"})
df.to_csv('C:\\Users\\surya\\OneDrive\\Documents\\PDS\\Assignments\\Assg1\\assg_proj\\clean_data\\cleaned_data.csv')

