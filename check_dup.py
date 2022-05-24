import pandas as pd

df = pd.read_csv("final_reviews.csv") 

df = df.drop(["id"], axis=1)

df.drop_duplicates(subset=None, inplace=True)

df.reset_index(inplace=True)

df.columns = ['id','company','opinion','date','rating','source','score','sentiment']

df.to_csv("final_reviews.csv",index=False)
