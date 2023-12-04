# 🎙️ JarvisChatGPT

**JarvisChatGPT**, or **Jarvis**, is your very own AI voice assistant powered by the same techonology as ChatGPT using OpenAI's API. It's built to be simple and conversational just like the Jarvis AI from the movies. Think of it like Siri or Alexa, but WAY better.

**Last Updated**: December 2nd, 2023 (12-2-23)

**OS Support**: Windows, MacOS later in the future.

By default, Jarvis utilizes the **GPT-3.5-Turbo** API model. However, if you fancy an upgrade, you can easily transition to **GPT-4** via the `main.py` file.

⚠️ **Important**: To harness the power of Jarvis, you'll need an **OpenAI API key**. Insert this key in the `apikey.py` file.

## 🚀 Quick Start
1. **Setup Python**: Ensure you have Python installed. If not, [download Python](https://www.python.org/downloads/).
2. **Install Dependencies**: Simply run `install.bat`.
3. **Launch Jarvis**: Run `Run.bat`. Should you encounter any hiccups, dive into the troubleshooting section.

## 🔍 Troubleshooting
- **Initial Issues**: If `Run.bat` closes abruptly, manually open a terminal in the Jarvis directory and input:
  ``` shell
  python main.py
  ```
- **Installation Failures**: Facing issues with `install.bat`? Manually install the required packages:
  ``` shell
  python install pip
  ```
  Then run:
  ``` shell
  pip install openai SpeechRecognition pyttsx3 pyaudio spotipy
  ```
- **Spotify Playback Errors**: Ensure you have an active Spotify session and check if you've entered correct Spotify credentials. Also, a premium account is a must-have or it won't work.
- **Mic Troubles**: Navigate to the control panel, access sound settings, select the recording tab, and set your mic as the default device.

## 📌 Key Features & Tips
- 🚫 Jarvis has **no token limit**. This means lengthier requests might have you twiddling your thumbs for a bit.
- 🛠️ Dive into `main.py` for customization options. Use `CTRL + F` and search for `system_prompt =` or `startswith("jarvis")` to swiftly locate and modify system prompts or wake word configurations.
- 🎤 For optimal performance, ensure the wake word, "Jarvis", starts your sentence.
- 🎵 Fancy some tunes? Remember, you need Spotify Premium for Jarvis's music features. 

## 🎵 Spotify Integration
Follow the steps below to set up Spotify integration:

### 1️⃣ Create a Spotify Account
Start by [creating or accessing your Spotify account](https://www.spotify.com/).

### 2️⃣ Access the Spotify Developer Dashboard
- Navigate to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/) and sign in.
  
### 3️⃣ Create a New App
- After logging in, click on the "Create an App" button.
- Fill in:
  - **App Name**: `Jarvis`
  - **App Description**: `Helpful voice assistant`

### 4️⃣ Get Your Client ID and Client Secret
- On your app's dashboard, locate your **Client ID** and enter it in the `apikey.py` file.
- Click "Show Client Secret" to retrieve your **Client Secret** and add it to the `apikey.py` file as well.

### 5️⃣ Jam With Jarvis
Initiate Jarvis and request your favorite songs!

## 📜 Changelog
- **Weather Updates**: Jarvis now boasts a built-in weather API.
- **Spotify Integration**: Dance away with Jarvis's Spotify playback feature.
- **Calculator**: Jarvis will now crunch numbers for you.
- **Permanent Memory**: Jarvis will remember tidbits for you. If ever needed, he can also be asked to forget.
- **Timekeeper**: Ask Jarvis for the current date and time.
- **Expanded Weather Data**: More comprehensive data about the skies above.

## 🤝 Contribute
Your feedback is gold! Please suggest features or report issues. Let's refine JarvisChatGPT together.
