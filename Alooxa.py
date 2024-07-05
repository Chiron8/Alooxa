from neuralintents import GenericAssistant
import pandas_datareader as web
import sys
import pyttsx3
import webbrowser
import nltk

import requests
weather_data = requests.get("http://api.openweathermap.org/data/2.5/weather?q=Southampton,GBR&APPID=0df68d400d12f95351570fdf112c7a15")

speech = pyttsx3.init()

todos = ['Sleep', 'Eat', 'Code', 'Repeat']

def greeting():
	print("Hey! It\'s me Alooxa!")
	speech.say("Hey! Its me Alooxa!")
	speech.runAndWait()

def todo_show():
	print("Your To-Do list is:\n")
	speech.say("Your To Do list is")
	speech.runAndWait()
	for todo in todos:
		print(todo)
		speech.say(todo)
		speech.runAndWait()
	print("\n\n")

def todo_add():
	speech.say("What do you need to do?")
	speech.runAndWait()
	todo = input("What do you need to do?")
	todos.append(todo)
	print("I added ", todo, " to your To-Do list")
	speech.say("I added")
	speech.runAndWait()
	speech.say(todo)
	speech.runAndWait()
	speech.say("To your list")
	speech.runAndWait()
def todo_remove():
	idx = int(input("Which task would you like to remove?")) - 1
	if idx < len(todos):
		print(f"Removing {todos[idx]}")
		todos.pop(idx)
	else:
		("There is no To-Do at this position")

def weather():
	max_tempK = weather_data.json().get('main').get('temp_max')
	min_tempK = weather_data.json().get('main').get('temp_min')
	wind_speed = weather_data.json().get('wind').get('speed')
	desc = weather_data.json().get('weather')[0].get('main')

	max_tempC = max_tempK - 273.15
	min_tempC = min_tempK - 273.15

	max_tempC = str(round(max_tempC, 1))
	min_tempC = str(round(min_tempC, 1))

	print("The weather for Southampton, England today is:\n\n")
	speech.say("The weather for Southampton, England today is")
	speech.runAndWait()

	print("The maximum temperature for today is", max_tempC, "°C")
	print("The min temp is: ", min_tempC, "°C")
	print("The conditions are: ", desc)
	print("The wind speed is: ", wind_speed, ' mph\n\n')
	TempSpeech = ("The maximum temperature for today is" + str(max_tempC) + "degrees celcius")
	speech.say(TempSpeech)
	speech.runAndWait()

	
	speech.say("The Minimum Temperature for today is")
	speech.runAndWait()
	speech.say(min_tempC)
	speech.runAndWait()
	speech.say("Degrees Celcius")
	speech.runAndWait()
	
	speech.say("The conditions are")
	speech.runAndWait()
	speech.say(desc)
	speech.runAndWait()
	
	speech.say("The wind speed is")
	speech.runAndWait()
	speech.say(wind_speed)
	speech.runAndWait()
	speech.say("Miles per hour")
	speech.runAndWait()

def web():
                GoogleSearch = ('https://www.google.com/search?q=')
                Search = input('What do you want to look up?')
                JoinV = (GoogleSearch, Search)
                Seperator = ''
                Site = Seperator.join(JoinV)
                webbrowser.open(Site, 2)



def bye():
	print("Bye")
	speech.say("Bye")
	speech.runAndWait()
	sys.exit(0)

def NotSure():
	print("I'm sorry, I don't understand what you mean by ", message)
	speech.say("I am sorry I don't understand what you mean by")
	speech.runAndWait()
	speech.say(message)
	speech.runAndWait()

mappings = {'Greeting': greeting,
	    'Show_TODOS': todo_show,
        'Exit':bye,
        'Add_TODO':todo_add,
        'Weather':weather,
		'Web':web,
		'NotSure':NotSure}

assistant = GenericAssistant("Intents.json", mappings)

assistant.train_model()
assistant.save_model("Alooxa")

#assistant.load_model("Alooxa")


while True:
	message = input("Message: ")
	assistant.request(message)
