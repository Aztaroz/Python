import pandas as pd

path = 'E:\\Work\\มวล\\ITD\\ปี 2\\เทอม 3\\AI\\Week 11\\IMI_Dataset.csv'
df = pd.read_csv(path)

df['Timestamp'] = pd.to_datetime(df.Timestamp)
df2 = pd.DataFrame(df['Timestamp'])

df2["date"] = df2['Timestamp'].dt.date
df2["quarter"] = df2['Timestamp'].dt.quarter
df2["week"] = df2['Timestamp'].dt.weekday
df2['time'] = df2['Timestamp'].dt.time

df2['time_session'] = pd.to_datetime(df2['Timestamp'], format='%H:%M:%S')

a = df.assign(time_session = pd.cut(df2['time_session'].dt.hour,[0,6,12,18,24],labels=['Night','Morning','Afternoon','Evening']))

df2['time_session'] = a['time_session']
print(df2)