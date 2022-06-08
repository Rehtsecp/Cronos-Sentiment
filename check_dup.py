from hashlib import new
from re import sub
import pandas as pd

df = pd.read_csv("cronos_reviews.csv")

old_count = len(df.index) 

df = df.astype("str")

df = df.drop(["index"], axis=1)

num_dup = df.duplicated().sum()

print(f"{num_dup} duplicates found")

df.drop_duplicates(subset="opinion", inplace=True)

df = df.replace('\r\n','. ', regex=True)

df.reset_index(
    inplace=True,
)

new_count = len(df.index)

diff_count = new_count - old_count

if diff_count < 0: print(f'Found 0 new review(s)')
else: print(f'Found {diff_count} new review(s)')

df.to_csv("cronos_reviews.csv", index=False)
