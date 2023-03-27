import matplotlib.pyplot as plt
import pandas as pd

path = 'E:\\Work\\มวล\\ITD\\ปี 2\\เทอม 3\\AI\\Week 12\\pearson\\กษิดิศ บุญชัย - IMI_Dataset.csv'
df = pd.read_csv(path)

from sklearn.preprocessing import LabelEncoder

label_encoder = LabelEncoder()

for i in df.columns:
    if df[i].dtypes == 'object' and i != 'Timestamp':
        df[i] = label_encoder.fit_transform(df[i])
        print(df[i])
df2 = df[(df["Sex"] == 0) & (df["ChestPainType"] == 1)]
df3 = df[(df["Sex"] == 1) & (df["ChestPainType"] == 1)]

corF = df2[["Age", "Cholesterol", "MaxHR", "RestingBP"]].corr()
corM = df3[["Age", "Cholesterol", "MaxHR", "RestingBP"]].corr()
import seaborn as sns

sns.heatmap(corM, vmin=-1, vmax=1, annot=True)
plt.show()