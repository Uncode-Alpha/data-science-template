import numpy as np
import pandas as pd

#Test comment on this
# This page will hold concepts related to this lex course:
# https://lex.infosysapps.com/web/en/viewer/web-module/lex_auth_0126429283054141441728?collectionId=lex_auth_01275797507348070414&collectionType=Learning%20Path&pathId=lex_16286352104288236000,lex_auth_0126429259454873601795

#PANDAS

#CONCATENATION
#Concatenation of dataframes example
pd.concat( [data1,data2], axis = 1 )
#column-wise concatenation
pd.concat([df1, df2], axis=1)
#row-wise concatenation (ignore_index=True)
pd.concat([df1, df2], ignore_index=True)

#RESHAPE
# Example input
#                   Year1     Year2
# Country Game                     
# IND     Game1 -2.263939 -0.793986
#         Game2 -0.390861  0.728531
# US      Game1 -0.944708  0.352151
#         Game2 -0.232056  0.452532 
# To reduce the complexity of the visualization
# stack and unstack
df.stack(); df.unstack()
#Example output
# Country  Game        
# IND      Game1  Year1   -2.263939
#                 Year2   -0.793986
#          Game2  Year1   -0.390861
#                 Year2    0.728531
# US       Game1  Year1   -0.944708
#                 Year2    0.352151
#          Game2  Year1   -0.232056
#                 Year2    0.452532
# dtype: float64

#PIVOT
#Example input
#       Country   Medal   Game Score
# Year1     IND    Gold  Game1   9.9
# Year2     IND  Bronze  Game2     8
# Year1     USA  Silver  Game1   9.5
# Year2     USA    Gold  Game2   8.6 
# To break down a large dataset into a smaller one
df.pivot(index = 'Country', columns = 'Medal')
#Example output
#           Game                Score            
# Medal   Bronze   Gold Silver Bronze Gold Silver
# Country                                        
# IND      Game2  Game1   None      8  9.9   None
# USA       None  Game2  Game1   None  8.6    9.5

#GROUPING
#Example input
#   Category  Sales
# 0   Laptop   1000
# 1   Laptop   2520
# 2  Desktop   3000
# 3  Desktop    400
#Group similar data and apply a function
df.groupby(['Category'], sort = False).sum()
#Example output
#           Sales
# Category       
# Laptop     3520
# Desktop    3400 