import pandas as pd
import numpy as np

#=========== Section 1 ===========
# technologies = {
#     'Courses' : ["Spark", "PySpark", "Hadoop", "Python", "Pandas"],
#     'Fee': [22000,25000,23000,24000,26000],
#     'Discount': [1000,2300,1000,1200,2500],
#     'Duration':['35days','35days','40days','30days','25days']
# }
#
# df = pd.DataFrame(technologies)
# print('df\n',df)
#
# df1 = df.iloc[:3,:]
# print('df1\n',df1)

# print('df1\n',df[0:2])

#======================

#=========== Section 2 ===========
# left = pd.DataFrame({"A":["A0","A1","A2"], "B":["B0","B1","B2"]}, index = ["K0","K1","K2"])
# right = pd.DataFrame({"C":["C0","C2","C3"], "D":["D0","D2","D3"]}, index = ["K0","K2","K3"])
#
# result1 = pd.concat([left, right])
#
# result2 = pd.concat([left,right], axis=0)
# result3 = pd.concat([left,right], axis=1)
#======================

#=========== Section 3 : Missing Values Handling ===========

df = pd.read_csv("E:\Work\มวล\ITD\ปี 2\เทอม 3\AI\Week 6\\NewExEnv-missing-values.csv")
datadrop = df.dropna()
# print(df.to_string())

# print(df.dtypes)
# print(df.describe(include='object').to_string())
# print(df.info())
# print(df.isnull().sum(), '\n')

print(datadrop.to_string())
print(datadrop.dtypes)
print(datadrop.describe(include='object').to_string())
print(datadrop.info())
print(datadrop.isnull().sum(), '\n')