# Write a program that reads the customer data and generates report as follows.
# - Pie chart to show Male VS Female customers
# - Pie chart to show the number of customers w.r.t age groups(<30, 30-40, 40-50, >50)
# - Bar chart to show the number of customers w.r.t amount spent(<500, 500-1000, 1001-5000, >5000)
# - Line chart to show the overall bill amount w.r.t customer numbers.

import pandas as pd
import matplotlib.pyplot as plt


file_path = "April8.xlsx"
df = pd.read_excel(file_path, index_col=False)

df.columns = df.columns.str.strip()

# if 'Gender' in df.columns:
#     gender_counts = df['Gender'].value_counts()

#     labels = gender_counts.index
#     sizes = gender_counts.values
#     colors = ['skyblue', 'pink']
#     plt.figure(figsize=(8, 8))
#     plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)
#     plt.title('Male vs Female Customers')
#     plt.show()
# else:
#     print("Error: Gender column not found in the dataset")



# if 'Age' in df.columns:
#     bins = [0, 30, 40, 50, float('inf')]
#     labels = ['<30', '30-40', '40-50', '>50']
    
#     df['Age Group'] = pd.cut(df['Age'], bins=bins, labels=labels, right=False)

#     age_group_counts = df['Age Group'].value_counts().sort_index()
    
#     pie_labels = age_group_counts.index
#     pie_sizes = age_group_counts.values
#     colors = ['lightblue', 'lightgreen', 'orange', 'pink']

#     plt.figure(figsize=(8, 8))
#     plt.pie(pie_sizes, labels=pie_labels, autopct=' %1.1f%%', startangle=90, colors=colors)
#     plt.title('Number of Customers by Age Group')
#     plt.show()
# else:
#     print("Error: Age column not found in the dataset")


# if 'Amount Spent' in df.columns:
#     bins = [0, 500, 1000, 5000, float('inf')]
#     labels = ['<500', '500-1000', '1001-5000', '>5000']
    
#     df['Spending Group'] = pd.cut(df['Amount Spent'], bins=bins, labels=labels, right=False)
    
#     spending_group_counts = df['Spending Group'].value_counts().sort_index()
#     bar_labels = spending_group_counts.index
#     bar_values = spending_group_counts.values

#     plt.figure(figsize=(8, 6))
#     plt.bar(bar_labels, bar_values, color=['skyblue', 'lightgreen', 'orange', 'pink'], edgecolor='black')
#     plt.title('Number of Customers by Amount Spent')
#     plt.xlabel('Spending Group')
#     plt.ylabel('Number of Customers')
#     plt.xticks(rotation=45)
#     plt.grid(axis='y', linestyle='--', alpha=0.7)
#     plt.show()
# else:
#     print("Error: 'Amount Spent' column not found in the dataset")


