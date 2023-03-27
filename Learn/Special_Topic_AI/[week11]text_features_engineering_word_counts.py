import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

sample = ['problem of evil','evil queen','horizon problem']

vec = CountVectorizer()
X = vec.fit_transform(sample)
df = pd.DataFrame(X.toarray(), columns=vec.get_feature_names_out())

# from sklearn.feature_extraction.text import TfidfVectorizer
#
# vec = TfidfVectorizer()
# X = vec.fit_transform(sample)
# df2 = pd.DataFrame(X.toarray(),columns = vec.get_feature_names_out())

print(df)