import csv
import os 
import tkinter as tk
from tkinter import ttk 
from tkcalendar import DateEntry

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

def addAppointment(title,date,hour): 
	"""
	this function allow user to add an appointment to the CSV File
	:param title: the title of the appointment 
	:param date: the date of the appointment
	:param hour: the hour of the appointment
	"""
	relativePath = os.path.join('..','data','appointmentList.csv') 
	with open (relativePath, mode= 'a', newline='') as csvFile:
			csvWriter = csv.writer(csvFile)
			stringToAdd = title + "," + content + "," + date
			csvWriter.writerow(stringToAdd) 

def buttonFunction(parentFrame): 
	"""
	this function is called in the main window when the user click on the appointment button
	:param parentFrame: the parentFrame
	"""
	
	#Creation of the new window
	optionFrame = tk.Toplevel(parentFrame)
	optionFrame.geometry("200x200")
	optionFrame.title("Create an Appointment")
	
	mainLabel = tk.Label(optionFrame, text="Quel type de RDV?")
	mainLabel.pack() 
	
	#First pannel (<=> title) 
	listPannel1 = ["Psy","Fabien","Médecin"]
	varPannel1 = tk.StringVar(value=listPannel1[0])
	
	pannel1 = tk.OptionMenu(optionFrame,varPannel1, *listPannel1)
	pannel1.pack()
	
	#Second pannel (<=> date) 
	dateLabel = tk.Label(optionFrame, text= "Please pick a date :")
	dateLabel.pack()
	
	selectedDate = tk.StringVar()
	pickerDate = DateEntry(optionFrame, textvariable=selectedDate, date_pattern="yyyy-mm-dd")
	pickerDate.pack()
	
	# Information "Please pick an hour"
	textLabel = tk.Label(optionFrame, text="Please pick an hour") 
	
	#Third pannel (<=> hour)
	listHour = [] 
	for i in range(25):
		listHour.append(i)
		 
	varHour = tk.StringVar(value=listHour[0])
	
	hourPanel = tk.OptionMenu(optionFrame,varHour, *listHour)
	hourPanel.pack()
	
	listMinute = []
	for i in range(61): 
		listMinute.append(i) 
	
	varMinute = tk.StringVar(value=listMinute[0]) 
	
	minutePannel = tk.OptionMenu(optionFrame, varMinute, *listMinute) 
	minutePannel.pack()
	
	
	
	
	 
