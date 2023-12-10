# Security Policy

I take security seriously in JarvisChatGPT to ensure the safety and privacy of our users and their data.

## Data Security

- **Local Data**: All data within the JarvisChatGPT application is kept local on the user's device and is not transmitted or shared with external parties.

- **OpenAI API**: Interaction with the OpenAI API for generating responses is managed securely through OpenAI's infrastructure. Data sent to the API is subject to OpenAI's own security measures and practices.

- **Outgoing data**: The only data being sent outside your computer is the response to OpenAI's servers, and what song you wanted to play on Spotify through Spotify's servers. Both of these are sent securely through each of their API's and they both have user identification keys that you provided to use it. Weather information is requested through an API but no data is sent, it just asks for all weather data and Jarvis formats it later, this feature also uses an API key of my own and it is secure, everything is secure and privite.

- **Other features**: All other features not mentioned here are 100% local on your computer, all memory files are stored and created on device, all User and Jarvis messages are deleted after closing the app, all voice files are deleted after being played, all speech is generated on device, all recorded speech is deleted after the listening message disappears, and all calculations are not saved anywhere.

- **NOTE**: If you share your folder with Jarvis, even if you deleted the api key out of the api key file, it will still show up in cache and anyone else could use it and read it, to fix this, deleted pycache from the folder and you're all set.

## Reporting Security Vulnerabilities

If you discover a security vulnerability in JarvisChatGPT, I encourage you to responsibly disclose it by submitting an issue through GitHub's issue tracker.

To report a security vulnerability:
- Go to the [Issues tab](https://github.com/antmannacho/J.A.R.V.I.S.-ChatGPT-VoiceAssistant/issues) on the GitHub repository.
- Click on the "New Issue" button.
- Select the "Security Vulnerability" issue template.
- Provide a clear and detailed description of the vulnerability.

I will thoroughly investigate and address all reported security vulnerabilities in a timely manner. Your cooperation is invaluable in upholding the security of JarvisChatGPT.

## Responsible Disclosure

I kindly request that you:
- Allow me a reasonable amount of time to respond to your report before making it public.
- Avoid unauthorized access, modification, or damage to other users' data.
- Adhere to relevant laws and regulations when reporting security issues.

Thank you for collaborating with me to maintain the security and privacy of JarvisChatGPT. Your assistance is vital to our commitment to data security.
