from re import sub
import pandas as pd

df = pd.read_csv("cronos_reviews.csv")

df = df.astype("str")

df = df.drop(["index"], axis=1)

num_dup = df.duplicated().sum()

print(f"{num_dup} duplicates found")

df.drop_duplicates(subset="opinion", inplace=True)

df.reset_index(
    inplace=True,
)


df.to_csv("cronos_reviews.csv", index=False)
