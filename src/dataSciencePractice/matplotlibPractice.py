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
    df = pd.read_csv('src/data/pokemon_alopez247.csv')
    
    #iloc[] to select all rows (:) and the 4th column (4), and store it in tot_power
    tot_power = df.iloc[:,4]
    print(tot_power.head(4)) #We print first 4 rows
    #We do the same thing, all rows from the 21st column on catch_rate
    catch_rate = df.iloc[:,21]
    print(catch_rate.head(4)) #We print first 4 rows
    #subplots creates a figure (fig) and an axes object (ax)
    fig, ax = plt.subplots()
    #ax.scatter(x,y,c='g') creates the scatter plot with x being catch_rate, tot_power being y axis
    #and g being color green
    p = ax.scatter(catch_rate, tot_power, c = 'g')
    #following commands only give label names to the plot
    ax.grid()
    ax.set_xlabel('Catch Rate')
    ax.set_ylabel('Total Power')
    ax.set_title('Pokemon Catch Rate vs their Power')
    plt.legend([p],['Pokemons'])
    plt.show()
    return

def lineChartExample():
    df = pd.read_csv('src/data/pokemon_alopez247.csv')
    #We extract specific set of columns from a specific row
    #df.iloc[0,4:11] takes row 0  columns from 4 to 10 (11 is excluded)
    #df.iloc[3,4:11] takes row 3 columns from 4 to 10  (11 is excluded)
    #df.iloc[6,4:11] takes row 6 columns from 4 to 10  (11 is excluded)
    #The values are converted into a list
    bulbasaur = list(df.iloc[0,4:11])
    charmander = list(df.iloc[3,4:11])
    squirtle = list(df.iloc[6,4:11])
    pokets = [bulbasaur, charmander, squirtle]
    # Converting height from meters to inches
    # Weight remains in kg
    # we store these values in a list
    bul_hw = [df.iloc[0,19]*3.281, df.iloc[0,20]]
    char_hw = [df.iloc[3,19]*3.281, df.iloc[3,20]]
    squ_hw =  [df.iloc[6,19]*3.281, df.iloc[6,20]]
    hw = [bul_hw, char_hw, squ_hw]
    #Creates figure with ID of 0 that will contain subplots
    fig = plt.figure(0)
    # Line plot
    #Grid Size of 4x3, starting at 0,0 and spanning 3 columns in first row
    ax1 = plt.subplot2grid((4,3), (0,0), colspan=3)
    ax1.plot(bulbasaur,'g-',bulbasaur,'go') #g- is green line 'go' is green circles
    ax1.plot(charmander,'r-',charmander,'ro')#r- is red line 'ro is red circles
    ax1.plot(squirtle,'b-',squirtle,'bo')#b- is blue line 'bo' is blue circles
    ax1.set_xlim(-0.3,6.3) #sets x axis limits from 0.3 to 6.3
    ax1.set_ylim(0,350) #Set Y-axis limits
    ax1.set_yticks(range(0,350,50)) #Show ticks every 50 units
    
    #We define specific coordinates from our plot
    text_x_coord = [0.045, .19, 0.34, 0.49, 0.64, 0.795, 0.945]
    text_y_coord = [0.7, 0.57, 0.65, 0.75, 0.75, 0.75, 0.72]
    rot = [0, 45, 45, 45, 45, 45, 45] #rot of labels
    txt = [r'$T_{OTAL}$', r'$HP$', r'$A_{TTACK}$', r'$D_{EFENSE}$',
        r'$S_{P}\_A_{TK}$',r'$S_{P}\_D_{EF}$',r'$S_{PEED}$'] # text is in TEX format
    for i in range(0, 7):
        ax1.text(text_x_coord[i], text_y_coord[i], txt[i],
                transform = ax1.transAxes,  # makes width and height in percentage
                va = 'top',
                rotation = rot[i],
                bbox = dict(
                        boxstyle = 'round',
                        facecolor = 'wheat',
                        alpha = 0.78))  # alpha -> transparency
    plt.show()
    return

