import pandas as pd
import numpy as np
# # Data Collection
path = 'E:\\Work\\มวล\\ITD\\ปี 2\\เทอม 3\\AI\\Week 12\\pearson\\กษิดิศ บุญชัย - IMI_Dataset.csv'
df = pd.read_csv(path)
df.drop('Timestamp', axis=1, inplace=True)
# # Data Preprocessing
# Handling Categorical Data
from sklearn.preprocessing import LabelEncoder
label_encoder = LabelEncoder()
for i in df.columns:
    if df[i].dtype == "object" and i != "HeartDisease":
        df[i] = label_encoder.fit_transform(df[i])
# Normalize the data
from sklearn import preprocessing
scaler = preprocessing.MinMaxScaler()
scaler.fit(df.iloc[:, 1:11])
df.iloc[:, 1:11] = pd.DataFrame(scaler.transform(df.iloc[:, 1:11]), index=df.index, columns=df.iloc[:, 1:11].columns)

from sklearn.feature_selection import SelectKBest, chi2
X = df.loc[:, df.columns != 'HeartDisease']
y = df[['HeartDisease']]
selector = SelectKBest(chi2, k=5)
selector.fit(X, y)
X_new = selector.transform(X)
best_features = X.columns[selector.get_support(indices=True)]
# Correlation
cor = df[best_features].corr()
import seaborn as sns
import matplotlib.pyplot as plt
# Plot correlation coefficient by a heatmap
sns.heatmap(cor, vmin=-1, vmax=1, annot=True)
plt.tight_layout()
plt.show()

# Calculating the accuracy and the time taken by the classifier
from sklearn.metrics import accuracy_score
import time
# Data Splitting for training and testing
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

# Decision Tree
from sklearn.tree import DecisionTreeClassifier
dtModel = DecisionTreeClassifier()
startTime = time.time()
# Building the model using the training data set
dtModel.fit(X_train, np.ravel(y_train))
# Evaluating the model using testing data set
dtY_pred = dtModel.predict(X_test)
dtScore = round(accuracy_score(y_test, dtY_pred), 2)
dtTime = round(time.time() - startTime, 2)
# Printing the accuracy and the time taken by the classifier
print('Accuracy using Decision Tree:', dtScore)
print('Time taken using Decision Tree:', dtTime)

# K-Nearest Neighbors
from sklearn.neighbors import KNeighborsClassifier
kNNModel = KNeighborsClassifier(n_neighbors=2)
startTime = time.time()
# Building the model using the training data set
kNNModel.fit(X_train, np.ravel(y_train))
# Evaluating the model using testing data set
kNNY_pred = kNNModel.predict(X_test)
kNNScore = round(accuracy_score(y_test, kNNY_pred), 2)
kNNTime = round(time.time() - startTime, 2)
# Printing the accuracy and the time taken by the classifier
print('Accuracy using K-Nearest Neighbors:', kNNScore)
print('Time taken using K-Nearest Neighbors:', kNNTime)

# Support Vector Machine
from sklearn.svm import SVC
svmModel = SVC(kernel='linear')
startTime = time.time()
# Building the model using the training data set
svmModel.fit(X_train, np.ravel(y_train))
# Evaluating the model using testing data set
svmY_pred = svmModel.predict(X_test)
svmScore = round(accuracy_score(y_test, svmY_pred), 2)
svmTime = round(time.time() - startTime, 2)
# Printing the accuracy and the time taken by the classifier
print('Accuracy using Support Vector Machine:', svmScore)
print('Time taken using Support Vector Machine:', svmTime)

# Neural Networks
from sklearn.neural_network import MLPClassifier
nnModel = MLPClassifier()
startTime = time.time()
# Building the model using the training data set
nnModel.fit(X_train, np.ravel(y_train))
# Evaluating the model using testing data set
nnY_pred = nnModel.predict(X_test)
nnScore = round(accuracy_score(y_test, nnY_pred), 2)
nnTime = round(time.time() - startTime, 2)
# Printing the accuracy and the time taken by the classifier
print('Accuracy using Neural Networks:', nnScore)
print('Time taken using Neural Networks:', nnTime)

