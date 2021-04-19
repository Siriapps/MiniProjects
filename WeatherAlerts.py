from urllib import request
import json

def getWheatherApi(area):
    api = "https://api.weather.gov/alerts/active?area="
    api+=area
    handle = request.urlopen(api)  # opening the api url
    data = handle.read().decode()  # reading the data
    return data

def parseWeatherAlerts(data):
    js = json.loads(data)  # loading the json
    features = js["features"]
    headlines = list()
    for h in range(0, len(features)):
        headlines.append(features[h]["properties"]["headline"])
    return headlines


print("** Weather Alerts **")
area = input("Enter your area: ").upper()
data = getWheatherApi(area)
WeatherAlerts = parseWeatherAlerts(data)
[print(i) for i in WeatherAlerts]