def boxPlotExample():
    df = pd.read_csv('src/data/pokemon_alopez247.csv')
    #We extract specific set of columns from a specific row
    #df.iloc[0,4:11] takes row 0  columns from 4 to 10 (11 is excluded)
    #df.iloc[3,4:11] takes row 3 columns from 4 to 10  (11 is excluded)
    #df.iloc[6,4:11] takes row 6 columns from 4 to 10  (11 is excluded)
    #The values are converted into a list
    bulbasaur = list(df.iloc[0,4:11])
    charmander = list(df.iloc[3,4:11])
    squirtle = list(df.iloc[6,4:11])
    pokets = [bulbasaur, charmander, squirtle]
    # Converting height from meters to inches
    # Weight remains in kg
    # we store these values in a list
    bul_hw = [df.iloc[0,19]*3.281, df.iloc[0,20]]
    char_hw = [df.iloc[3,19]*3.281, df.iloc[3,20]]
    squ_hw =  [df.iloc[6,19]*3.281, df.iloc[6,20]]
    hw = [bul_hw, char_hw, squ_hw]
    #Creates figure with ID of 0 that will contain subplots
    fig = plt.figure(0)
    # Line plot
    #Grid Size of 4x3, starting at 0,0 and spanning 3 columns in first row
    ax1 = plt.subplot2grid((4,3), (0,0), colspan=3)
    ax1.plot(bulbasaur,'g-',bulbasaur,'go') #g- is green line 'go' is green circles
    ax1.plot(charmander,'r-',charmander,'ro')#r- is red line 'ro is red circles
    ax1.plot(squirtle,'b-',squirtle,'bo')#b- is blue line 'bo' is blue circles
    ax1.set_xlim(-0.3,6.3) #sets x axis limits from 0.3 to 6.3
    ax1.set_ylim(0,350) #Set Y-axis limits
    ax1.set_yticks(range(0,350,50)) #Show ticks every 50 units
    
    #We define specific coordinates from our plot
    text_x_coord = [0.045, .19, 0.34, 0.49, 0.64, 0.795, 0.945]
    text_y_coord = [0.7, 0.57, 0.65, 0.75, 0.75, 0.75, 0.72]
    rot = [0, 45, 45, 45, 45, 45, 45] #rot of labels
    txt = [r'$T_{OTAL}$', r'$HP$', r'$A_{TTACK}$', r'$D_{EFENSE}$',
        r'$S_{P}\_A_{TK}$',r'$S_{P}\_D_{EF}$',r'$S_{PEED}$'] # text is in TEX format
    for i in range(0, 7):
        ax1.text(text_x_coord[i], text_y_coord[i], txt[i],
                transform = ax1.transAxes,  # makes width and height in percentage
                va = 'top',
                rotation = rot[i],
                bbox = dict(
                        boxstyle = 'round',
                        facecolor = 'wheat',
                        alpha = 0.78))  # alpha -> transparency

    # continuing from previous code
    #We create subplots in a 4x3 grid
    ax2 = plt.subplot2grid((4,3), (1,0), colspan=1)
    ax3 = plt.subplot2grid((4,3), (2,0), colspan=1)
    ax4 = plt.subplot2grid((4,3), (3,0), colspan=1)
    ax = [ax2, ax3, ax4]
    #colors for each box plot
    colors = ['g', 'r', 'b']
    #Loops iterating over the 3 subplots
    for i in range(0, 3):
        #box plot for each pokemon stat
        bp = ax[i].boxplot(pokets[i][1:],patch_artist=True)
        # Adding colors to edges
        #boxes - rectangular boxes
        #whiskers - vertical lines extending from boxes
        #fliers - outlier points
        #means, medians, caps are statistical markers
        #plt.setp(bp[element],color='k') sets color of all the elements to black
        for element in ['boxes', 'whiskers', 'fliers', 'means', 'medians', 'caps']:
                plt.setp(bp[element], color='k')
        # Adding color inside the box
        for patch in bp['boxes']:
            patch.set(facecolor=colors[i])
        ax[i].set_ylim(35,70)
        
    #Add an arrow shape pointing to the median
    ax3.annotate('Median', xy=(1.09, 51),xytext=(1.2, 60),
            arrowprops=dict(facecolor='wheat', 
                            shrink=0.001),)
    plt.show()
    return

def graphExcercise():
    x = np.arange(0.0, 5.0, 0.1)
    y = np.cos(2 * np.pi * x) * np.exp(-x)
    plt.plot(x,y); plt.show()
    return

