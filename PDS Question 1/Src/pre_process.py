import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('C:\\Users\\surya\\OneDrive\\Documents\\PDS\\Assignments\\Assg1\\pds.csv')
df['BMI'] = (df['Weight']*703)/(df['Height']**2)
df.BMI = df.BMI.round(1)
df['Person'] = df.index
df.to_csv('C:\\Users\\surya\\OneDrive\\Documents\\PDS\\Assignments\\Assg1\\assg_proj\\clean_data\\processed_data.csv')
