import csv
import os 

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

def addAppointment(title,content,date): 
	"""
	this function allow user to add an appointment to the CSV File
	:param title: the title of the appointment
	:param content: the content of the appointment 
	:param date: the date of the appointment
	"""
	relativePath = os.path.join('..','data','appointmentList.csv') 
	with open (relativePath, mode= 'a', newline='') as csvFile:
			csvWriter = csv.writer(csvFile)
			stringToAdd = title + "," + content + "," + date
			csvWriter.writerow(stringToAdd) 
