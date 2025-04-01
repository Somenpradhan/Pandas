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
newdf.sort_index(axis=1, ascending=False) # Sort the DataFrame by index in descending order

type(newdf[0]) # Display the type of the first column of the DataFrame
newdf2 = newdf # Create a copy of the DataFrame
newdf2[0][0] = 9783 # Update the first element of the copy of the DataFrame
newdf # Display the original DataFrame

newdf.loc[0,0] = 654 # Update the first element of the DataFrame using loc
newdf.head(2) 

newdf.columns = list("ABCDE") # Update the columns of the DataFrame
newdf.head(2) 

newdf = newdf.drop(0, axis=1) # Drop the first column of the DataFrame
newdf = newdf.drop(0, axis=0) # Drop the first row of the DataFrame

newdf.loc[[1,2], ["C", "D"]] # Display the values of the DataFrame at the specified index and columns
newdf.loc[[1,2], :] # Display the values of the DataFrame at the specified index and all columns
newdf.loc[:, ["C", "D"]] # Display the values of the DataFrame at all index and specified 

newdf.loc[(newdf['A']<0.3)] # Display the values of the DataFrame where the value of column A is less than 0.3
newdf.loc[(newdf['A']<0.3) & (newdf['C']<0.1)] # Display the values of the DataFrame where the value of column A is less than 0.3 and column C is less than 0.1

newdf.iloc[0,4] # Display the value of the DataFrame at the specified index and column
newdf.iloc[[0,5], [1,2]] # Display the value of the DataFrame at the specified index and columns

newdf.drop(['A','C'], axis=1, inplace=True) # Drop the columns A and C from the DataFrame
newdf.reset_index() # Reset the index of the DataFrame

newdf.drop_duplicates(inplace=True) # Drop the duplicate values from the DataFrame

newdf.loc[:, ['B']] = None #(Any value you can give to it) # Set the values of the column B to None


newdf['B'].isnull() # Display the null values of the column B
newdf['B'].isnull().sum() # Display the number of null values of the column B

newdf.dropna(how = 'all', axis =1) # Drop all the columns with all null values from the DataFrame
newdf.fillna(0) # Fill the null values of the DataFrame with 0

newdf.drop_duplicates(subset=['name'], keep=True) # Drop the duplicate values from the DataFrame based on the column name and keep the first value 
newdf.info() # Print the information of the DataFrame

newdf['toy'].value_counts(dropna=False) # Display the count of the values of the column toy and include the null values
newdf['toy'].value_counts(normalize=True) # Display the count of the values of the column toy and normalize it

newdf.nonull() # Display the count of the values of the column toy and include the null values
newdf.mean() # Display the mean of the DataFrame
newdf.corr() # Display the correlation of the DataFrame
newdf.count() # Display the count of the values of the DataFrame
newdf.max() # Display the maximum of the DataFrame
newdf.median() # Display the median of the DataFrame
newdf.std() # Display the standard deviation of the DataFrame