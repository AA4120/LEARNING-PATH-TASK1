import pandas as pd
import matplotlib.pyplot as plt

#Read .CSV Data
df = pd.read_csv('Read_Data_csv/sample_1.csv')
print(df)

x = df['Month']
y = df['Average']
plt.xlabel("Month")
plt.ylabel("Average")

#pie chart
plt.pie(y, labels=x, radius=1.2,shadow =True)
plt.show()

#bar chart 
plt.bar(x,y)
plt.show()

#scatter
plt.scatter(x,y)
plt.show()


