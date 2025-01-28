#Matplotlib is a python 2D plotting library providing features like plots, histograms, 
#power spectra, bar charts, error charts, scatter plots, etc., with just a few lines of code. 
#It provides the pyplot module which is quite similar to MATLAB providing a similar interface.

import matplotlib.pyplot as plt
from matplotlib import animation
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
    men_sc = [20, 30, 10, 50, 90]
    err_men_sc = [2, 3, 4, 5, 4]
    women = [10, 123, 19, 60, 40]
    err_women_sc = [1, 6, 2, 8, 7]
    
    #Because we want to plot against 5 games, we need to construct our y axis
    n_grps=np.arange(5)
    #standard bar width
    width=0.4
    
    #We create the bar graphs
    plt.bar(n_grps,men_sc,width,yerr=err_men_sc,alpha=0.5,color='b',label='Men')
    plt.bar(n_grps+width,women,width,yerr=err_women_sc,alpha=0.5,color='r',label='Women')
    
    #We add the labels, titles and legends
    plt.xlabel('Game')
    plt.ylabel('Scores')
    plt.title('Masculine and Feminine scores in 5 games w/error')
    plt.legend()
    
    #show the plot
    plt.show()
    return

def pieChartExample():
    #Create a copy of the Dataframe with selected columns
    df_pie = df[['Type_1', 'Attack', 'Defense', 'Speed', 'HP']].copy()
    print(df_pie.head())#Prints first 5 rows
    
    #Calculate the frequency of each Type_1 category
    frequent_grp = itemfreq(df_pie.iloc[:,0])#DEPRECATED METHOD
    #Converts to aray and sorts by frequency in descending order, then selects top 4 most frequent groups
    frequent_grp = np.array(sorted(frequent_grp, key=lambda x: x[1]))[::-1][0:4,:]
    print(frequent_grp)
    
    #Filters df to include only rows where type_1 column contains one of the specified category
    df_pie = df_pie.loc[df_pie.loc[:,'Type_1'].str.contains(r'(Water|Normal|Grass|Bug)')]
    print(df_pie)
    
    # Names of the group
    type_1_names = frequent_grp[:,0]
    print(type_1_names)
    # Mean of samples for each feature corresponding to all 4 group 
    df_grp = df_pie.groupby('Type_1').mean()
    print(df_grp)
    
    names = df_grp.columns
    colors = ['gold', 'lightcoral', 
                'yellowgreen', 'lightskyblue']
    explode = (0, 0, 0, 0.1)  # takes out only the 4th slice 
    fig, [[ax1, ax2], [ax3, ax4]] = plt.subplots(nrows=2, ncols=2)
    ax = [ax1, ax2, ax3, ax4]
    for i in range(0,4):
        percent = df_grp.iloc[i,:]
        ax[i].pie(percent, explode = explode,
                labels = names, colors = colors,
                autopct='%.2f%%',   # display value
                shadow=True,
                startangle=90)
        ax[i].set_aspect('equal')
        ax[i].set_title(type_1_names[i])
    plt.suptitle('Comparing major features of 4 most frequent Pokemon Group',
                fontsize = 14,
                fontweight = 'bold')

    return

def animationTest():
    n = 30
    x = np.arange(0,1,0.001)
    y = np.ones( (1000,n) )
    for i in range(0,n):
        y[:,i] = np.sin(2 * np.pi * x) * i+1
    def func(arg):
        plt.cla()   #Clear axis
        plt.plot(y[:,arg])
        plt.ylim(-30,30)
    fig = plt.figure(figsize=(5,4))
        
    to_save = animation.FuncAnimation(fig, func, frames=30)
    plt.show()
    return

def scatterPlotExample():
    #Beginning of example
    return

animationTest()