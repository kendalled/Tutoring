# Import statements
import pandas as pd
import numpy as np
import scipy as sp
from scipy.stats import stats
import matplotlib.pyplot as plt

# 1.) Establishes arr1 as DataFrame from CSV
arr1 = pd.read_csv('data/Chapter9.csv')
diff_arr = []
res = []
print("Initial DataFrame: \n{}".format(arr1))
print("-----------------------------------")

# 2.) Adds all differences (Outdoor - Indoor) to a list (diff_arr)
for i in range(len((arr1['Concentration Outdoor']))):
    diff_arr.append(float(arr1['Concentration Outdoor'][i])-float(arr1['Concentration Indoor'][i]))

# 2-a.) Creates new df Column and assigns values from above
arr1['Difference'] = diff_arr
print("Difference Column: \n{}".format(arr1['Difference']))
print("-----------------------------------")

# 3.) Confidence Interval
def confidence_interval(data, confidence=0.95):
    a = 1.0 * np.array(data)
    n = len(a)
    m, se = np.mean(a), sp.stats.sem(a)
    h = se * sp.stats.t.ppf((1 + confidence) / 2., n-1)
    return m-h, m+h

# 4-a.) Adds CI of 'Difference Column' to empty list called res
res = confidence_interval(arr1['Difference'])

# Neatly Prints Output of confidence_interval using new arr1
print(arr1)
print("-----------------------------------")
print("Confidence Interval for Difference: {}".format(res))
