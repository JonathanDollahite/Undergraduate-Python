import json
import requests

# Retrieves the player roster for the Baltimore Orioles (team_id=121)
r = requests.get(url="http://lookup-service-prod.mlb.com/json/named.roster_team_alltime.bam?start_season=2018&end_season=2019&team_id=121")
data = r.json()

# YOUR CODE HERE -- Print out all player names on the Orioles.
data = data['roster_team_alltime']
data = data['queryResults']
rows = data['row']
print('The Baltimore Orioles:')
for row in rows:
    if row['team_id'] == '121':
        print(row['name_first_last'])
