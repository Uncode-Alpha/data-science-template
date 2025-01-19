#Pandas is a data analysis library which provides object like DataFrame to load
#and perform operations on tabular data. It offers features most of which are 
# listed above including but not limited to a grouping of data along with 
# time-series functionality.

#Importing the pandas library
import pandas as pd
import numpy as np

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

def excercise1():
    #Given following dataframe
    df = pd.DataFrame([[0.23,'f1'],[5.36,'f2']],index = list('pq'),
                    columns = list('ab'))
    #1 Change the column name from 'a' to 'A'
    df.rename(columns = {'a':'A'},inplace=True)
    print('Dataframe after changing column name: \n',df)
    
    #2 Add a new column 'c' with random values
    df.insert(2,'c',pd.Series(np.random.randn(2), index=df.index))
    print('Dataframe after adding new column: \n',df)
    
    #3 Change the datatype of column 'A' values to complex
    df['A'] = df['A'].astype(complex)
    print('Dataframe after changing datatype \n',df)
    
    #4 Display rows whose any of the element matches with any element of
    #the given list
    lst = ['f30','f50','f2','f0'] 
    print('Printing only the row that matches at least one element of the list\n'
            ,df[df.isin(lst).any(axis=1)])
    #Now we will print only the index of the rows that match the list
    print('Printing only the index of the rows that match the list\n'
            ,df.index[df.isin(lst).any(axis=1)])
    

def excelExample():
    #This code needs pandas and openpyxl installed
    #This part of the example writes a dataset to an xlsx format
    df = pd.DataFrame([[11, 202],[33, 44]],index = list('AB'),columns = list('CD'))
    #Here we can specify the path and name of the file to put our dataframe info
    ''' Writing to excel file '''
    df.to_excel('data/dataSciencePractice/test_file.xlsx', sheet_name = 'Sheet1')
    ''' Reading from excel file '''
    print(pd.read_excel('data/dataSciencePractice/test_file.xlsx', 'Sheet1'))
    #Woth this command we can only print specific rows of a table
    print(df.head(1)) 
    #This part of the excel explains using read_excel to read a table from a file
    #df = pd.read_table('chat.txt')
    return

def excercise2():
    #Given this dataframe, perform the following
    dataTable = pd.DataFrame([[18,10,5,11,-2],
                    [2,-2,9,-11,3],
                    [-4,6,-19,2,1],
                    [3,-14,1,-2,8],
                    [-2,2,4,6,13]],
                    index = list('pqrst'),
                    columns = list('abcde'))
    #Excercise 1
    #Extract the rows whose total sum is even. 
    #Next, save this dataframe into a new dataframe named newTable . 
    #Copy this dataframe to an excel file named file_df_excercise2.xlsx under Sheet 1.
    #Solution: We show the sum
    print('Sum of rows from datTable\n',dataTable.sum(axis=1))
    #we perform  the operation  of assigning the rows that sum is even using % operator
    #we use dataTable to operate over all the rows
    newTable=dataTable[dataTable.sum(axis=1)%2 == 0]
    print('New table with rows that sum is even\n',newTable)
    #Lastly we write the result in the excel file
    newTable.to_excel('data/dataSciencePractice/file_df_excercise2.xlsx', 
                    sheet_name = 'Sheet1',index_label='Even sum rows')
    #We read the excel as proof of the operation
    print('This is the excel with only even rows\n',
        pd.read_excel('data/dataSciencePractice/file_df_excercise2.xlsx','Sheet1'))
    
    #Excercise 2
    #Copy newTable dataframe into a new dataframe df_temp. 
    #Append a new column named as 'm' to the df_temp dataframe which defines the multiplication of each element in one row.
    #Save this dataframe in Sheet 2 of file_df excel file.
    df_temp = newTable.copy()
    df_temp['m']=df_temp.apply(lambda x: x.prod(), axis=1)
    print('Temporal dataframe with new column m\n',df_temp)
    #We add the result to the excel file
    with pd.ExcelWriter('data/dataSciencePractice/file_df_excercise2.xlsx', engine='openpyxl', mode='a') as writer:
        df_temp.to_excel(writer, sheet_name='Sheet2', index_label='Multiplication of elements')
    print('New excel sheet with added column\n',pd.read_excel('data/dataSciencePractice/file_df_excercise2.xlsx','Sheet2'))
    return

def groupsExercise():
    #Given dataframe
    sys = ['s1','s1','s1','s1',
        's2','s2','s2','s2']
    net_day = ['d1','d1','d2','d2',
            'd1','d1','d2','d2']
    spd = [1.3, 11.4, 5.6, 12.3, 
            6.2, 1.1, 20.0, 8.8]
    df = pd.DataFrame({'set_name':sys,
                        'spd_per_day':net_day,
                        'speed':spd})
    #Excercise 1 - Construct a dataframe new_df where the given dataset is grouped based on each system (s1 and s2) 
    #and speed per day (d1 and d2) with the median speed each day per system. Also, provide a secondary name ' Median' for the speed attribute.
    # Group by 'set_name' and 'spd_per_day' and calculate the median
    new_df = df.groupby(['set_name', 'spd_per_day'], as_index=False).median()

    # Rename the 'speed' column to 'Median'
    new_df.rename(columns={'speed': 'Median'}, inplace=True)

    print(new_df)
    
    #Excercise 2 - Sort the dataframe new_df in the ascending order of the median speed.
    print('\n',new_df.sort_values(by='Median', ascending=True))
    return

groupsExercise()