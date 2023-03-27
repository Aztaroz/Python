import pandas as pd

path = 'E:\\Work\\มวล\\ITD\\ปี 2\\เทอม 3\\AI\\Week 11\\IMI_Dataset.csv'
df = pd.read_csv(path)

df2 = pd.DataFrame(df["Age"])


bins = [0,2,4,12,17,59,102]
df2['AgeBin'] = pd.cut(df['Age'],bins)

labels = ["Baby","Toddler","Children","Teen","Adult","Older adults"]
df2["AgeLabel"] = pd.cut(df2["Age"],bins = bins,labels = labels)

#(df2.sample(n=5))

df3 = pd.DataFrame(df['Age'])
df3.loc[df3['Age'].between(0,2,'both'),'binned_label'] = "Baby"
df3.loc[df3['Age'].between(2,4,'right'),'binned_label'] = "Toddler"
df3.loc[df3['Age'].between(4,12,'right'),'binned_label'] = "Children"
df3.loc[df3['Age'].between(12,17,'right'),'binned_label'] = "Teen"
df3.loc[df3['Age'].between(17,59,'right'),'binned_label'] = "Adult"
df3.loc[df3['Age'].between(59,102,'right'),'binned_label'] = "Older adults"

df4 = pd.DataFrame(df['Age'])
df4['binned_label'],cut_bin = pd.qcut(df['Age'],q=6,
                                     labels = ["Baby","Toddler","Children","Teen","Adult","Older adults"],
                                     retbins=True)

print("cut_bin:",cut_bin)
print(df4.sample(n=5))