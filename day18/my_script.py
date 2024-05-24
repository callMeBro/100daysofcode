import pandas as pd

# store path of csv 
# csv_path = 'customers-100.csv'

# # create dataframe
# df = pd.read_csv(csv_path)

# #  display first five rows of data frame 
# df.head()

# print(df)

# # get all unique elements in the column name 
# unames = df['First Name'].unique() 

# unames = df['Country'] == 'Chile'
# filtered = df[unames]
# print(filtered)

# Create a Series from a list
# data = [10, 20, 30, 40, 50]
# s = pd.Series(data)


# print(s[2])     # Access the element with label 2 (value 30)

# print(s[2])     # Access the element with label 2 (value 30)

# print(s[2])     # Access the element with label 2 (value 30)

# print(s)


# # create dataframes from dictionaries 
# data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
#         'Age': [25, 30, 35, 28],
#         'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']}
# df = pd.DataFrame(data)
# print(df)

# print(df['Name'])  # Access the 'Name' column

# # access rows by their index using .iloc[]  
# print(df.iloc[2])   # Access the third row by position
# # access by label using .loc[]
# print(df.loc[1])    # Access the second row by label


# print(df[['Name', 'Age']])  # Select specific columns
# print(df[1:3])             # Select specific rows

# # find unique elements
# unique_dates = df['Age'].unique()

# # conditional filtering 
# high_above_102 = df[df['Age'] > 25]

# # save dataframe
# df.to_csv('trading_data.csv', index=False)

#Define a dictionary 'x'

x = {'Name': ['Rose','John', 'Jane', 'Mary'], 'ID': [1, 2, 3, 4], 'Department': ['Architect Group', 'Software Group', 'Design Team', 'Infrastructure'], 
      'Salary':[100000, 80000, 50000, 60000]}

#casting the dictionary to a DataFrame
df = pd.DataFrame(x)

#display the result df
print(df)

#Retrieving the "ID" column and assigning it to a variable x
x = df[['ID']]
print(x)

#check the type of x
type(x)

#Retrieving the Department, Salary and ID columns and assigning it to a variable z
z = df[['Department','Salary','ID']]
print(z)


##########################################################################

# Get the Student column as a series Object
x = df1['Student']
print(x)

#check the type of x
type(x)

###########################################################################################

# loc() and iloc() functions

# To slice out a set of rows, you use this syntax: data[start:stop] --- can perform slicing using both the index and the name of the column.

# When slicing in pandas, the start bound is included in the output.--- if you want to select rows 0, 1, and 2 your code would look like this: df.iloc[0:3]
# start at index 0 and select rows 0, 1, 2 up to but not including 3

# When using loc(), integers can be used, but the integers refer to the index label and not the position.
# For example, using loc() and select 1:4 will get a different result than using iloc() to select rows 1:4.


# syntax for your understanding: loc[row_label, column_label]

# Access the value on the first row and the first column
df.iloc[0, 0]


# Access the value on the first row and the third column
df.iloc[0,2]


# Access the column using the name
df.loc[0, 'Salary']



# store path of csv 
csv_path = 'customers-100.csv'

# # create dataframe
df2 = pd.read_csv(csv_path)

df2=df2.set_index("Name")


#To display the first 5 rows of new dataframe
df2.head()


#Now, let us access the column using the name
df2.loc['Jane', 'Salary']


# slicing
# if you want to select rows 0, 1, and 2 your code would look like this: df.iloc[0:3].
#  start at index 0 and select rows 0, 1, 2 up to but not including 3


#let us do the slicing using old dataframe df
df.iloc[0:2, 0:3]

#let us do the slicing using loc() function on old dataframe df where index column is having labels as 0,1,2
df.loc[0:2,'ID':'Department']


#let us do the slicing using loc() function on new dataframe df2 where index column is Name having labels: Rose, John and Jane
df2.loc['Rose':'Jane', 'ID':'Department']