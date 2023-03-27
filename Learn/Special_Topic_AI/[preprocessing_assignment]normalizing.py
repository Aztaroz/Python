import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

path = 'E:\\Work\\มวล\\ITD\\ปี 2\\เทอม 3\\AI\\Week 11\\Assignment\\กษิดิศ บุญชัย - example_dataset.csv'
df = pd.read_csv(path)

# หาค่า Mean ในแต่ละ Column
means = df.mean()
# นำค่า Mean ที่หาได้ไปเติมใน Column ที่ข้อมูลสูญหายไป
df = df.fillna(means)

# หาค่า Mode ของ Column "Gender"
consuming_mode = df['Gender'].mode()[0]
# นำค่า Mode ที่หาได้ไปเติมใน Column "Gender"
df['Gender'].fillna(consuming_mode, inplace=True)


from sklearn.preprocessing import LabelEncoder

label_encoder = LabelEncoder()

for i in df.columns:
    if df[i].dtypes == 'object' and i != "Timestamp":
        df[i] = label_encoder.fit_transform(df[i])
print(df['MeanHR'].describe())
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import RobustScaler

MinMaxScaler = MinMaxScaler()
StandardScaler = StandardScaler()
RobustScaler = RobustScaler()

# df['MeanHRMinMax'] = MinMaxScaler.fit_transform(df['MeanHR'].to_numpy().reshape(-1,1))
# df['MeanHRStandard'] = StandardScaler.fit_transform(df['MeanHR'].to_numpy().reshape(-1,1))
df['MeanHRRobust'] = RobustScaler.fit_transform(df['MeanHR'].to_numpy().reshape(-1,1))
print(dir(df))
print(df.iloc[:,14:].describe().to_string())
# print(df['MeanEDA'].describe().to_string())


sns.boxplot(x=df["MeanHR"])
plt.title("MeanHR")
plt.show()