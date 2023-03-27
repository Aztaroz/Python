import pandas as pd

# Load Dataset
path = 'E:\\Work\\มวล\\ITD\\ปี 2\\เทอม 3\\AI\\Week 11\\IMI_Dataset.csv'
df = pd.read_csv(path)
# Handling Categorical Data
from sklearn.preprocessing import LabelEncoder

label_encoder = LabelEncoder()

for i in df.columns:
    if df[i].dtype == "object" and i != "Timestamp":
        df[i] = label_encoder.fit_transform(df[i])

#print(df.info())

from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import RobustScaler

MinMaxScaler = MinMaxScaler()
StandardScaler = StandardScaler()
RobustScaler = RobustScaler()

df["AgeMinMax"] = MinMaxScaler.fit_transform(df["Age"].to_numpy().reshape(-1,1))
df["AgeStandard"] = StandardScaler.fit_transform(df["Age"].to_numpy().reshape(-1,1))
df["AgeRobust"] = RobustScaler.fit_transform(df["Age"].to_numpy().reshape(-1,1))

print(df.describe().to_string)