import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn import preprocessing

data = pd.read_csv('diabetes.csv')

# Replace 0 BMI value
bmi_mean = data[data.BMI != 0].BMI.mean()
data.BMI = data.BMI.replace(0,bmi_mean)

# Replace 0 BloodPressure value
BP_mean = data[data.BloodPressure != 0].BloodPressure.mean()
data.BloodPressure = data.BloodPressure.replace(0,BP_mean)

# Replace 0 SkinThickness value
ST_mean = data[data.SkinThickness != 0].SkinThickness.mean()
data.SkinThickness = data.SkinThickness.replace(0,ST_mean)

# Replace 0 Insulin value
IL_mean = data[data.Insulin != 0].Insulin.mean()
data.Insulin = data.Insulin.replace(0,IL_mean)

# Replace 0 Glucose value
GC_mean = data[data.Glucose != 0].Glucose.mean()
data.Glucose = data.Glucose.replace(0,GC_mean)

# Eliminate Outliers from Insulin
# Q1 = data['Insulin'].quantile(0.25)
# Q3 = data['Insulin'].quantile(0.75)
# IQR = Q3 - Q1
# Lower_fence = Q1 - (1.5 * IQR)
# Upper_fence = Q3 + (1.5 * IQR)
# data = data[~((data['Insulin'] < Lower_fence) | (data['Insulin'] > Upper_fence))]


# Eliminate Outliers from BloodPressure
# Q1 = data['BloodPressure'].quantile(0.25)
# Q3 = data['BloodPressure'].quantile(0.75)
# IQR = Q3 - Q1
# Lower_fence = Q1 - (1.5 * IQR)
# Upper_fence = Q3 + (1.5 * IQR)
# data = data[~((data['BloodPressure'] < Lower_fence) | (data['BloodPressure'] > Upper_fence))]

# Eliminate Outliers from DiabetesPedigreeFunction
# Q1 = data['DiabetesPedigreeFunction'].quantile(0.25)
# Q3 = data['DiabetesPedigreeFunction'].quantile(0.75)
# IQR = Q3 - Q1
# Lower_fence = Q1 - (1.5 * IQR)
# Upper_fence = Q3 + (1.5 * IQR)
# data = data[~((data['DiabetesPedigreeFunction'] < Lower_fence) | (data['DiabetesPedigreeFunction'] > Upper_fence))]


# Check Outliers
columnName = "Insulin"
sns.boxplot(x=data[columnName])
plt.title(columnName)
plt.show()


# Numeric Feature Engineering ( Binning )
data.loc[data['BMI'].between(1, 18.5, 'both'), 'BMI_LV'] = 'Underweight'
data.loc[data['BMI'].between(18.5, 25, 'right'), 'BMI_LV'] = 'Normal'
data.loc[data['BMI'].between(25, 30, 'right'), 'BMI_LV'] = 'Overweight'
data.loc[data['BMI'].between(30, 35, 'right'), 'BMI_LV'] = 'OBESE'
data.loc[data['BMI'].between(35, 70,'right'), 'BMI_LV'] = 'Extremely_OBESE'


# LabelEncoder
label_encoder = LabelEncoder()
for i in data.columns:
    if i == 'BMI_LV':
        data[i] = label_encoder.fit_transform(data[i])


# Normalizing
from sklearn.preprocessing import RobustScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
Robustscaler = RobustScaler()
MinMaxScaler = MinMaxScaler()
StandardScaler = StandardScaler()

# Normalizing Insulin
data["Insulin"] = Robustscaler.fit_transform(data["Insulin"].to_numpy().reshape(-1, 1))

# Normalizing SkinThickness
data["SkinThickness"] = Robustscaler.fit_transform(data["SkinThickness"].to_numpy().reshape(-1, 1))

# Normalizing DiabetesPedigreeFunction
data["DiabetesPedigreeFunction"] = Robustscaler.fit_transform(data["DiabetesPedigreeFunction"].to_numpy().reshape(-1, 1))


# Check Outliers
columnName = "Insulin"
sns.boxplot(x=data[columnName])
plt.title(columnName +' After Normalized')
plt.show()


# Corelation Matrix
data2 = data[(data["Outcome"] == 0)]
data3 = data[(data["Outcome"] == 1)]

corF = data2[["Pregnancies", "Glucose", "BloodPressure", "SkinThickness","Insulin","BMI","DiabetesPedigreeFunction","Age"]].corr()
corM = data3[["Pregnancies", "Glucose", "BloodPressure", "SkinThickness","Insulin","BMI","DiabetesPedigreeFunction","Age"]].corr()
import seaborn as sns

sns.heatmap(corM, vmin=-1, vmax=1, annot=True)
plt.show()


from sklearn.metrics import accuracy_score
import time
from sklearn.model_selection import train_test_split

# Split the data into features and target
# X = data.drop('Outcome', axis=1)
X = data.drop(columns=['Outcome','BMI'])
print(X.to_string())
print(X.describe().to_string())

y = data['Outcome']
# Split the data into training and testing sets (with a 60/40 split)


