1# Methods used in the main window are regrouped here
from datetime import datetime
import csv 
import os
from PIL import Image
import requests 

# Functions for the Date 
def getCurrentDate(): 
	currentDate = datetime.now() 
	goodFormatDate = currentDate.strftime('%d-%m-%Y %H:%M:%S')[:-3]
	return goodFormatDate
	
# Functions for the Appointment 
def readCSVFileForAppointment(): 
	"""
	This function read the appointmentList CSV file and returns 
	a list with all the informations for the appointment
	:return: the list of informations
	"""
	relativePath = os.path.join('..','data','appointmentList.csv') 
	appointmentList = []
	with open(relativePath,newline='') as csvFile:
		csvReader = csv.DictReader(csvFile) 

		for ligne in csvReader:
			appointmentList.append(ligne['Titre'])
			appointmentList.append(ligne['Date'])
			appointmentList.append(ligne['Heure'])
	return appointmentList 
	
def convertListToStringAppointment(l): 
	"""
	This function return a string with the list information 
	:param l: the list
	:return: the string of all the information
	"""
	string = "Titre Date Heure" + "\n" 
	for i in range(0,len(l),3):
		string += l[i] + " " + l[i+1] + " " + l[i+2] + "\n"
			
	return string
			
# Functions for the gif / media section 
def loadImage(path):
	"""
	This function is loading an image with the pillow module 
	:param path: the path of the image
	:return: a pillow image in a tkinter compatible format
	""" 
	pass
			
# Functions for the note section 

def readCSVFileForNotes():
	"""
	This function read the appointmentList CSV file and returns 
	a list with all the informations for the notes
	:return: the list of informations
	"""	
	relativePath = os.path.join('..','data','noteList.csv')
	noteList = []
	with open(relativePath,newline='') as csvFile:
		csvReader = csv.DictReader(csvFile) 

		for ligne in csvReader:
			noteList.append(ligne['Titre'])
			noteList.append(ligne['Contenu'])
	return noteList 
	
def convertListToStringNote(l):
	"""
	This function return a string with the list information 
	:param l: the list
	:return: the string of all the information
	"""
	string = "Titre Contenu \n" 
	for i in range(0,len(l),2):
		string += l[i] + " : " + l[i+1] + "\n"
			
	return string

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

