#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

# print enron_data['PRENTICE JAMES']['total_stock_value']
def max_key(dict, key):
    import operator
    index, value = max()
    return (index, value)

# total = [(k, v['total_payments']) for k,v in enron_data.iteritems() if (k == "SKILLING JEFFREY K" or 'LAY' in k or 'FASTOW' in k)]

# print max(total)
# print ([k for k,v in enron_data.iteritems() if (v['poi'] == 1)]);

# print (len([k for k,v in enron_data.iteritems() if (v['poi'] != 'NaN')]))

iter_enron = enron_data.iteritems()

poi = ([(k,v) for k,v in iter_enron if (v['poi'] == True)])
poi_no_pay = [(v['total_payments']) for k,v in poi ]
# if (v['total_payments'] == 'NaN')
no_total_payments = [k for k,v in enron_data.iteritems() if (v['total_payments'] == 'NaN')]
print len(poi)