# Naive Bayes
from sklearn.naive_bayes import GaussianNB
nbModel = GaussianNB()
startTime = time.time()
# Building the model using the training data set
nbModel.fit(X_train, np.ravel(y_train))
# Evaluating the model using testing data set
nbY_pred = nbModel.predict(X_test)
nbScore = round(accuracy_score(y_test, nbY_pred), 2)
nbTime = round(time.time() - startTime, 2)
# Printing the accuracy and the time taken by the classifier
print('Accuracy using Naive Bayes:', nbScore)
print('Time taken using Naive Bayes:', nbTime)

# Results comparison
modelLabel = ["Decision Tree", "KNN", "SVM", "NN", "Naive Bayes"]
modelAccuracy = [dtScore, kNNScore, svmScore, nnScore, nbScore]
modelTime = [dtTime, kNNTime, svmTime, nnTime, nbTime]
dfAccuracy = pd.DataFrame(modelAccuracy, columns=['accuracy'], index=modelLabel)
dfTime = pd.DataFrame(modelTime, columns=['seconds'], index=modelLabel)
ax = sns.barplot(x=modelLabel, y='accuracy', data=dfAccuracy, palette='flare')
plt.ylim(min(modelAccuracy)-0.2, max(modelAccuracy)+0.2)
ax.bar_label(ax.containers[0])
plt.title("Accuracy Comparison")
plt.tight_layout()
plt.show()
ax = sns.barplot(x=modelLabel, y='seconds', data=dfTime, palette='flare')
plt.ylim(min(modelTime), max(modelTime)+0.2)
ax.bar_label(ax.containers[0])
plt.title("Processing Time Comparison")
plt.tight_layout()
plt.show()




######################################## Tree ####################################################
import matplotlib.pyplot as plt
# z
# # Plot correlation coefficient by a heatmap
# sns.heatmap(cor, vmin=-1, vmax=1, cmap='vlag', annot=True)
# plt.tight_layout()
# plt.show()
#
# from sklearn.metrics import accuracy_score
import time

# Data Splitting for training and testing
from sklearn.model_selection import train_test_split
import time

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5)
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_text
from sklearn import tree
#
dtModel = tree.DecisionTreeClassifier()
startTime = time.time()
from sklearn.metrics import accuracy_score
#
# # Building the model using the training data set
dtModel.fit(X_train, np.ravel(y_train))
#
# # Evaluating the model using testing data set
dtY_pred = dtModel.predict(X_test)
dtScore = round(accuracy_score(y_test, dtY_pred), 2)
dtTime = round(time.time() - startTime, 2)

# # Printing the accuracy and the time taken by the classifier
print('Accuracy using Decision Tree:', dtScore)
print('Time taken using Decision Tree:', dtTime)
#
importances = dtModel.feature_importances_
print(importances)
indices = np.argsort(importances)
# features = ['MeanHR', 'MeanSKT', 'EDA_mean_norm', 'MeanAir']
features = ["Timestamp", "Age", "Sex", "ChestPainType", "RestingBP", "Cholesterol", "FastingBS", "RestingECG", "MaxHR",
            "ExerciseAngina", "Oldpeak", "ST_Slope"]
# features = ['MeanHR', 'MeanSKT', 'MeanEDA', 'MeanAir', 'IndoorHumidity', 'IndoorTemperature']
# features = ['MeanHR', 'MeanSKT', 'EDA_mean_norm', 'MeanAir', 'gender', 'age', 'BMI', 'disease']
j = 5  # top j importance
fig = plt.figure(figsize=(16, 9))
plt.barh(range(j), importances[indices][len(indices) - j:], color='lightblue', align='center')
plt.yticks(range(j), [features[i] for i in indices[len(indices) - j:]])
plt.title('Feature Importances')
plt.xlabel('Relative Importance')
plt.show()
#
#
cn = ['1', '0']
fig = plt.figure(figsize=(100, 40))
vis = tree.plot_tree(dtModel, feature_names=features, class_names=cn, max_depth=20,
                     fontsize=9, proportion=True, filled=True, rounded=True)
plt.savefig('tree_high_dpi_x2', bbox_inches='tight', dpi=250)
plt.show()
tree_rules = export_text(dtModel, max_depth=20, show_weights=True, feature_names=list(X_train.columns))
tree_rules = export_text(dtModel, max_depth=20, feature_names=list(X_train.columns))
print(tree_rules)

with open('hi_rule_x2.txt', 'a') as the_file:
    the_file.write(str(tree_rules))
    the_file.write("\n")