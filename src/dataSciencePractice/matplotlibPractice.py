#Matplotlib is a python 2D plotting library providing features like plots, histograms, 
#power spectra, bar charts, error charts, scatter plots, etc., with just a few lines of code. 
#It provides the pyplot module which is quite similar to MATLAB providing a similar interface.

import matplotlib.pyplot as plt
import numpy as np
#from scipy.stats import itemfreq deprecated use pandas instead
import pandas as pd

def barGraphExcercise():
    #We read our file in this case a csv
    df = pd.read_csv('src/data/pokemon_alopez247.csv') 
    #We want to count the number of distinct groups belonging to that group
    #available under Type_1 category
    #We use scipy.stats itemfreq
    
    #We retrieve a list of group types against the number of pokemon belonging
    #to that group
    type_1, counts = np.unique(df.iloc[:, 2], return_counts=True)
    type_1_freq = np.asarray((type_1, counts)).T
    print(type_1_freq)
    
    # Total number of distinct groups
    type_1_grps = len(type_1_freq)
    print(type_1_grps)
    # Names of group
    type_1_names = type_1_freq[:,0]
    print(type_1_names)
    # Pokemon count particular to each group
    type_1_count = type_1_freq[:,1]
    print(type_1_count)
    
    #After gathering this data we can plot a bar graph against the variables
        
    type_1_grps = np.arange(type_1_grps)
    bar_width = 0.5
    plt.bar(type_1_grps, type_1_count, bar_width,
                    alpha = 0.5,   # tranparency factor
                    color = 'g',   # color factor
                    label='Pokemon count respective to their Type_1')
    plt.legend(loc='best')
    plt.xticks(type_1_grps + bar_width/2, type_1_names)
    
    #To show the plot
    plt.show()
    return

def multipleBarExcercise():
    #Given score points of Men and Women in a certain game played 5 times with the corresponding errors in the observations:
    #Plot a bar graph depicting scores for all 5 games along with errors in observation.
    n_grps = np.arange(5)
    bar_width = 0.4
    men_sc = [20, 30, 10, 50, 90]
    err_men_sc = [2, 3, 4, 5, 4]
    women = [10, 123, 19, 60, 40]
    err_women_sc = [1, 6, 2, 8, 7]
    
    #We use the bar function from matplotlib and we use the yerr parameter for error parameters
    plt.bar()
    
    return

barGraphExcercise()