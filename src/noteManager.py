import csv
import os
import tkinter as tk

class NoteManager:

    def __init__(self, interfaceApp):
        self.filePath = os.path.join('..', 'data', 'noteList.csv')
        self.interfaceApp = interfaceApp

    def readCSVFileForNotes(self):
        """
        This function read the appointmentList CSV file and returns 
        a list with all the informations for the notes
        :return: the list of informations
        """    
        relativePath = os.path.join('..', 'data', 'noteList.csv')
        noteList = []
        with open(relativePath, newline='') as csvFile:
            csvReader = csv.DictReader(csvFile)

            for ligne in csvReader:
                noteList.append(ligne['Titre'])
                noteList.append(ligne['Contenu'])
        return noteList

    def convertListToStringNote(self, l):
        """
        This function return a string with the list information 
        :param l: the list
        :return: the string of all the information
        """
        string = "Titre Contenu \n"
        for i in range(0, len(l), 2):
            string += f"{l[i]} : {l[i + 1]}\n"

        return string

    def addNote(self,string):
        """
        add a note to the note note csv file
        :param string: the string we want to add
        """
        with open(self.filePath, mode='a',newline='',encoding='utf-8') as csvFile:
            csvWriter = csv.writer(csvFile,quoting=csv.QUOTE_MINIMAL)
            csvWriter.writerow([string])
    
    def buttonFunction(self,parentFrame):
        """
        function used by the button to create a note popup
        :param parentFrame: used to create toplevel
        """
        optionFrame = tk.Toplevel(parentFrame)
        optionFrame.geometry("200x200")
        optionFrame.title("Create a Note") 

        titleLabel = tk.Label(optionFrame,text="Title :")
        titleLabel.pack()

        textTitle = tk.Text(optionFrame,height=2,width=40)
        textTitle.pack()

        contentLabel = tk.Label(optionFrame,text="Content :")
        contentLabel.pack()

        textContent = tk.Text(optionFrame,height=2,width=40)
        textContent.pack()

        confirmButton = tk.Button(
            optionFrame,
            text="Confirm",
            command=lambda: self.validateNote(optionFrame,textTitle,textContent)
        )
        confirmButton.pack()

    def validateNote(self,frame,title,content):
        """
        function used by the confirm button to create a note 
        :param frame: the frame 
        :param title: the title of the note
        :param content: the content of the note
        """
        titleText = title.get("1.0", "end-1c")
        contentText = content.get("1.0", "end-1c")
        self.addNote(titleText + " " + contentText)
        self.interfaceApp.update()
        frame.destroy()


