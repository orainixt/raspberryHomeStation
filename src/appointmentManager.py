import csv 
import os

class AppointmentManager:

	def __init__(self):
		self.filePath = os.path.join('..', 'data', 'appointmentList.csv')
	
	# Functions for the Appointment 
	def readCSVFileForAppointment(self): 
		"""
		This function read the appointmentList CSV file and returns 
		a list with all the informations for the appointment
		:return: the list of informations
		"""
		appointmentList = []
		with open(self.filePath,mode='r', encoding='utf-8') as csvFile:
			csvReader = csv.reader(csvFile) 
			for ligne in csvReader:
				appointmentList.append(','.join(ligne))
		return appointmentList 
	
	def convertListToStringAppointment(self,l): 
		"""
		This function return a string with the list information 
		:param l: the list
		:return: the string of all the information
		"""
		string = "" 
		for i in range(0,len(l)):  
			string += l[i] + "\n"
		return string

	def addAppointment(self,string): 
		"""
		this function allow user to add an appointment to the CSV File
		:param title: the title of the appointment 
		:param date: the date of the appointment
		:param hour: the hour of the appointment
		"""	
		with open (self.filePath, mode= 'a', newline='',encoding='utf-8') as csvFile:
			csvWriter = csv.writer(csvFile,quoting=csv.QUOTE_MINIMAL)
			csvWriter.writerow([string]) 