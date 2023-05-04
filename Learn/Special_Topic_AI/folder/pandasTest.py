import pandas as pd
import numpy as np

# s1 = pd.Series(["apple", "Banana", "lemon", "mango"])
# s2 = pd.Series({"A":1, "B":2, "C":3, "D":4})
# s3 = pd.Series([1,2,3,4,5], index=["A","B","C","D","E"], name="simple series")
# path = 'E:\Work\มวล\ITD\ปี 2\เทอม 3\AI\Week 6\data.csv'
# df4 = pd.read_csv(path)
# print(df4.describe(include='object'))

np.random.seed(5000)
data = np.random.randint(0,20, size=(5,4))
df = pd.DataFrame(data, columns = list("ABCD"))
print(df)


print(df.index)
print(df.columns)
