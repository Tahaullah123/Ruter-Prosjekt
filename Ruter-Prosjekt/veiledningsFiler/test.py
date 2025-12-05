import json
from datetime import datetime

with open('data.json', 'r') as file:
    data = json.load(file)
    
    
print(type(data))

for d in data:
            print(d["serviceJourney"]["journeyPattern"]["line"]["publicCode"])
            print(d["serviceJourney"]["journeyPattern"]["line"]["name"])
            print(d["destinationDisplay"]["frontText"])
            print(datetime.fromisoformat(d["aimedDepartureTime"]).strftime("%H:%M"))
            print(datetime.fromisoformat(d["expectedDepartureTime"]).strftime("%H:%M"))


