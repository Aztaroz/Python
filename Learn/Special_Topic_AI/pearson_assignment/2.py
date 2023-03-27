import scipy.stats as stats
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Load the dataset
path = 'E:\\Work\\มวล\\ITD\\ปี 2\\เทอม 3\\AI\\Week 12\\pearson\\กษิดิศ บุญชัย - IMI_Dataset.csv'
df = pd.read_csv(path)
# # Extract individual groups
group1 = df['Age'][(df['Sex'] == 'M') & (df['HeartDisease'] == 1) & (df['ChestPainType'] == 'ATA')]
group2 = df['Age'][(df['Sex'] == 'M') & (df['HeartDisease'] == 0) & (df['ChestPainType'] == 'ATA')]
Mnomeans, Mmeans = group1.mean(), group2.mean()
# Perform the ANOVA
anova = stats.f_oneway(group1, group2)
print(anova)
sns.distplot(group1, color="skyblue", label="Male no HeartDisease")
sns.distplot(group2, color="orchid", label="Male's HeartDisease")
plt.text(x=60, y=0.030, s="MalenoHeartDisease's mean: %.2f" % Mnomeans, color='blue')
plt.text(x=80, y=0.028, s="Male's mean: %.2f" % Mmeans, color='red')
plt.title("ANOVA Test between resting blood pressure and gender")
plt.legend()
plt.show()
print(anova)