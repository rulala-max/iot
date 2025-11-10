import pandas as pd
import seaborn as sns

df = sns.load_dataset('penguins')
# print(df.info())
# print(df.tail())
# print(df.describe())
# print(df['body_mass_g'].describe())
print(df[df['bill_length_mm'] >= 55.0])
