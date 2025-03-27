import pandas as pd

friend1 = {"name": "Somen", "age": 21}
df = pd.DataFrame([friend1])
print(df)

friend2 = {"name": ["Anjali","Rahul"], "age": [23,24]}
ndf = pd.DataFrame(friend2)
print(ndf)

df = pd.concat([df,ndf], ignore_index= True)
print(df)

df.loc[1] = {"name": "Sasa", "age": 22}
print(df)

df["status"] = ["bf" if age > 22 else "nbf" for age in df["age"]]
print(df)

df["MailId"] = ["abc@gmai.com", "xyz@gmail.com", "xyz@gmail.com"]
print(df)
df.to_csv("mail.csv")