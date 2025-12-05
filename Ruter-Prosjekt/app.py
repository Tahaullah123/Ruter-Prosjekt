from flask import Flask, render_template
import requests
from datetime import datetime

app = Flask(__name__)

StasjonID = ["'Holmlia', '59636'"]

 



@app.route("/")
def index():
    url = "https://api.entur.io/journey-planner/v3/graphql"
    headers = {
        "Content-Type": "application/json",
        "ET-Client-Name": "tahaullah-journeyplanner"
    }

    query = """
      {
        stopPlace(id: "NSR:StopPlace:59636") {
          name,
          estimatedCalls(numberOfDepartures: 25) {
            realtime,
            aimedDepartureTime,
            expectedDepartureTime,
            destinationDisplay { frontText },
            serviceJourney {
              journeyPattern {
                line {
                  publicCode,
                  name,
                  transportMode
                },
              },
            },
          },
        },
      }"""
      
    

    response = requests.post(url, headers=headers, json={"query": query})
    data = response.json()

    stop = data["data"]["stopPlace"]["name"]
    departures_raw = data["data"]["stopPlace"]["estimatedCalls"]


    departures = []
    for d in departures_raw:
        departures.append({
            "line": d["serviceJourney"]["journeyPattern"]["line"]["publicCode"],
            "line_name": d["serviceJourney"]["journeyPattern"]["line"]["name"],
            "destination": d["destinationDisplay"]["frontText"],
            "expected":  datetime.fromisoformat(d["expectedDepartureTime"]).strftime("%H:%M"),
            "aimed": datetime.fromisoformat(d["aimedDepartureTime"]).strftime("%H:%M"),
            "realtime": d["realtime"]
        })
        
   

    return render_template("index.html", stop=stop, departures=departures)
  
  
   


# def format_output(): #makes dates'n'shit look nice


if __name__ == "__main__":
    app.run(debug=True)

# Stajon ID
# Holmlia: 59636
# Grorud: 58216

