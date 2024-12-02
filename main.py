import pandas as pd
import numpy as np
import droplets

# importing data
df = pd.read_excel("sample_data.xlsx")

# initialize class with dataframe object (df)
table = droplets(df)

# track every droplet in primary frame 62 (index 777-837) and return them each at their maximum sizes 
index = np.linspace(777,837,61)
df1 = pd.DataFrame()
for data in index:
    df2 = droplets.max_size(table.track(int(data)))
    df1 = pd.concat([df1,df2])
rejects = droplets.rejects(df1)  # return all non-circular droplets in the dataframe