def barPlotExample():
    df = pd.read_csv('src/data/pokemon_alopez247.csv')
    #We extract specific set of columns from a specific row
    #df.iloc[0,4:11] takes row 0  columns from 4 to 10 (11 is excluded)
    #df.iloc[3,4:11] takes row 3 columns from 4 to 10  (11 is excluded)
    #df.iloc[6,4:11] takes row 6 columns from 4 to 10  (11 is excluded)
    #The values are converted into a list
    bulbasaur = list(df.iloc[0,4:11])
    charmander = list(df.iloc[3,4:11])
    squirtle = list(df.iloc[6,4:11])
    pokets = [bulbasaur, charmander, squirtle]
    # Converting height from meters to inches
    # Weight remains in kg
    # we store these values in a list
    bul_hw = [df.iloc[0,19]*3.281, df.iloc[0,20]]
    char_hw = [df.iloc[3,19]*3.281, df.iloc[3,20]]
    squ_hw =  [df.iloc[6,19]*3.281, df.iloc[6,20]]
    hw = [bul_hw, char_hw, squ_hw]
    #Creates figure with ID of 0 that will contain subplots
    fig = plt.figure(0)
    # Line plot
    #Grid Size of 4x3, starting at 0,0 and spanning 3 columns in first row
    ax1 = plt.subplot2grid((4,3), (0,0), colspan=3)
    ax1.plot(bulbasaur,'g-',bulbasaur,'go') #g- is green line 'go' is green circles
    ax1.plot(charmander,'r-',charmander,'ro')#r- is red line 'ro is red circles
    ax1.plot(squirtle,'b-',squirtle,'bo')#b- is blue line 'bo' is blue circles
    ax1.set_xlim(-0.3,6.3) #sets x axis limits from 0.3 to 6.3
    ax1.set_ylim(0,350) #Set Y-axis limits
    ax1.set_yticks(range(0,350,50)) #Show ticks every 50 units
    
    #We define specific coordinates from our plot
    text_x_coord = [0.045, .19, 0.34, 0.49, 0.64, 0.795, 0.945]
    text_y_coord = [0.7, 0.57, 0.65, 0.75, 0.75, 0.75, 0.72]
    rot = [0, 45, 45, 45, 45, 45, 45] #rot of labels
    txt = [r'$T_{OTAL}$', r'$HP$', r'$A_{TTACK}$', r'$D_{EFENSE}$',
        r'$S_{P}\_A_{TK}$',r'$S_{P}\_D_{EF}$',r'$S_{PEED}$'] # text is in TEX format
    for i in range(0, 7):
        ax1.text(text_x_coord[i], text_y_coord[i], txt[i],
                transform = ax1.transAxes,  # makes width and height in percentage
                va = 'top',
                rotation = rot[i],
                bbox = dict(
                        boxstyle = 'round',
                        facecolor = 'wheat',
                        alpha = 0.78))  # alpha -> transparency

    # continuing from previous code
    #We create subplots in a 4x3 grid
    ax2 = plt.subplot2grid((4,3), (1,0), colspan=1)
    ax3 = plt.subplot2grid((4,3), (2,0), colspan=1)
    ax4 = plt.subplot2grid((4,3), (3,0), colspan=1)
    ax = [ax2, ax3, ax4]
    #colors for each box plot
    colors = ['g', 'r', 'b']
    #Loops iterating over the 3 subplots
    for i in range(0, 3):
        #box plot for each pokemon stat
        bp = ax[i].boxplot(pokets[i][1:],patch_artist=True)
        # Adding colors to edges
        #boxes - rectangular boxes
        #whiskers - vertical lines extending from boxes
        #fliers - outlier points
        #means, medians, caps are statistical markers
        #plt.setp(bp[element],color='k') sets color of all the elements to black
        for element in ['boxes', 'whiskers', 'fliers', 'means', 'medians', 'caps']:
                plt.setp(bp[element], color='k')
        # Adding color inside the box
        for patch in bp['boxes']:
            patch.set(facecolor=colors[i])
        ax[i].set_ylim(35,70)
        
    #Add an arrow shape pointing to the median
    ax3.annotate('Median', xy=(1.09, 51),xytext=(1.2, 60),
            arrowprops=dict(facecolor='wheat', 
                            shrink=0.001),)
    
    # continuing from previous code
    ax5 = plt.subplot2grid((4,3), (1,1), colspan=2, rowspan = 3)
    bar_width = 0.2
    wdt = 0
    names = ['Bulbasaur','Charmander','Squirtle']
    for i in range(0, 3):
        p=ax5.barh(np.arange(2) + wdt, hw[i],bar_width,
                alpha = 0.5,
                color = colors[i],
                label = names[i])
        wdt += bar_width
    ax5.legend(loc = 'lower right')
    ax5.set_xlim(0,12)
    ax5.set_ylim(-0.2,1.8)
    plt.yticks(np.arange(2) + (bar_width)*1.5, 
            ('Height', 'Weight'))
    plt.tight_layout()
    plt.show()
    return

barPlotExample()