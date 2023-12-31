import csv
import os
import tkinter as tk
from tkcalendar import DateEntry
from tkinter import ttk

class AppointmentManager:

    def __init__(self,interfaceApp):
        """
        __ init__() is the AppointmentManager constructor 
        """
        self.filePath = os.path.join('..', 'data', 'appointmentList.csv')
        self.interfaceApp = interfaceApp

    def readCSVFileForAppointment(self):
        """
        this function read a CSV file and return a list of all informations
        :return: a list of the informations on the CSV file
        """
        appointmentList = []
        with open(self.filePath, mode='r', encoding='utf-8') as csvFile:
            csvReader = csv.reader(csvFile)
            for ligne in csvReader:
                appointmentList.append(','.join(ligne))
        return appointmentList


    def convertListToStringAppointment(self, l):
        """
        this function convert a list to a String 
        :param l: the list we want to convert 
        :return: string the string of the list 
        """
        string = ""
        for i in range(0, len(l)):
            string += l[i] + "\n"
        return string


    def addAppointment(self, string):
        """
        this function add an appointment to the csv file 
        :param string: the string we want to add 
        """
        with open(self.filePath, mode='a', newline='', encoding='utf-8') as csvFile:
            csvWriter = csv.writer(csvFile, quoting=csv.QUOTE_MINIMAL)
            csvWriter.writerow([string])

    def buttonFunction(self, parentFrame):
        """
        this function is used by the button to create a brand new popup
        :param parentFrame: used to create a toplevel
        """
        optionFrame = tk.Toplevel(parentFrame)
        optionFrame.geometry("200x200")
        optionFrame.title("Create an Appointment")

        mainLabel = tk.Label(optionFrame, text="Quel type de RDV?")
        mainLabel.grid(row=0, column=0, columnspan=3)

        listPannel1 = ["Psy", "Fabien", "Médecin"]
        varPannel1 = tk.StringVar(value=listPannel1[0])

        pannel1 = tk.OptionMenu(optionFrame, varPannel1, *listPannel1)
        pannel1.grid(row=1, column=0, columnspan=3)

        dateLabel = tk.Label(optionFrame, text="Please pick a date :")
        dateLabel.grid(row=2, column=0, columnspan=3)

        selectedDate = tk.StringVar()
        pickerDate = DateEntry(optionFrame, textvariable=selectedDate, date_pattern="dd/mm/yyyy")
        pickerDate.grid(row=3, column=0, columnspan=3)

        textLabel = ttk.Label(optionFrame, text="Please pick an hour")
        textLabel.grid(row=4, column=0, columnspan=2, sticky=tk.W + tk.E)

        listHour = [str(i) for i in range(25)]
        varHour = tk.StringVar(value=listHour[0])

        hourPanel = ttk.OptionMenu(optionFrame, varHour, *listHour)
        hourPanel.grid(row=5, column=0)

        labelCharactor = tk.Label(optionFrame, text="h")
        labelCharactor.grid(row=6, column=1, sticky=tk.N + tk.W)

        listMinute = ["0", "15", "30", "45"]
        varMinute = tk.StringVar(value=listMinute[0])

        minutePannel = ttk.OptionMenu(optionFrame, varMinute, *listMinute)
        minutePannel.grid(row=5, column=2)

        confirmButton = tk.Button(
            optionFrame,
            text="Confirm",
            command=lambda: self.validateAppointment(optionFrame, varPannel1, selectedDate, varHour, varMinute)
        )
        confirmButton.grid(row=6, column=0, columnspan=2)

    def validateAppointment(self, frame, typeRDV, date, hour, minute):
        """
        this function is used by the confirm button 
        it create a "good" appointment (format typeRdv,date,hourFinal)
        :param frame: the frame of the function 
        :param typeRDV: the type given by the btn function
        :param date: the date given by the btn function
        :param hour: the hour given by the btn function
        :param minute: the minute given by the btn function
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
        self.interfaceApp.update()
        frame.destroy()


