# def one_dict(list_dict):
#     keys=list_dict[0].keys()                #extract keys from list 
#     out_dict={key:[] for key in keys}               #initialize output dictionary with empty list for the keys 
#     for dict_ in list_dict:         #Iterate over each dictionary in the list 
#         for key, value in dict_.items():                #iterate over key value pairs in the current dictionary         
#             out_dict[key].append(value)                 #append values to corresponding list of output dictionaries 
#     return out_dict


from nba_api.stats.static import teams
from nba_api.stats.endpoints import leaguegamefinder
import pandas as pd
import matplotlib.pyplot as plt

def one_dict(list_dict):
    # If the list is empty, return an empty dictionary
    if not list_dict:
        return {}
    
    # Collect all keys from all dictionaries
    all_keys = set()
    for dict_ in list_dict:
        all_keys.update(dict_.keys())
    
    # Initialize the output dictionary with empty lists for each key
    out_dict = {key: [] for key in all_keys}
    
    # Populate the output dictionary
    for dict_ in list_dict:
        for key in all_keys:
            # Append the value if the key exists in the current dictionary, otherwise append None
            out_dict[key].append(dict_.get(key, None))
    
    return out_dict

# Get the list of NBA teams
nba_teams = teams.get_teams()

# Show the first three elements of the list
print(nba_teams[0:3])

# Convert the list of dictionaries to a dictionary of lists using the one_dict function
dict_nba_team = one_dict(nba_teams)

# Create a DataFrame from the dictionary
df_teams = pd.DataFrame(dict_nba_team)

# Display the first few rows of the DataFrame
print(df_teams.head())

# Filter the DataFrame to find the row corresponding to the Golden State Warriors
df_warriors = df_teams[df_teams['nickname'] == 'Warriors']
print(df_warriors)

# Extract the team ID for the Warriors
id_warriors = df_warriors[['id']].values[0][0]
print(f"Warriors Team ID: {id_warriors}")

# Request game information for the Warriors using their team ID
gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable=id_warriors)

# Retrieve the JSON data
game_data_json = gamefinder.get_json()
# print(game_data_json)

# Convert the game data to a DataFrame
games = gamefinder.get_data_frames()[0]

# Display the first few rows of the games DataFrame
print(games.head())


import requests

filename = "https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%205/Labs/Golden_State.pkl"

# download the dataframe from the API call for Golden State
def download(url, filename):                            #takes a URL and a filename as parameters
    response = requests.get(url)                            #send http get request to the url                         
    if response.status_code == 200:                         #If the request is successful (status_code == 200), it writes the content to a file in binary mode ("wb")                    
        with open(filename, "wb") as f:
            f.write(response.content)

# download data from url
download(filename, "Golden_State.pkl")


file_name = "Golden_State.pkl"
games = pd.read_pickle(file_name)
games.head()


file_name = "Golden_State.pkl"
games = pd.read_pickle(file_name)
games.head()

# create two dataframes, one for the games that the Warriors faced the raptors at home, and the second for away games
games_home=games[games['MATCHUP']=='GSW vs. TOR']
games_away=games[games['MATCHUP']=='GSW @ TOR']

# We can calculate the mean for the column PLUS_MINUS for the dataframes games_home and  games_away:
games_home['PLUS_MINUS'].mean()

games_away['PLUS_MINUS'].mean()

# plot out the PLUS MINUS column for the dataframes games_home and  games_away
# figure and axis are created for the plot
fig, ax = plt.subplots()
# PLUS_MINUS for both home and away games is plotted against the GAME_DATE
games_away.plot(x='GAME_DATE',y='PLUS_MINUS', ax=ax)
games_home.plot(x='GAME_DATE',y='PLUS_MINUS', ax=ax)

# ax.legend(["away", "home"]) adds a legend to differentiate between home and away games.
ax.legend(["away", "home"])
# display plot 
plt.show()
