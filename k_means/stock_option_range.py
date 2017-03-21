import pickle
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
### there's an outlier--remove it! 
data_dict.pop("TOTAL", 0)

def find_key(data_dict, filter_func, sub_key):
  def key_func(x):
    return data_dict[x][sub_key]
  key = filter_func(data_dict, key=key_func)
  print key, ":", data_dict[key][sub_key]

def get_range(data_dict, key):
  data_dict_no_nan = {k:v for (k,v) in data_dict.iteritems() if (v[key] != "NaN")}
  max_range = find_key(data_dict_no_nan, max, key)
  min_range = find_key(data_dict_no_nan, min, key)



print "exercised_stock_options"
get_range(data_dict, "exercised_stock_options")

print "salary"
get_range(data_dict, "salary")