#
# from sklearn.datasets import make_classification
# from imblearn.under_sampling import RandomUnderSampler
# # Generate the dataset
# X, y = make_classification(n_classes=2, class_sep=2, weights=[0.1, 0.9],
#                            n_informative=3, n_redundant=1, flip_y=0,
#                            n_features=20, n_clusters_per_class=1,
#                            n_samples=5000, random_state=10)
# # Apply the random under-sampling
# rus = RandomUnderSampler()
# X, y = rus.fit_resample(X, y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4)

# # Decision Tree
# from sklearn.tree import DecisionTreeClassifier
# dtModel = DecisionTreeClassifier()
# startTime = time.time()
# # Building the model using the training data set
# dtModel.fit(X_train, np.ravel(y_train))
# # Evaluating the model using testing data set
# dtY_pred = dtModel.predict(X_test)
# dtScore = round(accuracy_score(y_test, dtY_pred), 2)
# dtTime = round(time.time() - startTime, 2)
# # Printing the accuracy and the time taken by the classifier
# print('Accuracy using Decision Tree:', dtScore)
# print('Time taken using Decision Tree:', dtTime)


#
#
# print('##############################################')
#
# # K-Nearest Neighbors
# from sklearn.neighbors import KNeighborsClassifier
# kNNModel = KNeighborsClassifier(n_neighbors=2)
# startTime = time.time()
# # Building the model using the training data set
# kNNModel.fit(X_train, np.ravel(y_train))
# # Evaluating the model using testing data set
# kNNY_pred = kNNModel.predict(X_test)
# kNNScore = round(accuracy_score(y_test, kNNY_pred), 2)
# kNNTime = round(time.time() - startTime, 2)
# # Printing the accuracy and the time taken by the classifier
# print('Accuracy using K-Nearest Neighbors:', kNNScore)
# print('Time taken using K-Nearest Neighbors:', kNNTime)
#
# print('##############################################')
#
# Support Vector Machine
# from sklearn.svm import SVC
# svmModel = SVC(kernel='linear')
# startTime = time.time()
# # Building the model using the training data set
# svmModel.fit(X_train, np.ravel(y_train))
# # Evaluating the model using testing data set
# svmY_pred = svmModel.predict(X_test)
# svmScore = round(accuracy_score(y_test, svmY_pred), 2)
# svmTime = round(time.time() - startTime, 2)
# # Printing the accuracy and the time taken by the classifier
# print('Accuracy using Support Vector Machine:', svmScore)
# print('Time taken using Support Vector Machine:', svmTime)
#
#
# print('##############################################')
#
#
#
# # Neural Networks
# from sklearn.neural_network import MLPClassifier
# nnModel = MLPClassifier()
# startTime = time.time()
# # Building the model using the training data set
# nnModel.fit(X_train, np.ravel(y_train))
# # Evaluating the model using testing data set
# nnY_pred = nnModel.predict(X_test)
# nnScore = round(accuracy_score(y_test, nnY_pred), 2)
# nnTime = round(time.time() - startTime, 2)
# # Printing the accuracy and the time taken by the classifier
# print('Accuracy using Neural Networks:', nnScore)
# print('Time taken using Neural Networks:', nnTime)
#
#
# print('##############################################')

# Naive Bayes
from sklearn.naive_bayes import GaussianNB
nbModel = GaussianNB()
startTime = time.time()
# Building the model using the training data set
nbModel.fit(X_train, np.ravel(y_train))
# Evaluating the model using testing data set
nbY_pred = nbModel.predict(X_test)
nbScore = accuracy_score(y_test, nbY_pred)
nbTime = round(time.time() - startTime, 2)

# Printing the accuracy and the time taken by the classifier

print('Accuracy using Naive Bayes:', nbScore)
print('Time taken using Naive Bayes:', nbTime)


from sklearn.metrics import confusion_matrix
import seaborn as sns
# Generating confusion matrix for Naive Bayes model
nb_cm = confusion_matrix(y_test, nbY_pred)

# Plotting confusion matrix as heatmap using Seaborn
sns.heatmap(nb_cm, annot=True, cmap='crest', fmt='g', xticklabels=['(0)No Diabetes', '(1)Diabetes'], yticklabels=['(0)No Diabetes', '(1)Diabetes'])
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix - Naive Bayes')
plt.show()


# from sklearn.metrics import confusion_matrix
# nbModel = GaussianNB()
# startTime = time.time()
# # Building the model using the training data set
# nbModel.fit(X_train, np.ravel(y_train))
# # Evaluating the model using testing data set
# nbY_pred = nbModel.predict(X_test)
# nbScore = round(accuracy_score(y_test, nbY_pred), 2)
# nbTime = round(time.time() - startTime, 2)
#
# # Generating the confusion matrix
# nbCm = confusion_matrix(y_test, nbY_pred)
# print('Confusion matrix using Naive Bayes:')
# print(nbCm)
#
# # Printing the accuracy and the time taken by the classifier
# print('Accuracy using Naive Bayes:', nbScore)
# print('Time taken using Naive Bayes:', nbTime)

