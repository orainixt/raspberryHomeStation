# raspberryHomeStation
This is the code for my own raspberry station

# How it works 
- I'm currently trying to "copy" a google station, with informations that I think are usefull for my day 
- It's in python (I'm using a raspbery) 
- The sources files are in [src](src)
- The data files are in [data](data) 

## State of Development 
- For the moment, I only coded the main files, nothing is "pretty" 

## To activate the venv
- If it's your first time using this repository, you need to launch a virtual enviromnent 
- First launch : (for Linux / macOs)
- ```	bash 
	python3 -m venv venv
	source venv/bin/activate
	pip install -r requirements.txt ```
- First launch : (for Windows)
- ```	shell
	python3 -m venv venv 
	venv/Scripts/activate```

## To desactivate it (when you are done)
- Quite easy : (for all os)
- `desactivate`

## Main File 
- The main file is available at [main.py](src/mainWindow.py)
- For now, you can launch it like that : 
- ```	root/src
	python3 mainWindow.py```
