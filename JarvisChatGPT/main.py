import requests
import openai
import json
import math
import os
from apikey import weather_api_key, DEFAULT_LOCATION, UNIT, spotify_client_id, spotify_client_secret
from datetime import datetime

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
        "feels_like": data["current"]["feelslike_f"],
        "max_temp": data['forecast']['forecastday'][0]['day']['maxtemp_f'],
        "min_temp": data['forecast']['forecastday'][0]['day']['mintemp_f'],
        "unit": "fahrenheit",
        "forecast": data["current"]["condition"]["text"],
        "wind_speed": data["current"]["wind_mph"],
        "wind_direction": data["current"]["wind_dir"],
        "humidity": data["current"]["humidity"],
        "pressure": data["current"]["pressure_in"],
        "rain_inches": data["current"]["precip_in"],
        "sunrise": data['forecast']['forecastday'][0]['astro']['sunrise'],
        "sunset": data['forecast']['forecastday'][0]['astro']['sunset'],
        "moonrise": data['forecast']['forecastday'][0]['astro']['moonrise'],
        "moonset": data['forecast']['forecastday'][0]['astro']['moonset'],
        "moon_phase": data['forecast']['forecastday'][0]['astro']['moon_phase'],
        "visibility": data["current"]["vis_miles"],
        "will_it_rain": data['forecast']['forecastday'][0]['day']['daily_will_it_rain'],
        "chance_of_rain": data['forecast']['forecastday'][0]['day']['daily_chance_of_rain'],
        "uv": data["current"]["uv"]  
        }
    else:
        weather_info = {
            "error": "Unable to retrieve the current weather. Try again in a few seconds."
        }

    return weather_info

def perform_math(operation, operands):
    """Perform a math operation based on the given operation and operands"""
    if not operands:
        return {"error": "No operands provided"}

    result = None
    if operation == "add":
        result = sum(operands)
    elif operation == "subtract":
        result = operands[0] - sum(operands[1:])
    elif operation == "multiply":
        result = 1
        for op in operands:
            result *= op
    elif operation == "divide":
        result = operands[0] / operands[1] if operands[1] != 0 else "Undefined (division by zero)"
    elif operation == "power":
        result = pow(operands[0], operands[1])
    elif operation == "square_root":
        result = math.sqrt(operands[0])

    return {"result": result}

memory_file_path = None

def get_memory_file_path():
    """Return the full path to the memory.txt file. Create the file if it doesn't exist."""
    global memory_file_path

    if memory_file_path:
        return memory_file_path

    current_dir = os.path.dirname(os.path.abspath(__file__))

    memory_file_path = os.path.join(current_dir, "memory.txt")

    if not os.path.exists(memory_file_path):
        with open(memory_file_path, 'w') as file:
            json.dump([], file)

    return memory_file_path

def memory_manager(operation, data=None):
    """Store, retrieve, or clear data in a file"""
    file_path = get_memory_file_path()
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if operation == "store":
        with open(file_path, 'r') as file:
            memory = json.load(file)
        
        memory.append({
            "data": data,
            "store_time": current_time,
            "retrieve_time": None
        })

        with open(file_path, 'w') as file:
            json.dump(memory, file)

        return {"message": f"Data stored successfully on {current_time}"}

    elif operation == "retrieve":
        with open(file_path, 'r') as file:
            memory = json.load(file)

        if not memory:
            return {"message": "No data stored yet"}

        for item in memory:
            item["retrieve_time"] = current_time

        with open(file_path, 'w') as file:
            json.dump(memory, file)

        retrieved_data = [{"data": item["data"], "store_time": item["store_time"], "retrieve_time": current_time} for item in memory]
        return {"message": f"Data retrieved on {current_time}", "data": retrieved_data}

    elif operation == "clear":
        with open(file_path, 'w') as file:
            json.dump([], file)
        return {"message": "Memory cleared successfully"}

def get_current_datetime(mode="date & time"):
    """Get the current date and/or time"""
    now = datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    time_str = now.strftime("%I:%M:%S %p")  
    
    if mode == "date":
        return {"datetime": date_str}
    elif mode == "time":
        return {"datetime": time_str}
    else:
        return {"datetime": f"{date_str} {time_str}"}

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
        song_name = results['tracks']['items'][0]['name']  
        try:
            sp.start_playback(uris=[song_uri])
            return {"message": f"The song '{song_name}' is now playing"}
        except spotipy.exceptions.SpotifyException:
            return {"message": "Tell the user they have to open Spotify first before you can play the song."}
    else:
        return {"message": "Sorry, I couldn't find the song you requested."}

import speech_recognition as sr 
import pyttsx3

openai.api_key = api_key

engine = pyttsx3.init() 

voices = engine.getProperty('voices')
for voice in voices:
    if "george" in voice.name.lower():  
        engine.setProperty('voice', voice.id)
        break

system_prompt = "You are Jarvis, you are a helpful assistant, RESPOND AS CONCISE AS POSSIBLE. You can get the weather using the get_current_weather function ALWAYS format and delete uncessory weather info. You can play songs using the search_and_play_song function, if you get an error you will tell the user what the error was. You don't have to play the exact words the user gives you for a song, you can paraphrase or choose what you think fits better. ALWAYS SUMMARIZE WEATHER RESPONSE. If the user asks you a personal question, check the memory manager for stored data."
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
    "get_current_weather": get_current_weather,
    "get_current_datetime": get_current_datetime,
    "perform_math": perform_math,
    "memory_manager": memory_manager
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
    "description": "Search for a song by name on Spotify and play it",
    "parameters": {
        "type": "object",
        "properties": {
            "song_name": {
                "type": "string",
                "description": "The name of the song to search for (can be anything, doesn't have to be exactly what the user typed)"
            }
        },
        "required": ["song_name"]
    }
},
{
    "name": "get_current_datetime",
    "description": "Get the current date and/or time",
    "parameters": {
        "type": "object",
        "properties": {
            "mode": {
                "type": "string",
                "enum": ["date", "time", "date & time"],
                "description": "Choose whether to get date, time, or both",
            }
        },
        "required": ["mode"],
    },
},
{
    "name": "perform_math",
    "description": "Perform a math operation",
    "parameters": {
        "type": "object",
        "properties": {
            "operation": {
                "type": "string",
                "enum": ["add", "subtract", "multiply", "divide", "power", "square_root"],
                "description": "The math operation to perform"
            },
            "operands": {
                "type": "array",
                "items": {
                    "type": "number"
                },
                "description": "The numbers to perform the operation on"
            }
        },
        "required": ["operation", "operands"]
    }
},
{
    "name": "memory_manager",
    "description": "Store, retrieve, or clear data in a file",
    "parameters": {
        "type": "object",
        "properties": {
            "operation": {
                "type": "string",
                "enum": ["store", "retrieve", "clear"],
                "description": "Operation to perform"
            },
            "data": {
                "type": "string",
                "description": "The data to store, in this format: User asked me to remember... (required for 'store' operation)"
            }
        },
        "required": ["operation"]
    }
},
{
    "name": "get_current_weather",
    "description": "Get the current weather and condition data for any given location, eg moon phases, rain %, rainfall measurement, wind and pressure data, and more, defaults to clearwater FL.",
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