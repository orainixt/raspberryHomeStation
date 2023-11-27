import requests 
from datetime import datetime

# Functions for the Date 
def getCurrentDate(): 
	currentDate = datetime.now() 
	goodFormatDate = currentDate.strftime('%d-%m-%Y %H:%M:%S')[:-3]
	return goodFormatDate
	
# Functions for the weather section 

def getWeather(apiKey,city):
	"""
	this function is loading the weather with the api key 
	:param apiKey: the api key 
	:param city: the city we want to have weather
	:return: the data corresponding to the city weather (or None if error)
	"""
	baseUrl = "https://api.openweathermap.org/data/2.5/weather"
	params = {"q": city, "appid":apiKey, "units":"metric"}
	response = requests.get(baseUrl, params=params)
	
	if response.status_code == 200: 
		data=response.json()
		return data
	else:
		print("Error while request :", response.status_code) 
		return None 

def getWeatherData():
	"""
	this function is using an apikey to collect data about the weather at Lille
	:return: string the string with the informations 
	"""
	myApiKey = "69a622249c718a2cbe5f2cdd85a6047d"
	city = "Lille"
	weatherData = getWeather(myApiKey,city)
	string = "Aujourd'hui à Lille : \n"
	
	if weatherData : 
		temperature = weatherData["main"]["temp"]
		description = weatherData["weather"][0]["description"]
		string += (f"Il fait {temperature}°C \n Conditions : {description}")
		
		return string

