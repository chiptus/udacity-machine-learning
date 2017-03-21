import pickle
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
### there's an outlier--remove it! 
data_dict.pop("TOTAL", 0)

eso_no_nan = {k:v for (k,v) in data_dict.iteritems() if (v["exercised_stock_options"] != "NaN")}

def key(x):
  return eso_no_nan[x]['exercised_stock_options']
max = max(eso_no_nan, key=key)
print max, ":", eso_no_nan[max]['exercised_stock_options']
min = min(eso_no_nan, key=key)
print min, ":", eso_no_nan[min]['exercised_stock_options']
