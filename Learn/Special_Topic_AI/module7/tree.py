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