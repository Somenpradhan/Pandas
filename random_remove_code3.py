# Make a list of 8 Team Leader name, randomly remove one by one using pandas.
import pandas as pd
import random
team_leaders = ['smruti', 'joti','chiranjib', 'kishor', 'janmajay', 'Somen', 'Sweeta', 'Kasturi']

df = pd.DataFrame(team_leaders, columns=['Team Leader'])

# Randomly remove one Team Leader at a time
while not df.empty:
    random_index = random.choice(df.index)
    print(f"Removing: {df.loc[random_index, 'Team Leader']}")# Print the removed Team Leader
    df = df.drop(random_index).reset_index(drop=True) # Drop the selected index
    print("Remaining Team Leaders:")
    print(df)
    print()
