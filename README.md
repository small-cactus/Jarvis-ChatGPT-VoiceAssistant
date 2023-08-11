# JarvisChatGPT
Jarvis powered by GPT-3.5/GPT-4

NOTE: You need an openai API key to use Jarvis.

APIKEY: Put your api key within the quotes inside the apikey.py file then save and exit.

THINGS TO INSTALL BEFORE RUNNING: Python: https://www.python.org/downloads/

STARTUP INFO:
1: Run install.bat, and wait for it to finish.
2: Run the Run.bat file, if it closes immediately you have done something wrong.


TROUBLESHOOT:
If the Run.bat file does not open Jarvis and instead closes, right click the empty space in the
file window that jarvis is in, click open in terminal and paste the following command without the quotes "Python main.py".

If any instalations fail while running the install.bat file, run this command using the same method to open the terminal, 
paste without the quotes "pip install openai SpeechRecognition pyttsx3 pyaudio"


GENERAL INFO:
Jarvis has no token limit so if you ask him to generate a feature film legnth script you're gonna have to wait for him to finish
talking or you can close and reopen Jarvis to skip.

You can change the #system prompt by changing the prompt within the main.py file, CTRL + F to easily find it, copy without the quotes: "system_prompt ="

You can change the wake word by finding this portion in the code and changing "Jarvis" to anything you want: startswith("jarvis")

Loud noises might confuse Jarvis, the mic will cutout because he thinks you're talking, don't worry he won't waste tokens, he knows when you say actual words.

Wake words will only work if it is the first thing you say within a spoken sentence. For example "Hey there, Jarvis who are you?" will NOT work. However "Jarvis who are you?" will work.

Vocal commands are listed when you run the Run.bat file

HELP ME BULID:
Please submit feature requests and issues for Jarvis, i'll add anything I think is easy or interesting.
