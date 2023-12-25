import tkinter as tk 
from tkinter import ttk
import os
import csv
import subprocess

class AlarmManager:

    def __init__(self,interfaceApp):
        self.interfaceApp = interfaceApp
        self.filePath = os.path.join('..','data','alarmList.csv')
        self.buttonStates = {}

    def readCSVFileForAlarm(self):
        """
        this function read a CSV file and return a list of all alarms
        :return: list of alarm informations
        """
        alarmList = []
        with open(self.filePath,mode='r',encoding='utf-8') as csvFile:
            csvReader = csv.reader(csvFile)
            for ligne in csvReader:
                alarmList.append(','.join(ligne))
        return alarmList

    def convertListToStringAlarm(self,l):
        """
        this function convert a list to a String
        :param l: the list we want to convert 
        :return: string the string of the list
        """
        string = ""
        for i in range(0,len(l)):
            string += l[i] + "\n"
        return string
    

    def addAlarm(self, string):
        with open(self.filePath, mode='a',newline='',encoding='utf-8') as csvFile:
            csvWriter = csv.writer(csvFile,quoting=csv.QUOTE_MINIMAL)
            csvWriter.writerow([string])

    def buttonFunction(self,parentFrame):
        """
        function used by the alarm button
        :param parentFrame: the parentFrame 
        """
        optionFrame = tk.Toplevel(parentFrame)
        optionFrame.geometry("200x200")
        optionFrame.title("Create Your Alarm")

        mainLabel = tk.Label(optionFrame,text="Pick an Hour")
        mainLabel.grid(row=0,column=0,columnspan=3)

        listHour = [str(i) for i in range(25)]
        varHour = tk.StringVar(value=listHour[0])

        hourPannel = tk.OptionMenu(optionFrame,varHour,*listHour)
        hourPannel.grid(row=1,column=0)

        hourLabel = tk.Label(optionFrame,text="h")
        hourLabel.grid(row=1,column=1)

        listMinute = ["0", "15", "30", "45"]
        varMinute = tk.StringVar(value=listMinute[0])

        minutePannel = tk.OptionMenu(optionFrame,varMinute,*listMinute)
        minutePannel.grid(row=1,column=2)

        confirmButton = tk.Button(
            optionFrame,
            text="Confirm",
            command=lambda: self.validateAlarm(optionFrame,varHour,varMinute)
        )
        confirmButton.grid(row=6,column=0,columnspan=3)

    def validateAlarm(self,frame,hour,minute):
        """
        function used by the confirm button
        it create a good note (format for csv file)
        :param frame: the frame 
        :param hour: the hour of the alarm 
        :param minute: the minute of the alarm 
        """
        hourSelected = hour.get()
        minuteSelected = minute.get()
        if int(hourSelected) < 10:
            hourSelected = "0" + hourSelected
        if int(minuteSelected)< 10:
            minuteSelected = "0" + minuteSelected
        hourFinal = hourSelected + "h" + minuteSelected
        self.addAlarm(hourFinal)
        self.interfaceApp.update()
        frame.destroy()

    def toggleButton(self, buttonVar, button):
        """
        this function is called in the mainWindow in the alarms buttons
        :param buttonVar: the boolean for the state of the button (on/off)
        :param button: the alarm button 
        """
        etat = not buttonVar.get() 
        buttonVar.set(etat)
        couleur = "#4CD964" if etat else "#B3B3B3"
        button.config(bg=couleur)

    def playAlarm(): 
        subprocess.run(["aplay","../data/alarmSound.wav"])
