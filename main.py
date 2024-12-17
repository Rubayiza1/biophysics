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

            # call droplet class across a range of frames
            stacks = int(df['Frames'].iloc[0])-int(df['Frames'].iloc[-1])  # no. of frames in z-scan
            resolution = stacks  # how often the class should be called. max value = stacks
            
            # find best frame to call class
            count = []
            frame = []
            for i in np.linspace(int(df['Frames'].iloc[0]),int(df['Frames'].iloc[-1]),resolution):
                z = df.loc[df['Frame'] == int(i)]
                count.append(len(z))
                frame.append(i)
            Primary_frame_index = np.argmax(count)
            Primary_frame = frame[Primary_frame_index]
            index = df.loc[df['Frame'] == Primary_frame, 'index']
            
            df1 = pd.DataFrame()

            for data in index:
                df2 = droplets.max_size(table.track(int(data)))
                df1 = pd.concat([df1,df2])
            df1.to_csv(str(filename)+"_results",index=False)
            rejects = droplets.rejects(df1)  # return all non-circular droplets in the dataframe
            rejects.to_csv(str(filename)+"_rejects",index=False)



