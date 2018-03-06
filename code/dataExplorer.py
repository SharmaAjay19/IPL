import pandas as pd

trainpath = '../data/train/train/'
testpath = '../data/test/test/'

df = pd.read_csv(trainpath+'ball_by_ball_data.csv')

print(df.head())