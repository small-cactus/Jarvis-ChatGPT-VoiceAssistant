# <span style="color: #3498db;">JarvisChatGPT</span>


JarvisChatGPT is a voice assistant powered by ChatGPT, named <span style="font-style: italic;">Jarvis</span>. It uses the <span style="font-weight: bold;">GPT-3.5-Turbo</span> model by default, but you can switch to <span style="font-weight: bold;">GPT-4</span> by making edits in the `main.py` file.


**NOTE:** To use JarvisChatGPT, you must have an <span style="font-weight: bold;">OpenAI API key</span>.

**APIKEY:** Place your API key within the quotes in the `apikey.py` file, then save and exit.

## Prerequisites
1. Install Python: [Download Python](https://www.python.org/downloads/)
2. Run `install.bat` and wait for the installation to complete.
3. Execute the `Run.bat` file. If it closes immediately, you might have missed a step during setup.


## Getting Started (2 click install)
1. Run `install.bat` to install all dependencies.
2. Launch JarvisChatGPT by running the `Run.bat` file. If it closes immediately, there might be an issue with your configuration.
3. If it doesn't run you might have to supply a Spotify client ID and client Secret for it to work, info on how to do that is listed in the spotify section.

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

1. If you get **errors trying to play music**, either credientials are wrong, or you do not have an **Active spotify session**, to overcome this issue simply play a song on spotify and pause it.

2. If music **playback still does not work**, you either don't have **spotify premium**, or you didn't put the client id and secret in right. Refer to spotify setup for insructions there

1. If the mic isn't working for Jarvis, open control panel, click sound, click recording at the top, then scroll to find the mic you're using, right click, then select make default device.

## General Information
- JarvisChatGPT does not have a token limit. If you ask it to generate a feature film-length script, be prepared to wait for its response. Alternatively, you can close and reopen Jarvis to skip its response.
  
- You can modify the system prompt by changing the code within the `main.py` file. Use `CTRL + F` to locate it easily. The system prompt in the code is: `system_prompt =`
  
- You can customize the wake word by locating the following section in the code and changing "Jarvis" to any other desired word. Look for: `startswith("jarvis")`
  
- For better weather functionality, replace the placeholders in the `apikey.py` with your respective information.
  
- JarvisChatGPT might be affected by loud noises that and will cause microphone cutouts making him unable to hear you. It may interpret these noises as speech. However, it won't consume tokens for non-speech sounds.
  
- The wake word works only if it is the first word spoken in a sentence. For instance, "Hey there, Jarvis, who are you?" will NOT trigger a response. However, "Jarvis, who are you?" will work as intended.
  
- A list of vocal commands is provided when you run the `Run.bat` file.

- You need Spotify Premium to use Jarvis's music features.


# Spotify Client ID and Client Secret Setup

Follow the steps below to obtain your Spotify Client ID and Client Secret:

### Step 1: Create a Spotify Account
- If you don't already have one, sign up for a Spotify account on [Spotify's website](https://www.spotify.com/).

### Step 2: Access the Spotify Developer Dashboard
- Navigate to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/).
- Click on the "Log In" button.
- Use your Spotify account credentials to sign in.

### Step 3: Create a New App
- After logging in, click on the "Create an App" button.
- Provide the following information:
  - **App Name**: `Jarvis`
  - **App Description**: `Helpful voice assistant.`

### Step 4: Get Your Client ID and Client Secret
- You'll be taken to your app's dashboard after creation.
- Here, you'll find your **Client ID**, put this in the `apikey.py` file where it says to do so.
- Next to the Client ID is a "Show Client Secret" button. Click it to view your **Client Secret**, also put this in the `apikey.py` file where it says to do so.

### Step 5: Open Spotify
- Open Spotify website.
- Start Jarvis.
- Ask him to play any song or have him choose.


## Changelog
- **Added weather support to Jarvis:** Jarvis can now call a weather API and retrieve weather information by himself.
- You will not need a separate API key for this functionality.
- **Added spotify music playback:** Jarvis can now call the spotify API and retrieve spotify songs and play them by himself.
- Refer to Spotify Clien ID and Client Secret Setup to get it working, don't worry it's free.

## Contribute to Development
Feel free to submit feature requests and report issues for JarvisChatGPT. I'll consider implementing anything that's feasible and interesting.

