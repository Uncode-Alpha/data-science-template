#Pandas is a data analysis library which provides object like DataFrame to load
#and perform operations on tabular data. It offers features most of which are 
# listed above including but not limited to a grouping of data along with 
# time-series functionality.

#Importing the pandas library
import pandas as pd

def exampleDataframe():
    # 1. Using list of dictionary
    lst = [{"C1": 1, "C2": 2},
            {"C1": 5, "C2": 10, "C3": 20}]
    # Observe NaN       
    print(pd.DataFrame(lst, index = ["R1", "R2"]))
    #     C1  C2    C3
    # R1   1   2   NaN
    # R2   5  10  20.0
    # 2. Using dictionary
    dc = {"C1": ["1", "3"],
            "C2": ["2","4"]}
    print( pd.DataFrame(dc, index = ["R1", "R2"]) )
    #    C1 C2
    # R1  1  2
    # R2  3  4
    # 3. Using list
    lst = [[52,32],[45,85]]
    print(pd.DataFrame(lst, index = list('pq'), columns = list('ab')))
    #     a   b
    # p  52  32
    # q  45  85
    return

exampleDataframe()