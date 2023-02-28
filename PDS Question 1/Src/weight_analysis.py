import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('C:\\Users\\surya\\OneDrive\\Documents\\PDS\\Assignments\\Assg1\\assg_proj\\clean_data\\processed_data.csv')
plt.ylabel("Weight")
plt.title("Weight Analysis")
plt.boxplot(df.Weight)
plt.savefig('C:\\Users\\surya\\OneDrive\\Documents\\PDS\\Assignments\\Assg1\\assg_proj\\results\\weight_distribution.png')
