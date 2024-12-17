import pandas as pd
import numpy as np
import droplets
import os

# Define the path to the folder
folder_path = 'path/to/your/folder'

# Loop through all files in the folder
for filename in os.listdir(folder_path):
    # Construct the full file path
    file_path = os.path.join(folder_path, filename)
    
    # Check if it's a file (and not a subdirectory)
    if os.path.isfile(file_path):
        try:
            # Open the file
            df = pd.read_excel(file_path)
            # initialize class with dataframe object (df)
            table = droplets(df)
            # edit the following lines to call droplet class across a range of evenly spaced frames and pick the result with the largest count.
            index = np.linspace(777,837,61)
            df1 = pd.DataFrame()
            df1.to_csv(str(filename)+"_results",index=False)
            for data in index:
                df2 = droplets.max_size(table.track(int(data)))
                df1 = pd.concat([df1,df2])
            rejects = droplets.rejects(df1)  # return all non-circular droplets in the dataframe
            rejects.to_csv(str(filename)+"_rejects",index=False)



