from randomuser import RandomUser 
import pandas as pd


# create random user object 
r = RandomUser()

#then using generate_users() function we get a list of random 10 users 
some_list = r.generate_users(10)


# get user details
user_data = []              #create list
for user in some_list:
    # put user info on dict
    user_info = {
        'Full Name': user.get_full_name(),
        'Gender': user.get_gender(),
        'City': user.get_city(),
        'State': user.get_state(),
        'Email': user.get_email()
    }
    user_data.append(user_info)             #append user info to the list 

# craete a dataframe
user_table = pd.DataFrame(user_data)
print(user_table)
    
#function to geenerate usernames 
def gen_random_user(num_users):
    some_list = r.generate_users(num_users)
    for user in some_list:
        print(user.get_Full_name())           
        
                      
    
   
    
    
    
    
    
    
