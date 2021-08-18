from urllib import request
import requests  # access to url links
import json  # json
import pyttsx3  # text to speech - ver 2.71

# voice setting section(male\female, fast\slow etc..)
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 125)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # 1 - male, 0 - female

# random jokes API link
url = "http://official-joke-api.appspot.com/random_ten"
response = requests.get(url)
print(response.status_code)
# creating a json file for the generated data
jsonData = json.loads(response.text)
print(jsonData)

"""
This class represent a joke with a setup and a punchLine.
It also contain a toString method.
"""
class Joke:
    def __init__(self, setup, punchline) -> None:
        self.setup = setup
        self.punchline = punchline

    def __str__(self) -> str:
        return f"-> {self.setup} ... {self.punchline}"

# end of class Joke

jokes = []  # a list of Jokes objects

#   loop through the json file and create new Jokes objects & add them to the list
for j in jsonData:
    setup = j["setup"]
    punchline = j["punchline"]
    joke = Joke(setup, punchline)
    jokes.append(joke)

print(len(jokes))
# print and saying the Joke
for jk in jokes:
    print(jk.__str__())
    engine.say(jk)
    engine.runAndWait()
    engine.stop()
