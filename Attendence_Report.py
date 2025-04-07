# Show the program of the course
# Prepare an attendence report
# you have to plot all the data from the excel file in the pie chart in the excel file name book1.xlsx file
# Print the date in the x axis and the present and absent values in y axis.

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("Book1.xlsx", index_col=False)

df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df = df.dropna(subset=['Date'])

plt.plot(df['Date'], df['Lession'], marker='o')
plt.show()
