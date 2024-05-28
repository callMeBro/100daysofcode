import pandas as pd
import runpandas as rpd
import warnings

# suppress warnings for cleaner output.
warnings.filterwarnings('ignore')

# runpandas.get_events to fetch events related to Berlin
results = rpd.get_events('Berlin')
print(results)

berlin_result = results[0]
print('Event type', berlin_result.run_type)
print('Country', berlin_result.country)
print('Year', berlin_result.edition)
print('Name', berlin_result.summary)

#loading the race data into a RaceData Dataframe
race_result = berlin_result.load()
print(race_result)

print('Total participants', race_result.total_participants)
print('Total finishers', race_result.total_finishers)
print('Total Non-Finishers', race_result.total_nonfinishers)


# note: 
# The $home/punpandas folder likely appears due to the behavior of the runpandas library.
# When you run certain operations or load data using runpandas, it may create temporary files 
# or cache data for performance reasons. These files might be stored in a default directory, such as $home/punpandas, or a directory specified by the library.