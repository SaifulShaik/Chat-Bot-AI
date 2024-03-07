




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

















import json
import requests
import numpy as np

import nltk
from nltk.stem import WordNetLemmatizer

from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.optimizers import SGD

import pickle
import random

lemmatizer = WordNetLemmatizer()

# dictionary
intents = json.loads(open('intents.json').read())

words = []
classes = []
documents = []
ignore_letters = ['!', '?', ',', '.']


for intent in intents['intents']:
    for pattern in intent['patterns']:
        word_list = nltk.word_tokenize(pattern)
        words.extend(word_list)
        documents.append((word_list, intent['tag']) )
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

words = [lemmatizer.lemmatize(word) for word in words if word not in ignore_letters]
words = sorted(set(words))

classes = sorted(set(classes))

pickle.dump(words, open('words.pkl', 'wb'))
pickle.dump(classes, open('classes.pkl', 'wb'))


training = []
output_empty = [0] * len(classes)

for document in documents:
    bag = []
    word_patterns = document[0]
    word_patterns = [lemmatizer.lemmatize(word.lower()) for word in word_patterns]
    for word in words:
        bag.append(1) if word in word_patterns else bag.append(0)

    output_row = list(output_empty)
    output_row[classes.index(document[1])] = 1
    training.append([bag, output_row])

random.shuffle(training)
max_words = len(words)
max_classes = len(classes)

train_x = []
train_y = []

for bag, output_row in training:
    # Padding or trimming bag to max_words
    bag = bag[:max_words] + [0] * (max_words - len(bag))
    
    # Padding or trimming output_row to max_classes
    output_row = output_row[:max_classes] + [0] * (max_classes - len(output_row))
    
    train_x.append(bag)
    train_y.append(output_row)

train_x = np.array(train_x)
train_y = np.array(train_y)


model = Sequential()
#input layer with 128 neurons and an input shape depended on the size of the training data, activation funtion to be an actifed linear unit
model.add(Dense(128, input_shape = (len(train_x[0]),), activation='relu'))
# in order to prevent overflow
model.add(Dropout(0.5))
# dense layer with 64 nurons
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
# activaction softamx sums up or scales the results which equals to 1 
model.add(Dense(len(train_y[0]), activation='softmax'))

# sacastic gradient learning rate 0.01 | decay of 1e-6| momentem of 0.9
sgd = SGD(lr=0.05, momentum=0.9, nesterov=True)
#loss function we are going to chose is catagorical_crossentrophy 
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])
# epochs is how much times it will iterate
hist = model.fit(np.array(train_x), np.array(train_y), epochs = 200, batch_size = 6, verbose=1)
model.save('chatbotmodel.h5', hist)
print("Finished Training...")



