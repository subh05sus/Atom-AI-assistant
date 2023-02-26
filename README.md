# Atom-AI-assistant
Python Voice Assistant with ChatGPT and DALI
This is a Python voice assistant that is integrated with ChatGPT and DALI. With this assistant, you can perform a variety of tasks using natural language commands.

Features
Voice recognition for natural language commands
Integration with ChatGPT for chatbot functionality
Integration with DALI for smart home control
Requirements
Python 3.x
PyAudio (for voice recognition)
chatbot (for ChatGPT integration)
DALI driver (for DALI integration)
Installation
Clone the repository to your local machine.
Install the required packages using pip: pip install -r requirements.txt
Connect your DALI devices to your network and configure the DALI driver accordingly.
Usage
Start the assistant by running python main.py
Wait for the assistant to say "Ready" before giving a command.
Speak your command into the microphone. You can use natural language commands like "Turn on the lights" or "What's the weather like today?".
The assistant will respond to your command using text-to-speech technology.
Customization
You can customize the assistant's behavior by editing the config.json file. This file contains settings for the voice recognition module, the ChatGPT module, and the DALI module. You can adjust these settings to fit your needs.

Troubleshooting
If the assistant is not recognizing your voice commands, make sure that your microphone is connected and configured correctly.
If the ChatGPT module is not working correctly, make sure that you have an internet connection and that your API key is valid.
If the DALI module is not working correctly, make sure that your DALI devices are connected and configured correctly.
Credits
This project uses the ChatGPT library from OpenAI (https://openai.com/)
This project uses the DALI driver from Signify (https://www.signify.com/en-us/brands/dali)
