import seaborn as seaborn
seaborn.boxplot(x="gender",y="Scores Of Mathematics",data=Students_Performance_data)
plt.title("Gender based math scores")	
plt.show()
