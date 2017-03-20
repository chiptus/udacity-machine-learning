#!/usr/bin/python
from heapq import nsmallest

def get_error_key(w):
    return w[2]

def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    data = [(ages[i][0], net_worths[i][0], predictions[i][0] - net_worths[i][0]) for i in range(len(predictions))]
    cleaned_data = nsmallest(int(0.9 * len(predictions)), data, lambda d: d[2])
    # print len(cleaned_data), len(predictions)
    ### your code goes here

    
    return cleaned_data

