import tkinter as tk
from weatherWidget import *
from appointmentManager import AppointmentManager  
from noteManager import NoteManager 
from alarmManager import AlarmManager


class InterfaceApp:
    
    def __init__(self, root):
        self.root = root
        self.root.title("Interface Raspberry Pi")
        self.root.geometry("800x480")  #Ajustez la taille en fonction de la résolution de votre écran ("800x480") raspberry
        self.appointmentManager = AppointmentManager(self)
        self.noteManager = NoteManager(self)
        self.alarmManager = AlarmManager(self)
        self.create_widgets()
        
    # Functions that'll be used by Tkinter componants
    
        
    def update(self):
        """
        this function is used every time we need to update the main window 
        """
        # DATE 
        currentDate = getCurrentDate() 
        weatherString = getWeatherData() 
        stringLabel = currentDate + "\n" + weatherString
        self.dateLabel.config(text=stringLabel)
        # APPOINTMENTS
        listOfAppointment = self.appointmentManager.readCSVFileForAppointment()
        stringOfAppointment = self.appointmentManager.convertListToStringAppointment(listOfAppointment)
        self.appointmentLabel.config(text=stringOfAppointment) 
        # NOTES
        listOfNotes = self.noteManager.readCSVFileForNotes()
        stringOfNotes = self.noteManager.convertListToStringNote(listOfNotes)
        self.noteLabel.config(text=stringOfNotes)
        # ALARMS 
        listOfAlarms = self.alarmManager.readCSVFileForAlarm()
        stringOfAlarms = self.alarmManager.convertListToStringAlarm(listOfAlarms)
        self.alarmLabel.config(text=stringOfAlarms)
        for button, state in self.alarmManager.buttonStates.items():
            couleur = "#4CD964" if state else "#B3B3B3"
            button.config(bg=couleur)

    def onAlarmButtonClick(self, buttonVar, button):
        self.alarmManager.toggleButton(buttonVar, button)

    def create_widgets(self):
        """
        this function create the widget of the main window 
        """
        for i in range(8):
            
            frame = tk.Frame(self.root, width=200, height=240, borderwidth=2, relief="solid")
            rowPosition = i//4 
            frame.grid(row=rowPosition, column=i%4, padx=10, pady=10)
            
            # From here, frame is instancied and can be modified 
            
            if i == 0: 
                currentDate = getCurrentDate()
                weatherString = getWeatherData()
                stringLabel = currentDate + "\n" + weatherString
                self.dateLabel = tk.Label(frame, text = stringLabel,justify="center")
                self.dateLabel.pack()
                
            elif i == 1: 
                listOfAppointment = self.appointmentManager.readCSVFileForAppointment()
                stringOfAppointment = self.appointmentManager.convertListToStringAppointment(listOfAppointment)
                self.appointmentLabel = tk.Label(frame, text=stringOfAppointment)
                appointmentButton = tk.Button(
                    frame,
                    text="Create New Appointment",
                    command=lambda frame=frame:self.appointmentManager.buttonFunction(frame))
                self.appointmentLabel.pack()
                appointmentButton.pack() 
                
            elif i == 2:
                listOfNotes = self.noteManager.readCSVFileForNotes()
                stringOfNotes = self.noteManager.convertListToStringNote(listOfNotes)
                self.noteLabel = tk.Label(frame, text=stringOfNotes, justify="center")
                noteButton = tk.Button(
                    frame,
                    text="Create New Note",
                    command=lambda frame=frame:self.noteManager.buttonFunction(frame)
                )
                self.noteLabel.pack()
                noteButton.pack()

            elif i == 3 :

                listOfAlarms = self.alarmManager.readCSVFileForAlarm()
                
                y = 1
                titleLabel = tk.Label(frame,text=listOfAlarms[0])
                titleLabel.grid(row=0,column=0,columnspan=2)

                for z in range(1,len(listOfAlarms)) : 
                    alarm = listOfAlarms[z]
                    self.alarmLabel = tk.Label(frame,text=alarm)
                    alarmButtonVar = tk.BooleanVar()
                    alarmButton = tk.Button(
                        frame,
                        text="ON/OFF",
                    )
                    alarmButton.config(command=lambda buttonVar=alarmButtonVar, button=alarmButton: self.onAlarmButtonClick(buttonVar, button))
                    self.alarmLabel.grid(row=y,column=0)
                    alarmButton.grid(row=y,column=1)
                    y += 1 

                addAlarmButton = tk.Button(
                    frame,
                    text="Add New Alarm",
                    command=lambda frame=frame:self.alarmManager.buttonFunction(frame)
                )
                addAlarmButton.grid(row=y,column=0,columnspan=2)

            else : 
                label = tk.Label(frame, text=f"Information {i+1}")
                label.pack()
            
            
            for i in range(2): 
                self.root.grid_rowconfigure(i,weight=1) 
            
            for i in range(4):
                self.root.grid_columnconfigure(i,weight=1)

if __name__ == "__main__":
    root = tk.Tk()
    app = InterfaceApp(root)
    app.appointmentManager = AppointmentManager(app)
    app.noteManager = NoteManager(app)
    app.alarmManager = AlarmManager(app)
    root.mainloop()
