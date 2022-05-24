import pandas as pd

df = pd.read_csv("final_reviews.csv") 

old_count = df.shape[0]

df = df.drop(["id"], axis=1)

df.drop_duplicates(subset=None, inplace=True)

df.reset_index(inplace=True)

df.columns = ['id','company','opinion','date','rating','source','score','sentiment']

new_count = df.shape[0]

dups = old_count - new_count

if dups <= 0: print('No duplicates found!')
else: print(f'{dups} duplicates found')

df.to_csv("final_reviews.csv",index=False)