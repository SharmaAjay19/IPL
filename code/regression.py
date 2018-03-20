import pandas as pd

trainpath = '../data/train/train/'
testpath = '../data/test/test/'

df = pd.read_csv(trainpath+'ball_by_ball_data.csv')
matches = pd.read_csv(trainpath+'match_data.csv')[['match_id', 'venue']]
df = pd.merge(df, matches, on='match_id')
df1 = df.groupby(['match_id', 'inning', 'batting_team', 'bowling_team', 'venue']).apply(lambda x: x['extra_runs'].sum()).reset_index(name='extra_runs')
df1['match_year'] = df1['match_id'].apply(lambda x: int(x.split('_')[0]))
df1['inning'] = df1['inning'].apply(lambda x: int(x))
df1 = df1.drop('match_id', axis=1)


from sklearn.preprocessing import LabelEncoder
enc1 = LabelEncoder()
enc1.fit(df1['batting_team'].values)
df1['batting_team'] = enc1.transform(df1['batting_team'].values).tolist()
df1['bowling_team'] = enc1.transform(df1['bowling_team'].values).tolist()

enc2 = LabelEncoder()
enc2.fit(df1['venue'].values)
df1['venue'] = enc2.transform(df1['venue'].values).tolist()

print(df1.head())

features = df1[['inning', 'batting_team', 'bowling_team', 'match_year']].values
labels = df1['extra_runs'].values


from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
X_train, X_test, y_train, y_test = train_test_split(features, labels,
									test_size=0.2, random_state=42)

print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)

from sklearn import linear_model
from sklearn.svm import SVR
models = [
('LinearRegression', linear_model.LinearRegression()),
('RidgeRegression', linear_model.Ridge(alpha = 0.5)),
('RidgeCV', linear_model.RidgeCV(alphas=[0.1, 1.0, 10.0])),
('Lasso', linear_model.Lasso(alpha = 0.1)),
('LassoCV', linear_model.LassoCV()),
('PassiveAggressiveRegressor', linear_model.PassiveAggressiveRegressor()),
('Perceptron', linear_model.Perceptron())]
''',
('svr_rbf', SVR(kernel='rbf', C=1e3, gamma=0.1)),
('svr_lin', SVR(kernel='linear', C=1e3)),
('svr_poly', SVR(kernel='poly', C=1e3, degree=2)),
]'''
for name, model in models:
	print('\n\n#####', name, '####\n')
	model.fit(X_train, y_train)
	predictions = model.predict(X_test)
	print("Mean squared error: %.2f"
      % mean_squared_error(y_test, predictions))
	# Explained variance score: 1 is perfect prediction
	print('Variance score: %.2f' % r2_score(y_test, predictions))