# ChatGPT Chatbot

## Overview

This project is a simple chatbot application that uses the OpenAI ChatGPT API to provide conversational responses. The chatbot is built using Python and allows users to interact with the model via a command-line interface.

## Features

- Interactive command-line chatbot
- Integration with OpenAI's ChatGPT API
- Simple setup and usage

## Prerequisites

1. **Python**: Make sure you have Python 3.6 or higher installed. You can download it from [python.org](https://www.python.org/downloads/).
2. **OpenAI API Key**: You need an API key from OpenAI. You can obtain it by signing up at [OpenAI](https://platform.openai.com/signup) and generating an API key from the [API keys page](https://platform.openai.com/account/api-keys).

## Setup Instructions

1. **Clone the Repository**

   Clone the repository to your local machine:

   ```sh
   git clone https://github.com/yourusername/chatgpt-chatbot.git
   cd chatgpt-chatbot

## Create a Virtual Environment (Optional)
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

## Install Dependancies
pip install requests

## config API
Open the chatbot.py file in a text editor and replace 'your-api-key-here' with your actual OpenAI API key: ```API_KEY = 'your-actual-api-key```'

## Create .gitignore File
Ensure you have a .gitignore file to exclude sensitive files like .env from version control. If you need to create one.

## Running App
### Run script
1. **Run the Python Script**

      Execute the chatbot.py script: ```python chatbot.py```

2. **Interact with chat bot**

     * Type your messages to interact with the chat bot
     * Type ```exit``` to end conversation


