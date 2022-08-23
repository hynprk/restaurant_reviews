#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 17:36:48 2022

@author: hyoeungracepark
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer # text -> vector
from sklearn.svm import SVC # to build model
from sklearn.metrics import accuracy_score
import numpy as np
import matplotlib.pyplot as plt



# Import dataset to Spyder
## read_csv does not work b/c some cells are NA
review_df = pd.read_table("data/Restaurant_Reviews.csv")


# Assigning the inputs to X and outputs to y
X = review_df['Review'].values
y = review_df['Liked'].values

# Add CountVectorizer
## Transforms text into a vector that counts the number of each word
cv = CountVectorizer()

# Add Support Vector Classifier
review_model = SVC()

# Arrays to store train and test set accuracies
size = np.arange(0.05, 1, 0.05)
length = len(size)
train_accuracy = np.empty(length)
test_accuracy = np.empty(length)

# Loop over different values of s
for s in size:
    # Split training and testing data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = s,
                                                        random_state = 42)
    
    # Apply CountVectorizer to train and test inputs
    X_train_cv = cv.fit_transform(X_train)
    X_test_cv = cv.transform(X_test)
    
    # Fit the svc model to the training data
    review_model.fit(X_train_cv, y_train)
    
    # Predict model on training and testing
    y_pred_train = review_model.predict(X_train_cv)
    y_pred_test = review_model.predict(X_test_cv)
    
    #Compute accuracy on the training set
    train_accuracy[np.where(size == s)[0][0]] = accuracy_score(y_pred_train, y_train)

    #Compute accuracy on the testing set
    test_accuracy[np.where(size == s)[0][0]] = accuracy_score(y_pred_test, y_test)

# Generate plot with matplotlib.pyplot
plt.title('Support Vector Classification: Varying Testing Size')
plt.plot(size, train_accuracy, label = 'Training Accuracy')
plt.plot(size, test_accuracy, label = 'Testing Accuracy')
plt.legend()
plt.xlabel('Testing Set Size')
plt.ylabel('Accuracy')
plt.show()

max_test = np.max(test_accuracy)
print("Maximum testing prediction accuracy is {}".format(max_test), 
      "when test size is {}".format(size[np.where(test_accuracy == max_test)[0][0]]))
    
# Creating training and testing datasets
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 42, 
                                                    test_size = 0.30)


# Adding CountVectorizer to train and test inouts
X_train_cv = cv.fit_transform(X_train)
X_test_cv = cv.transform(X_test)

# Fitting model to training data
review_model.fit(X_train_cv, y_train)


# Predict model
y_pred = review_model.predict(X_test_cv)

# Accuracy
pred_acc = accuracy_score(y_pred, y_test)
print("Prediction Accuracy: {}".format(pred_acc))


###### END OF CREATING MODEL #####

tripadvisor_df = pd.read_csv("data/tripadvisor_raw.csv")

comments = tripadvisor_df["Comments"].values
comments_cv = cv.transform(comments)

good_bad = review_model.predict(comments_cv)
tripadvisor_df['good_bad'] = good_bad

# Create csv file
tripadvisor_df.to_csv("data/tripadvisor_newcol.csv")








