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

import ssl
import json
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer
from keras.src.models import Sequential
from keras.src.layers import Dense, Dropout
from keras.src.optimizers import Adam
from keras.src.callbacks import EarlyStopping
import pickle
import random
from pathlib import Path

# Fix SSL context for downloading nltk resources
ssl._create_default_https_context = ssl._create_unverified_context

# Download necessary nltk data
nltk.download('punkt', quiet=True)
nltk.download('wordnet', quiet=True)

# Initialize lemmatizer
lemmatizer = WordNetLemmatizer()

# Load intents file
def load_intents():
    try:
        with open('intents.json') as file:
            intents = json.load(file)
        return intents
    except FileNotFoundError:
        print("Error: intents.json file not found.")
        exit()

intents = load_intents()

# Initialize lists
words = []
classes = []
documents = []
ignore_letters = ['!', '?', ',', '.']

# Preprocess data
def preprocess_data():
    for intent in intents['intents']:
        for pattern in intent['patterns']:
            word_list = nltk.word_tokenize(pattern)
            words.extend(word_list)
            documents.append((word_list, intent['tag']))
            if intent['tag'] not in classes:
                classes.append(intent['tag'])

    words_lemmatized = [lemmatizer.lemmatize(word.lower()) for word in words if word not in ignore_letters]
    return sorted(set(words_lemmatized)), sorted(set(classes))

words, classes = preprocess_data()

# Save words and classes
def save_data():
    try:
        pickle.dump(words, open('words.pkl', 'wb'))
        pickle.dump(classes, open('classes.pkl', 'wb'))
        print("Saved words and classes to disk.")
    except Exception as e:
        print(f"Error saving data: {e}")
        exit()

save_data()

# Create training data
training = []
output_empty = [0] * len(classes)

for document in documents:
    bag = []
    word_patterns = document[0]
    word_patterns = [lemmatizer.lemmatize(word.lower()) for word in word_patterns]
    for word in words:
        bag.append(1 if word in word_patterns else 0)

    output_row = list(output_empty)
    output_row[classes.index(document[1])] = 1
    training.append([bag, output_row])

random.shuffle(training)
training = np.array(training, dtype=object)

train_x = np.array(list(training[:, 0]))
train_y = np.array(list(training[:, 1]))

# Build model
model = Sequential()
model.add(Dense(128, input_shape=(len(train_x[0]),), activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(len(train_y[0]), activation='softmax'))

# Compile model
adam = Adam(learning_rate=0.001)
model.compile(loss='categorical_crossentropy', optimizer=adam, metrics=['accuracy'])

# Add early stopping
early_stopping = EarlyStopping(monitor='loss', patience=3, restore_best_weights=True)

# Train model
def train_model():
    try:
        hist = model.fit(train_x, train_y, epochs=200, batch_size=6, verbose=1, callbacks=[early_stopping])
        model.save('chatbotmodel.h5')
        print("Finished Training...")
    except Exception as e:
        print(f"An error occurred during training: {e}")
        exit()

train_model()