import csv
import os
# Functions for the note section 

def readCSVFileForNotes():
	"""
	This function read the appointmentList CSV file and returns 
	a list with all the informations for the notes
	:return: the list of informations
	"""	
	relativePath = os.path.join('..','data','noteList.csv')
	noteList = []
	with open(relativePath,newline='') as csvFile:
		csvReader = csv.DictReader(csvFile) 

		for ligne in csvReader:
			noteList.append(ligne['Titre'])
			noteList.append(ligne['Contenu'])
	return noteList 
	
def convertListToStringNote(l):
	"""
	This function return a string with the list information 
	:param l: the list
	:return: the string of all the information
	"""
	string = "Titre Contenu \n" 
	for i in range(0,len(l),2):
		string += l[i] + " : " + l[i+1] + "\n"
			
	return string
