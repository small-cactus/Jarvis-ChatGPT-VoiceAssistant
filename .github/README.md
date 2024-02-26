# 🎙️ JarvisChatGPT

**JarvisChatGPT**, or simply **Jarvis**, is your cutting-edge AI voice assistant, leveraging the sophisticated technology behind ChatGPT and OpenAI's API for a user experience that far surpasses conventional assistants like Siri or Alexa. It's designed to be both simple for casual interaction and powerful for more complex tasks, reminiscent of the Jarvis AI from popular films.

**Last Updated**: December 12th, 2023 (12-12-23)

**Important Update**: We've moved on from the old repository and shifted our focus to a significantly improved version, known as **M.I.L.E.S**. Although the original **JarvisChatGPT** repo is not actively updated, we're still committed to addressing any issues that arise, provided there isn't an available workaround. 

For a better, more refined AI voice assistant experience, especially tailored for Mac users, check out our new and enhanced repository:

🌟 **[Visit the updated M.I.L.E.S repository](https://github.com/small-cactus/M.I.L.E.S)** 🌟

This latest version promises an enhanced performance with an installation process that is notably straightforward on MacOS. Windows users, please be informed that while support exists, the installation process can be significantly more challenging and might not succeed in every case. We primarily recommend this for Mac users, though Windows users willing to navigate the complexities are welcome to try.

**OS Support**: Optimized for MacOS. Windows compatibility exists but with potential installation challenges.

By default, Jarvis utilizes the **GPT-3.5-Turbo** API model. However, if you fancy an upgrade, you can easily transition to **GPT-4** via the `main.py` file.

⚠️ **Important**: To harness the power of Jarvis, you'll need an **OpenAI API key**. Insert this key in the `apikey.py` file.

## 🚀 Quick Start
1. **Setup Python**: Ensure you have Python installed. If not, [download Python](https://www.python.org/downloads/).
2. **Install Dependencies**: Simply run `install.bat`.
3. **Launch Jarvis**: Run `Run.bat`. Should you encounter any hiccups, dive into the troubleshooting section.
4. **Have Fun!**

## 💬 Share with your friends
  The people that clone, download, and view jarvis are what makes this possible for me to not lose motivation. *Please share Jarvis* with a link to this page! **Everyone has permission to share this anywhere they want**, post my projects anywhere you want!!
#

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
  pip install openai==0.28.1 SpeechRecognition pyttsx3 pyaudio spotipy
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
  - **Redirect URL**: `http://localhost:8080/callback`

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
