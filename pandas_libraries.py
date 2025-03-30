import numpy as np
import pandas as pd

dict1 = {"name": ['Somen', 'rohan', 'skillf', 'Anjali'],
         "marks": [81, 72, 93, 64],
         "city": ['Delhi', 'Mumbai', 'Delhi', 'Mumbai']
        }
df = pd.DataFrame(dict1)
print(df)

df.to_csv("friends.csv") # Save the DataFrame to a CSV file
df.to_csv("friends_index_false.csv", index=False) # Save the DataFrame to a CSV file without the index
df.head(2) # Display the first 2 rows of the DataFrame
df.tail(2) # Display the last 2 rows of the DataFrame
df.describe() # Display a stastic analysis and maximum of the DataFrame
somen = pd.read_csv("somen.csv") # Read the CSV file into a DataFrame
print(somen)

somen["marks"][0] = 100 # Update the marks of the first row
print(somen)

somen.index = ['first','second','third','fourth'] # Update the index of the DataFrame 
print(somen)

somen = somen.rename(columns={"marks": "percentage"}) # Rename the column "marks" to "percentage"   
print(somen)

ser = pd.Series(np.random.rand(10)) # Create a Series with random numbers
print(ser) # Display the Series
type(ser) # Display the type of the Series

newdf = pd.DataFrame(np.random.rand(334,5), index = np.arange(334)) # Create a DataFrame with random numbers
type(newdf) # Display the type of the DataFrame
newdf[0][0] = "Somen" # Display the first element of the DataFrame

newdf.head() # Display the first 5 rows of the DataFrame
newdf.tail() # Display the last 5 rows of the DataFrame
newdf.describe() # Display a stastic analysis and maximum of the DataFrame

newdf.index # Display the index of the DataFrame
newdf.columns # Display the columns of the DataFrame

newdf.to_numpy() # Display the DataFrame as a numpy array 
newdf[0][0] = 0.3 # Update the first element of the DataFrame
newdf.head() # Display the first 5 rows of the DataFrame

newdf.T # Display the transpose of the DataFrame
