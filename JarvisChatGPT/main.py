import openai
from apikey import api_key

import speech_recognition as sr 
import pyttsx3

openai.api_key = api_key

engine = pyttsx3.init() 

voices = engine.getProperty('voices')
for voice in voices:
    if "george" in voice.name.lower():  # <- this part does nothing and I dont feel like removing it
        engine.setProperty('voice', voice.id)
        break

system_prompt = "You are Jarvis, a concise and helpful assistant. Keep ALL responses as concise as possible."
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

def ask(question):
  conversation.append({"role": "user", "content": question})
  response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=conversation
  )
  conversation.append({"role": "assistant", "content": response["choices"][0]["message"]["content"]})

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