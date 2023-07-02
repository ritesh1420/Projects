#non inpute function
import datetime
from speak import say
def Time():
    time=datetime.datetime.now().strftime("%H:%M")
    say(time)

def Date():
    date=datetime.date.today()
    say(date)
def Day():
    day=datetime.datetime.now().strftime("%A")
    say(day)

def NonInputExecution(query):
    query=str(query)
    if("time") in query:
        Time()
    elif "date" in query:
        Date()
    elif "day" in query:
        Day()

#inpute function
import wikipedia
from PyDictionary import PyDictionary
import webbrowser
from listen import Listen
import os


def InputExecution(tag,query):
    if "wikipedia" in tag:
        name = str(query).replace("what is", "").replace("who is", "").replace("wikipedia", "").replace("what is",
                                                                                                          "definition of")
        try:
            page = wikipedia.page(name)
            summary = wikipedia.summary(name, sentences=2)  # Set the number of sentences you want
            say(summary)
        except wikipedia.exceptions.DisambiguationError as e:
            options = e.options[:3]  # Get the first three options
            say(f"There are multiple options for {name}. Here are some suggestions: {', '.join(options)}")
        except wikipedia.exceptions.PageError:
            say(f"I couldn't find any information on {name}.")

    elif "meaning" in tag:
        word = str(query).replace("meaning of", "").replace("what is the meaning of", "").replace("what are the meaning of", "").strip()
        dictionary = PyDictionary()
        meanings = dictionary.meaning(word)
        if meanings:
            response = f"The meanings of '{word}' are: "
            for part_of_speech, meanings_list in meanings.items():
                response += f"{part_of_speech}: {', '.join(meanings_list[:2])}. "
            say(response)
        else:
            say(f"No meanings found for '{word}'.")

    elif "youtube" in tag:
       say("Ok, what do you want to search?")
       request = Listen()
       if request:
           search_query = request.replace(" ", "+")
           search_url = f"https://www.youtube.com/results?search_query={search_query}"
           webbrowser.open(search_url)
           say(f"Searching YouTube for {request}.")
       else:
            say("I'm sorry, I didn't catch you.")


    elif "google" in tag:
        search_query = str(query).replace("search on google", "").replace("search ", "").strip()
        search_url = f"https://www.google.com/search?q={search_query}"
        webbrowser.open(search_url)
        say(f"Searching Google for {search_query}.")


    elif "any" in tag:
        say("Sure, please tell me website name.")
        website = Listen().replace(" ", "")
        if website:
            website_url = "https://www." + website + ".com"
            webbrowser.open(website_url)
            say(f"Opening {website}.")
        else:
            say("I'm sorry, I didn't catch the website name.")


    elif "screenshot" in tag:
        import pyautogui
        say("Sure,tell me name of this screenshot")
        name = Listen()
        save_path = "C://Users//Ritesh//Desktop//screenshot//name.png"  # Specify the desired save path here
        screenshot = pyautogui.screenshot()
        screenshot.save(save_path)
        say(f"Screenshot captured and saved as {os.path.basename(save_path)}")
       




