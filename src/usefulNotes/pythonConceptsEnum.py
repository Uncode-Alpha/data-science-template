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
