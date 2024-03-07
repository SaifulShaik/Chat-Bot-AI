# Chat-Bot-AI
- **Adding more features later on**
## Introduction
Hello everyone!

I've spent the past three days coding and troubleshooting, leaving me with little time to work on new projects. Nonetheless, I've developed a basic chatbot that's ready for interaction. Over the next few days, I'll focus on enhancing its features and functionality as much as possible. Stay tuned for updates!

To enhance my Python chatbot project, I'll make sure to integrate natural language processing for better understanding, sentiment analysis for emotional context so it can make you feel better, and machine learning for continuous improvement. Additionally, I'll add context-awareness for coherent dialogues and deploy it across various platforms for wider accessibility, aiming to create a more intelligent and user-friendly experience. Lastly, I am thinking of integrating a speach recognition feature to this project. I hope you enjoy your very own simple Chat Bot to talk with.

## File Procejure
To run the project, you'll need the JSON file, the training.py file, and the CB1.py file. These files work together to execute the chatbot project successfully.

1. Json File: The json file is where you can write your patterns and and responses for your bot to read. **SCROLL DOWN TO LEARN MORE**
2. Training.py File: 
3. CB1.py: This Python script is the main chatbot application. It loads the trained model, reads user input, predicts the intent of the input using the model, and generates an appropriate response based on the predicted intent and the responses defined in the JSON file.

**KEY POINT:** 
- ALWAYS RUN THE TRAINING PY FIRST AFTER MAKING CHANGES FOR THE BOT TO WORK.
- AFTER RUNNING THE TRAINING FILE YOU WILL GET MULTIPLE OTHER FILES. DO NOT TOUCH THEM THEY ARE NEEDED FOR THE CB1.PY FILE WHEN IT IS RUNNED.
- RUN THE CB1.PY FILE FOR THE FRONT PAGE.

## Json File
The JSON file contains a collection of "intents", where each intent represents a specific action or query that the chatbot can handle. Each intent has three main components:

1. Tag: A unique identifier for the intent. This tag is used to identify the intent when processing user input.

2. Patterns: A list of patterns or phrases that users might use to express the intent. These patterns are used to train the chatbot to recognize the intent based on user input.

3. Responses: A list of possible responses that the chatbot can give when the intent is recognized. These responses are randomly selected to provide variety in the chatbot's interactions.

4. Context: The "context" field is typically used to indicate a specific context or state that the conversation is in after a particular intent is recognized. This allows the chatbot to remember and track information about the conversation, which can influence how it responds to subsequent user inputs.

## Installments


## API Keys
An API key will access the information needed for the weather network.

### Creating API Keys
1. Go to the website OpenWeatherMap
2. Make an account for your API Key
3. On the top-right corner of the website you will see your username
4. Tap your username
5. After tapping your username, click my API Keys
6. After accessing the page, you will see a API Key which is your defult
7. Generate an API Key Named weather
8. Copy the API Key after genatrated and use that API Key in the CB1.py file
9. You've done it!




