from randomuser import RandomUser
import pandas as pd
import requests
import json


# r = RandomUser()

# some_list = r.generate_users(10)

# name = r.get_full_name()

# for user in some_list:
#     print (user.get_full_name()," ",user.get_email())
    
    
    
# #generate a table with information about the users
# def get_users():
#     users =[]
     
#     for user in RandomUser.generate_users(10):
#         users.append({"Name":user.get_full_name(),"Gender":user.get_gender(),"City":user.get_city(),"State":user.get_state(),"Email":user.get_email(), "DOB":user.get_dob(),"Picture":user.get_picture()})
      
#     return pd.DataFrame(users)     

# df1 = pd.DataFrame(get_users())  






# data = requests.get("https://fruityvice.com/api/fruit/all")

# results = json.loads(data.text)
# pd.DataFrame(results)

# # The result is in a nested json format. The 'nutrition' column contains multiple subcolumns, so the data needs to be 'flattened' or normalized.
# df2 = pd.json_normalize(results)

# print(df2)

# # Write your code here

# # get the banana row
# # "name" column is compared to the string 'Banana' and selects the banana row 
# banana = df2.loc[df2["name"] == 'Banana']

# # cals = banana.iloc[0]['nutritions.calories']
# # print(cals)

# cals = banana.at[banana.index[0], 'nutritions.calories']
# print(cals)



# joke = requests.get("https://official-joke-api.appspot.com/jokes/ten")
# print(joke.json.loads())


joke_response = requests.get("https://official-joke-api.appspot.com/jokes/ten")
joke_data = joke_response.json()

# Now you can work with the joke_data
print(joke_data)


df = pd.DataFrame.from_dict(joke_data)

print(df)