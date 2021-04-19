from urllib import request
import json
import time


def trackTime(funcToBeDecorated):
    def timeTaken(*args):
        startTime = int(time.time() * 1000)  # milliseconds
        data = funcToBeDecorated(*args)
        endTime = int(time.time() * 1000)  # milliseconds
        print(f"Function: {funcToBeDecorated.__name__}, Time Taken: {endTime - startTime} msec")
        return data
    return timeTaken


@trackTime
def getWheatherApi():
    api = "https://api.weather.gov/gridpoints/TOP/31,80/forecast/hourly"
    handle = request.urlopen(api)  # opening the api url
    data = handle.read().decode()  # reading the data
    return data

@trackTime
def parseWeatherData(WeatherForecast):
    js = json.loads(WeatherForecast)  # loading the json
    periods = js["properties"]["periods"]
    for p in range(0, len(periods)):
        start = periods[p]["startTime"]  # getting the start time
        temp = periods[p]["temperature"]  # getting the temparature
        unit = periods[p]["temperatureUnit"]  # getting the unit of temperature
        print(f"{start[11:16]} {temp}{unit}")

data = getWheatherApi()
hourlyWeatherForecast = parseWeatherData(data)

