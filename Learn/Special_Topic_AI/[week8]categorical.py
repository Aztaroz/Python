import pandas as pd
import numpy as np

df = pd.read_csv("E:\Work\มวล\ITD\ปี 2\เทอม 3\AI\Week 6\\NewExEnv-missing-values.csv")

from sklearn.preprocessing import LabelEncoder
label_encoder = LabelEncoder()

df["Consuming"] = label_encoder.fit_transform(df["Cnsuming"])

mapping = dict(zip(label_encoder.classes_, label_encoder.transform(label_encoder.classes_)))
print(mapping)
print(df.head().to_string())