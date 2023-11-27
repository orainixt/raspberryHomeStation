import tkinter as tk
from weatherWidget import *


class InterfaceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Interface Raspberry Pi")
        self.root.geometry("800x480")  # Ajustez la taille en fonction de la résolution de votre écran

        self.create_widgets()

    def create_widgets(self):
        # Créer les six carrés avec des étiquettes d'informations
        for i in range(8):
            
            frame = tk.Frame(self.root, width=200, height=240, borderwidth=2, relief="solid")
            rowPosition = i//4 
            frame.grid(row=rowPosition, column=i%4, padx=10, pady=10)
            
            # From here, frame is instancied and can be modified 
            
            if i == 0: 
                currentDate = getCurrentDate()
                weatherString = getWeatherData()
                stringLabel = currentDate + "\n" + weatherString
                dateLabel = tk.Label(frame, text = stringLabel,justify="center")
                dateLabel.pack()
                
            elif i == 1: 
                listOfAppointment = readCSVFileForAppointment()
                stringOfAppointment = convertListToStringAppointment(listOfAppointment)
                appointmentLabel = tk.Label(frame, text=stringOfAppointment)
                addAppointmentButton = tk.Button(frame,text="Create New Appointment")
                appointmentLabel.pack()
                addAppointmentButton.pack() 
                
            elif i == 2:
                listOfNotes = readCSVFileForNotes()
                stringOfNotes = convertListToStringNote(listOfNotes)
                noteLabel = tk.Label(frame, text=stringOfNotes, justify="center")
                noteLabel.pack()
                
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
    root.mainloop()
