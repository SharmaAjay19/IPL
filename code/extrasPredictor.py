import pandas as pd

trainpath = '../data/train/train/'
testpath = '../data/test/test/'

df = pd.read_csv(trainpath+'ball_by_ball_data.csv')

df1 = df.groupby(['match_id', 'inning', 'batting_team', 'bowling_team']).apply(lambda x: x['extra_runs'].sum()).reset_index(name='extra_runs')
df1['match_year'] = df1['match_id'].apply(lambda x: int(x.split('_')[0]))
#df1 = df1[['inning', 'batting_team', 'bowling_team', 'extra_runs', 'match_year']]
print(df1.head())

#team1 = 'KKR'
#team2 = 'RCB'

#print(df1['inning'])

#df2 = df1.loc[(df1['batting_team'].isin([team1, team2])) | (df1['bowling_team'].isin([team1, team2]))]
#df1.to_csv('../data/transformed/extras.csv', index=False)
#print(df1.head())

'''df = pd.read_csv(testpath + 'total_extras.csv')
df['match_year'] = df['match_id'].apply(lambda x: int(x.split('_')[0]))
df = df[['match_id', 'team1_id', 'team2_id', 'match_year']]

newdf = pd.DataFrame(columns = ['inning', 'batting_team', 'bowling_team', 'extra_runs', 'match_year'])
i = 0
for index, row in df.iterrows():
	newdf.loc[i+0] = [1, row['team1_id'], row['team2_id'], 0, row['match_year']]
	newdf.loc[i+1] = [2, row['team1_id'], row['team2_id'], 0, row['match_year']]
	newdf.loc[i+2] = [1, row['team2_id'], row['team1_id'], 0, row['match_year']]
	newdf.loc[i+3] = [2, row['team2_id'], row['team1_id'], 0, row['match_year']]
	i = i+4

newdf['inning'] = newdf['inning'].apply(lambda x: int(x))
print(newdf.head())

newdf.to_csv('../data/transformed/testdata.csv', index=False)'''