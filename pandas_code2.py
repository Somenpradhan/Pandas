import pandas as pd

dict1 = {"DAY": ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN'],
         "MIN TEMP": [22, 21, 20, 20, 23, 25, 25],
         "MAX TEMP": [33, 35, 34, 35,38, 40, 42]
        }
df = pd.DataFrame(dict1)
print(df)


df.to_excel("week.xlsx", index=False)