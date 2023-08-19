# <span style="color: #3498db;">JarvisChatGPT</span>

JarvisChatGPT is a voice assistant powered by ChatGPT, named <span style="font-style: italic;">Jarvis</span>. It uses the <span style="font-weight: bold;">GPT-3.5-Turbo</span> model by default, but you can switch to <span style="font-weight: bold;">GPT-4</span> by making edits in the `main.py` file.

**NOTE:** To use JarvisChatGPT, you must have an <span style="font-weight: bold;">OpenAI API key</span>.

**APIKEY:** Place your API key within the quotes in the `apikey.py` file, then save and exit.

## Prerequisites
1. Install Python: [Download Python](https://www.python.org/downloads/)
2. Run `install.bat` and wait for the installation to complete.
3. Execute the `Run.bat` file. If it closes immediately, you might have missed a step during setup.

## Getting Started
1. Run `install.bat` to install all dependencies.
2. Launch JarvisChatGPT by running the `Run.bat` file. If it closes immediately, there might be an issue with your configuration.

## Troubleshooting
If the `Run.bat` file closes without opening JarvisChatGPT, follow these steps:
1. Right-click in the directory where Jarvis is located.
2. Choose "Open in Terminal."
3. Paste the following command and press Enter:
```shell
python main.py
```

If any installations fail during the `install.bat` execution, use the same terminal method mentioned above and run this command:
```shell
pip install openai SpeechRecognition pyttsx3 pyaudio
```

## General Information
- JarvisChatGPT does not have a token limit. If you ask it to generate a feature film-length script, be prepared to wait for its response. Alternatively, you can close and reopen Jarvis to skip its response.
  
- You can modify the system prompt by changing the code within the `main.py` file. Use `CTRL + F` to locate it easily. The system prompt in the code is: `system_prompt =`
  
- You can customize the wake word by locating the following section in the code and changing "Jarvis" to any other desired word. Look for: `startswith("jarvis")`
  
- For better weather functionality, replace the placeholders in the `apikey.py` with your respective information.
  
- JarvisChatGPT might be affected by loud noises that and will cause microphone cutouts making him unable to hear you. It may interpret these noises as speech. However, it won't consume tokens for non-speech sounds.
  
- The wake word works only if it is the first word spoken in a sentence. For instance, "Hey there, Jarvis, who are you?" will NOT trigger a response. However, "Jarvis, who are you?" will work as intended.
  
- A list of vocal commands is provided when you run the `Run.bat` file.


## Changelog
- **Added weather support to Jarvis:** Jarvis can now call a weather API and retrieve weather information by himself.
- You will not need a separate API key for this functionality!

## Contribute to Development
Feel free to submit feature requests and report issues for JarvisChatGPT. I'll consider implementing anything that's feasible and interesting.

