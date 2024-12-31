#################################
#                               #
#                               #
#                               #
#           Chat Bot AI         #
#      Made By: Saiful Shaik    #
#                               #
#                               #
#                               #
#################################

import random
import json
import pickle
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer
from keras.api.models import load_model
import requests
import openai
import re  # For detecting math expressions

# DO NOT SHARE YOUR API KEY
openai.api_key = 'YOUR_API_KEY'  # Replace YOUR-API-KEY with your OpenAI API key
lemmatizer = WordNetLemmatizer()
intents = json.loads(open('intents.json').read())
words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))
model = load_model('chatbotmodel.h5')

def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]
    return sentence_words

def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag)

def predict_class(sentence):
    bow = bag_of_words(sentence)
    res = model.predict(np.array([bow]))
    
    ERROR_THRESHOLD = 0.1  # Lowered the threshold for better recognition
    results = []
    for i, r in enumerate(res[0]):
        if r > ERROR_THRESHOLD:
            results.append([i, r])
    
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    
    for r in results:
        return_list.append({'intent': classes[r[0]], 'probability': str(r[1])})
    
    return return_list

def get_response(intents_list, intents_json):
    tag = intents_list[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if i['tag'] == tag:
            return random.choice(i['responses'])
    return "I'm not sure how to respond to that. Can you please clarify?"

def get_weather(location):
    api_key = "YOUR_API_KEY"  # DO NOT SHARE YOUR API KEY
    api_url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"
    response = requests.get(api_url)
    weather_data = response.json()
    if 'main' in weather_data and 'weather' in weather_data:
        temperature_kelvin = weather_data["main"]["temp"]
        temperature_celsius = temperature_kelvin - 273.15
        description = weather_data["weather"][0]["description"]
        return f"Current weather in {location}: Temperature: {temperature_celsius:.2f}°C, Description: {description}"
    else:
        return "Failed to retrieve weather data for the specified location."

def get_openai_response(user_input):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003", 
            prompt=user_input,
            max_tokens=150,
            temperature=0.7
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return "Sorry, I couldn't process that. Please try again."

def solve_math_expression(expression):
    try:
        # Convert worded math expressions to Python-compatible syntax
        expression = expression.lower()

        # Replace worded expressions with Python symbols
        expression = expression.replace("to the power of", "**")
        expression = expression.replace("times", "*")
        expression = expression.replace("plus", "+")
        expression = expression.replace("minus", "-")
        expression = expression.replace("divided by", "/")
        expression = expression.replace("mod", "%")

        # Remove any unwanted characters to avoid errors
        expression = re.sub(r'[^0-9+\-*/().** ]', '', expression)
        result = eval(expression)
        return f"The answer is: {result}"
    except Exception as e:
        return "Sorry, I couldn't solve that math problem."

print("Welcome to CB1, how can I help you today?")

while True:
    message = input("")
    if message.lower() == 'exit':
        print("Goodbye! Have a nice day.")
        break
    
    if re.search(r'\d+', message):  # Checks if the message contains numbers
        print(solve_math_expression(message))
    else:
        ints = predict_class(message)
    
        if ints:
            # Check if the model recognized a valid intent
            if ints[0]['intent'] == 'weather':
                location = input("Enter your location (city, country): ")
                print(get_weather(location))
            else:
                print(get_response(ints, intents))
        else:
            print("Sorry, I didn't understand that. Can you try again?")
