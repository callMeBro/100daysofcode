import pandas as pd

#  create dictionary
data = {
    'name': ['Apple', 'Banana', 'Cherry', 'Date'],
    'family': ['Rosaceae', 'Musaceae', 'Rosaceae', 'Arecaceae'],
    'genus': ['Malus', 'Musa', 'Prunus', 'Phoenix']
}

# turn dict into data frame 
df2 = pd.DataFrame(data)
print(df2)

# Filtering and extracting values
cherry = df2.loc[df2["name"] == 'Cherry']
family_genus = (cherry.iloc[0]['family']), (cherry.iloc[0]['genus'])

print(family_genus)
