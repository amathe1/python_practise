import pandas as pd

students = {
    "Name" : ["Arun", "Anu", "Vynateya"],
    "ID" : ["1", "2", "3"],
    "Location" : ["Hyd", "Ban", "Ban"] 
}

df = pd.DataFrame(students, index=["row1", "row2", "row3"])

print(df)

'''
Output :

       Name ID Location
0      Arun  1      Hyd
1       Anu  2      Ban
2  Vynateya  3      Ban

'''