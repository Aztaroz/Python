import  pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

path = 'E:\\Work\\มวล\\ITD\\ปี 2\\เทอม 3\\AI\\Week 11\\Assignment\\กษิดิศ บุญชัย - example_dataset.csv'
df = pd.read_csv(path)

# หาค่า Mean ในแต่ละ Column
means = df.mean()
# นำค่า Mean ที่หาได้ไปเติมใน Column ที่ข้อมูลสูญหายไป
df = df.fillna(means)

sns.boxplot(x=df["PM25"])
plt.title("PM2.5 Before outlier elimination")
# plt.show()

pm25_q1 = df['PM25'].quantile(0.25)
pm25_q3 = df['PM25'].quantile(0.75)

pm10_q1 = df['PM10'].quantile(0.25)
pm10_q3 = df['PM10'].quantile()

print(f'PM2.5 1st Quartile {pm25_q1}')
print(f'PM2.5 3rd Quartile {pm25_q3} \n #####################')

print(f'PM10 1st Quartile {pm10_q1}')
print(f'PM10 3rd Quartile {pm10_q3}')



# pm25_iqr = pm25_q3 - pm25_q1
# pm10_iqr = pm10_q3 - pm10_q1
# print(f'PM2.5 Inter Quartile Range {pm25_iqr}\nPM10 Inter Quartile Range {pm10_iqr}')