import csv
import os 
import tkinter as tk
from tkinter import ttk 
from tkcalendar import DateEntry

 #class NewAppointment:
	 
	#def __init__(self,appointmentType,appointmentDate,appointmentHour): 
		  #self.appointmentType = appointmentType
		#self.appointmentDate = appointmentDate
		#self.appointmentHour = appointmentHour 
	
	
	
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
	string = "" 
	for i in range(0,len(l),3):
		string += l[i] + " " + l[i+1] + " " + l[i+2] + "\n"
	return string

def addAppointment(string): 
	"""
	this function allow user to add an appointment to the CSV File
	:param title: the title of the appointment 
	:param date: the date of the appointment
	:param hour: the hour of the appointment
	"""
	relativePath = os.path.join('..','data','appointmentList.csv') 
	with open (relativePath, mode= 'a', newline='') as csvFile:
			csvWriter = csv.writer(csvFile)
			csvWriter.writerow(string) 

def buttonFunction(parentFrame): 
	"""
	this function is called in the main window when the user click on the appointment button
	:param parentFrame: the parentFrame
	"""
	
	# Creation of the new window
	optionFrame = tk.Toplevel(parentFrame)
	optionFrame.geometry("200x200")
	optionFrame.title("Create an Appointment")
	
	mainLabel = tk.Label(optionFrame, text="Quel type de RDV?")
	mainLabel.grid(row=0,column=0,columnspan=3) 
	
	# First pannel (<=> title) 
	listPannel1 = ["Psy","Fabien","Médecin"]
	varPannel1 = tk.StringVar(value=listPannel1[0])
	
	pannel1 = tk.OptionMenu(optionFrame,varPannel1, *listPannel1)
	pannel1.grid(row=1,column=0,columnspan=3)
	
	# Second pannel (<=> date) 
	dateLabel = tk.Label(optionFrame, text= "Please pick a date :")
	dateLabel.grid(row=2,column=0,columnspan=3)
	
	selectedDate = tk.StringVar()
	pickerDate = DateEntry(optionFrame, textvariable=selectedDate, date_pattern="dd/mm/yyyy")
	pickerDate.grid(row=3,column=0,columnspan=3)
	
	# Information "Please pick an hour"
	textLabel = ttk.Label(optionFrame, text="Please pick an hour") 
	textLabel.grid(row=4,column=0,columnspan=2, sticky=tk.W + tk.E)
	
	# Third pannel (<=> hour)
	# First menu 
	listHour = [str(i) for i in range(26)]		 
	varHour = tk.StringVar(value=listHour[0])
	
	hourPanel = ttk.OptionMenu(optionFrame,varHour, *listHour)
	hourPanel.grid(row=5,column=0)
	
	# Letter h 
	labelCharactor = tk.Label(optionFrame, text="h") 
	labelCharactor.grid(row=6, column=1, sticky=tk.N + tk.W)
	
	# Second menu
	listMinute = [str(i) for i in range(61)]
	varMinute = tk.StringVar(value=listMinute[0]) 
	
	minutePannel = ttk.OptionMenu(optionFrame, varMinute, *listMinute) 
	minutePannel.grid(row=5,column=2)
	
	# The confirm button 
	
	confirmButton = tk.Button(optionFrame, text="Confirm",command=lambda:validateAppointment(optionFrame, varPannel1,selectedDate, varHour, varMinute))
	confirmButton.grid(row=6,column=0,columnspan=2)
	
def validateAppointment(frame,typeRDV,date,hour,minute):
	typeRDVSelected = typeRDV.get()
	dateSelected = date.get()
	hourSelected = hour.get() 
	minuteSelected = minute.get()
	if int(hourSelected) < 10: 
		hourSelected = "0" + hourSelected 
	if int(minuteSelected) < 10: 
		minuteSelected = "0" + minuteSelected 
	hourFinal = hourSelected + "h" + minuteSelected
	addAppointment(typeRDVSelected + "," + dateSelected + "," + hourFinal)
	frame.destroy()
	
	 
