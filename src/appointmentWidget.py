import csv
import os 
import tkinter as tk
from tkinter import ttk 
from tkcalendar import DateEntry
from mainWindow import *

class AppointmentWidget:

	def __init__(self):
		self.appointmentManager = AppointmentManager()

	def buttonFunction(self,parentFrame): 
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
		listHour = [str(i) for i in range(25)]		 
		varHour = tk.StringVar(value=listHour[0])
	
		hourPanel = ttk.OptionMenu(optionFrame,varHour, *listHour)
		hourPanel.grid(row=5,column=0)
	
		# Letter h 
		labelCharactor = tk.Label(optionFrame, text="h") 
		labelCharactor.grid(row=6, column=1, sticky=tk.N + tk.W)
	
		# Second menu
		listMinute = ["0","15","30","45"]
		varMinute = tk.StringVar(value=listMinute[0]) 
	
		minutePannel = ttk.OptionMenu(optionFrame, varMinute, *listMinute) 
		minutePannel.grid(row=5,column=2)
	
		# The confirm button 
	
		confirmButton = tk.Button(
			optionFrame,
			text="Confirm",
			command=lambda:self.validateAppointment(optionFrame, varPannel1,selectedDate, varHour, varMinute))
		confirmButton.grid(row=6,column=0,columnspan=2)
	
	def validateAppointment(self,frame,typeRDV,date,hour,minute,callback):
		"""
		validateAppointment is a function that transform the data from the appointment widget popup
		and update the main window with the new data 
		:param frame: the frame (the main window in this case)
		:param typeRDV: the type of rdv 
		:param date: the date
		:param hour: the hour
		:param minute: the minute
		"""
		typeRDVSelected = typeRDV.get()
		dateSelected = date.get()
		hourSelected = hour.get() 
		minuteSelected = minute.get()
		if int(hourSelected) < 10: 
			hourSelected = "0" + hourSelected 
		if int(minuteSelected) < 10: 
			minuteSelected = "0" + minuteSelected 
		hourFinal = hourSelected + "h" + minuteSelected
		self.addAppointment(typeRDVSelected + "," + dateSelected + "," + hourFinal)
		callback()
		frame.destroy()
