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

# Filtering and extracting values -- loc methos=d is used to access group of rows and columns 
cherry = df2.loc[df2["name"] == 'Cherry']
# the iloc is user for integer location based on indexing and selects the value in the family column of the first row of the dataframe
family_genus = (cherry.iloc[0]['family']), (cherry.iloc[0]['genus'])

print(family_genus)
