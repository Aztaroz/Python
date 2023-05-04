import pandas as pd

path = 'E:\\Work\\มวล\\ITD\\ปี 2\\เทอม 3\\AI\\Week 11\\Assignment\\กษิดิศ บุญชัย - example_dataset.csv'
df = pd.read_csv(path)

missing_values = df.isnull().sum()
# print(missing_values,'\n')

# หาค่า Mean ในแต่ละ Column
means = df.mean()
# นำค่า Mean ที่หาได้ไปเติมใน Column ที่ข้อมูลสูญหายไป
df = df.fillna(means)

# หาค่า Mode ของ Column "Gender"
consuming_mode = df['Gender'].mode()[0]
# นำค่า Mode ที่หาได้ไปเติมใน Column "Gender"
df['Gender'].fillna(consuming_mode, inplace=True)

print(df.to_string())


# consuming_mode = df['PM10'].mode()[0]
# df['PM10'].fillna(consuming_mode, inplace=True)

# print(df.isnull().sum(),'\n')
