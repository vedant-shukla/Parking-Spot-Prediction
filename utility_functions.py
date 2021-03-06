
# coding: utf-8

# In[5]:


import pandas as pd
from math import sqrt
from sklearn.metrics import mean_squared_error
import numpy as np

#actual = actual values of y data
#predicted - predicted values of the test set
#y_test set which comprises of 100 values
actual_ = [82, 94, 94, 99, 114, 118, 129, 137, 142, 151, 161, 161, 161, 161, 161, 161, 161, 161, 130, 97, 78, 66, 64, 70, 74, 82, 94, 115, 136, 151, 160, 161, 161, 161, 161, 161, 161, 161, 161, 161, 161, 161, 126, 74, 47, 39, 31, 30, 38, 47, 61, 89, 122, 145, 161, 161, 161, 161, 161, 161, 161, 161, 161, 161, 161, 159, 123, 100, 69, 45, 38, 44, 41, 51, 63, 92, 128, 139, 156, 160, 160, 161, 161, 161, 161, 161, 161, 161, 161, 159, 138, 85, 51, 34, 36, 40, 44, 49, 58, 100]
def rms(predicted,actual=actual_):
    return sqrt(mean_squared_error(actual, predicted))

def r2(predicted,actual=actual_):
    mean_actual = np.mean(actual)
    actual = np.array(actual)
    predicted = np.array(predicted)
    rss = np.sum((actual-predicted)**2)
    tss = np.sum((actual-mean_actual)**2)
    final = 1 - (rss/tss)
    return final

def accuracy_tolerance(pred_set,act_set=actual_,  tolerance=10.0):
    if len(pred_set) != len(act_set):
        raise ValueError('prediction and actual set lengths dont match')
    
    n = len(pred_set)
    count = 0
    for i in range(n):
        if abs(pred_set[i] - act_set[i]) <= tolerance: count += 1
    acc = float(count) / float(n)
    return acc

def calculate_accuracy(predicted,model_name='No Name',actual=actual_):
    #call this function to get all accuracies as a dictionary
    d = {}
    d['name'] = model_name
    d['r2'] = r2(actual,predicted)
    d['tol'] = accuracy_tolerance(actual,predicted)
    d['rms'] = rms(actual,predicted)
    return d

def plot_graph(y_pred, y_act=actual_):
    # y_pred : 1D array predicted values
    # y_act : 1D array actual values
    if (len(y_act)!=100):
        raise ValueError('Test set should contain 100 values only')
    if (len(y_pred) != len(y_act)):
        raise ValueError('actual and predicted values dont have the same lengths')
        
    x = [i for i in range(len(y_pred))]
    plt.figure(figsize=(8, 4))
    plt.plot(x, y_pred, 'r-', label='Predicted')
    plt.plot(x, y_act, 'b-', label='Actual')
    axes = plt.gca()
    axes.set_ylim([0, 200])
    plt.ylabel('available spots')
    plt.xlabel('time')
    plt.legend(loc='best')
#     plt.xticks(x)
    plt.legend()
    plt.show()
