import pandas as pd

path = 'E:\\Work\\มวล\\ITD\\ปี 2\\เทอม 3\\AI\\Week 11\\Assignment\\กษิดิศ บุญชัย - example_dataset.csv'
df = pd.read_csv(path)

df1 = pd.DataFrame(df['MeanHR'])
# กำหนดช่วงของข้อมูล
df1.loc[df1['MeanHR'].between(40,60,'both'),'Status'] = "Low"
df1.loc[df1['MeanHR'].between(60,100,'right'),'Status'] = "Normal"
df1.loc[df1['MeanHR'].between(100,150,'right'),'Status'] = "High"
df1.loc[df1['MeanHR'].between(150,170,'right'),'Status'] = "Dangerous"

# หาค่า Mean ในแต่ละ Column
means = df1.mean()
# นำค่า Mean ที่หาได้ไปเติมใน Column ที่ข้อมูลสูญหายไป
df1 = df1.fillna(means)

# หาค่า Mode ของ Column "Gender"
consuming_mode = df1['Status'].mode()[0]
# นำค่า Mode ที่หาได้ไปเติมใน Column "Gender"
df1['Status'].fillna(consuming_mode, inplace=True)

print(df1.sample(n=10))