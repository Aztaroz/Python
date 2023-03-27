import matplotlib.pyplot as plt
import pandas as pd

path = 'E:\\Work\\มวล\\ITD\\ปี 2\\เทอม 3\\AI\\Week 11\\IMI_Dataset.csv'
df =  pd.read_csv(path)

from sklearn.preprocessing import LabelEncoder
label_encoder = LabelEncoder()

for i in df.columns:
    if df[i].dtype == 'object' and i != "Timestamp":
        df[i] = label_encoder.fit_transform(df[i])

cor = df[["Age","Cholesterol","MaxHR","RestingBP"]].corr()

import seaborn as sns

sns.heatmap(cor,vmin=-1, vmax=1, annot=True)
plt.show()