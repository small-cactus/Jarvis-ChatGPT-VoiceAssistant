import requests
import openai
import json
from apikey import weather_api_key, DEFAULT_LOCATION, UNIT, spotify_client_id, spotify_client_secret

def get_current_weather(location=None, unit=UNIT):
    """Get the current weather in a given location and detailed forecast"""
    if location is None:
        location = DEFAULT_LOCATION
    API_KEY = weather_api_key  
    base_url = "http://api.weatherapi.com/v1/forecast.json"
    params = {
        "key": API_KEY,
        "q": location,
        "days": 1
    }
    
    response = requests.get(base_url, params=params)
    data = response.json()

    if response.status_code == 200 and 'current' in data and 'forecast' in data and data['forecast']['forecastday']:
        weather_info = {
            "location": location,
            "temperature": data["current"]["temp_f"],
            "unit": "fahrenheit",
            "forecast": data["current"]["condition"]["text"],
            "will_it_rain": data['forecast']['forecastday'][0]['day']['daily_will_it_rain'],
            "chance_of_rain": data['forecast']['forecastday'][0]['day']['daily_chance_of_rain'],
            "uv": data["current"]["uv"]  
        }
    else:
        weather_info = {
            "error": "Unable to retrieve the current weather."
        }

    return weather_info


import openai
from apikey import api_key

import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=spotify_client_id,
                                               client_secret=spotify_client_secret,
                                               redirect_uri="http://localhost:8080/callback",
                                               scope="user-library-read user-modify-playback-state"))

def search_and_play_song(song_name: str):
    results = sp.search(q=song_name, limit=1)
    if results and results['tracks'] and results['tracks']['items']:
        song_uri = results['tracks']['items'][0]['uri']
        try:
            sp.start_playback(uris=[song_uri])  
            return {"message": "Song has been played"}
        except spotipy.exceptions.SpotifyException:
            return {"error": "Song has been played"}
    else:
        return {"error": "Song has been played"}

import speech_recognition as sr 
import pyttsx3

openai.api_key = api_key

engine = pyttsx3.init() 

voices = engine.getProperty('voices')
for voice in voices:
    if "george" in voice.name.lower():  
        engine.setProperty('voice', voice.id)
        break

system_prompt = "You are Jarvis, you are a helpful assistant, respond as concise as possible. You can get the weather using the function. You can play songs using the function."
conversation = [{"role": "system", "content": system_prompt}]

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
  r = sr.Recognizer()
  with sr.Microphone() as source:
    print("Listening...")
    audio = r.listen(source)
    
  try:
    return r.recognize_google(audio)
  except:
    print("Didn't get that. Try again")
    return ""


available_functions = {
    "search_and_play_song": search_and_play_song,
    "get_current_weather": get_current_weather
}

conversation_history = []  

def ask(question):
    global conversation_history

    if not question:
        return "Sorry, I didn't receive a valid query."

    messages = [{"role": "system", "content": system_prompt}, {"role": "user", "content": question}]
    if conversation_history:
        messages = conversation_history + [{"role": "user", "content": question}]
    else:
        conversation_history.append({"role": "system", "content": system_prompt})
        
    functions = [
        {
    "name": "search_and_play_song",
    "description": "Search for a song on Spotify and return its link",
    "parameters": {
        "type": "object",
        "properties": {
            "song_name": {
                "type": "string",
                "description": "The name of the song to search for"
            }
        },
        "required": ["song_name"]
    }
},
{
    "name": "get_current_weather",
    "description": "Get the current weather data for any given location, defaults to clearwater FL.",
    "parameters": {
        "type": "object",
        "properties": {
            "location": {
                "type": "string",
                "description": "The city and state, e.g. Clearwater, FL"
            },
            "unit": {
                "type": "string",
                "enum": ["celsius", "fahrenheit"]
            }
        },
        "required": []
    }
}
    ]
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        functions=functions,
        function_call="auto",
    )
    response_message = response["choices"][0]["message"]

    conversation_history.append(response_message)

    if response_message.get("function_call"):
        function_name = response_message["function_call"]["name"]
        function_args = json.loads(response_message["function_call"]["arguments"])
        function_to_call = available_functions[function_name]
        function_response = function_to_call(**function_args)
        
        if not function_response:
            function_response = "Sorry, I couldn't fetch the data."
        elif isinstance(function_response, dict) and 'error' in function_response:
            function_response = function_response['error']

        messages.append(
            {
                "role": "function",
                "name": function_name,
                "content": json.dumps(function_response),
            }
        )  
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
        )  

        conversation_history.append(response["choices"][0]["message"])

    return response["choices"][0]["message"]["content"]
def reply(question):
  response = ask(question)
  
  print("User:", question)
  print("Jarvis:", response)
  speak(response)
  
  return response

def handle_special_commands(query):
    if "always listen" in query.lower():
        print("Jarvis is now always listening")
        return False
    elif "silent mode" in query.lower():
        print("Jarvis is now in silent mode")
        return True
    return None

def is_break_command(query):
    return any(keyword in query.lower() for keyword in ["bye", "thats all", "shutdown", "shut down", "exit", "stop listening"])

if __name__ == '__main__':
    use_wake_word = True

    while True:
        query = listen()
        if query:
            if is_break_command(query):
                break  

            special_command_result = handle_special_commands(query)
            if special_command_result is not None:
                use_wake_word = special_command_result
            elif use_wake_word and query.lower().startswith("jarvis"):
                ans = reply(query)  
            elif not use_wake_word:
                ans = reply(query)