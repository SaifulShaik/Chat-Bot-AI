# Chat-Bot-AI
**Future updates to enhance functionality and features.**

## Table of Contents
1. [Introduction](#introduction)
2. [File Procedure](#file-procedure)
3. [JSON File](#json-file)
4. [Installation Instructions](#installation-instructions)
5. [API Key Setup](#api-keys)

## Introduction
Welcome to the Chat-Bot-AI project! This is a simple chatbot that’s currently in development. After spending some time troubleshooting and coding, the basic version is ready for interaction. Over the coming days, I will be adding more advanced features, including:

- **Natural Language Processing (NLP)**: To improve the bot’s understanding of user inputs.
- **Sentiment Analysis**: Enabling the bot to detect emotions and provide appropriate responses.
- **Machine Learning**: For continuous improvement as the bot learns from interactions.
- **Context-Awareness**: To make conversations more coherent.
- **Speech Recognition**: To add a voice-based interface.

Stay tuned for updates, and enjoy chatting with your very own bot!

## File Procedure
To run the chatbot project, ensure you have the following files:

1. **JSON File**: Contains patterns and responses that the bot uses to generate replies.
2. **Training.py**: A script used to train the bot and save the trained model.
3. **CB1.py**: The main chatbot application that loads the trained model, processes user input, and returns a response.

### Key Points:
- Always run **training.py** first to train the bot before usage.
- After running **training.py**, new files will be generated. Do not modify these, as they are essential for **CB1.py** to function properly.
- Run **CB1.py** to start interacting with the chatbot.

## JSON File
The **JSON file** defines the **intents** that the bot can handle. Each intent includes:

1. **Tag**: A unique identifier for the intent.
2. **Patterns**: A list of phrases the bot will recognize as belonging to this intent.
3. **Responses**: A list of possible replies the bot can give for this intent.
4. **Context**: This field is used to track the conversation state and influence future responses.

The chatbot uses this data to match user input to intents and generate relevant replies.

## Installation Instructions
Before you start, ensure that **Python** is installed on your system. Follow the steps below to set up the necessary dependencies:

### 1. Install Dependencies
If `pip` is not installed, you can download it from [here](https://pip.pypa.io/en/stable/installation/).

#### Installing NLTK
To install NLTK (Natural Language Toolkit), follow the steps below based on your system:

1. **Windows and Mac**:
    ```bash
    pip install nltk  # or pip3 install nltk if using Python 3
    ```

2. **Linux**:
    ```bash
    sudo pip install -U nltk  # or sudo pip3 install -U nltk if using Python 3
    ```

3. **Anaconda**:
    ```bash
    conda install -c anaconda nltk
    ```

#### Installing Keras
To install Keras, follow these instructions depending on your operating system:

1. **Windows and Mac**:
    ```bash
    pip install keras  # or pip3 install keras if using Python 3
    ```

2. **Linux**:
    ```bash
    pip3 install keras
    ```

3. **Anaconda**:
    ```bash
    conda install -c anaconda keras
    ```

## API Keys

An API key is required to access the weather information needed for the chatbot.

### Creating API Keys

Follow these steps to generate your API key from OpenWeatherMap:

1. Go to the [OpenWeatherMap website](https://openweathermap.org/).
2. Sign up for an account or log in if you already have one.
3. Once logged in, click on your username in the top-right corner of the page.
4. Click **My API Keys**.
5. You will see your default API key, or you can generate a new one by clicking **Generate**.
6. Name your new API key as **weather**.
7. Copy the API key that is generated.
8. Paste the API key into the **CB1.py** file where required.

### Bonus:
Having trouble? Feel free to report issues under the **Issues** section of the repository, and I’ll be happy to assist!
