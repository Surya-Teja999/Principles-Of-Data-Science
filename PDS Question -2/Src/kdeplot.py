seaborn.kdeplot(x='writing score',data=Students_Performance_data,hue='lunch',fill=True,alpha=.3)
plt.title('Writing Scores by Lunch Type')
plt.xlabel('Writing Score')
plt.show()
