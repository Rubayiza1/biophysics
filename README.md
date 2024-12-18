REQUIREMENTS

The class has four methods and two attributes.
METHODS

1)init

initialize class with a dataframe object. 
eg.
```
# importing and making a dataframe df
df = pd.read_excel("sample_data.xlsx")
# initialize class with dataframe object (df)
table = droplets(df)
```
2)track & 3)max_size & 4) rejects

track every droplet in frame 62 (index 777-837) and return them each at their maximum sizes, then find droplets
rejected for circularity violations
eg. 
```
index = np.linspace(777,837,61)
df1 = pd.DataFrame()
for data in index:
    df2 = droplets.max_size(table.track(int(data)))
    df1 = pd.concat([df1,df2])
rejects = droplets.rejects(df1)  # return all non-circular droplets in the dataframe
```
ATTRIBUTES
1) threshold

change threshold values
eg.
```
droplets.threshold = 0.1
```
2) circularity

toggle filter for circularity: True or False 
eg.
```
droplets.circularity = True
```

DESCRIPTION
This class used to analyse droplets. It will produce a filtered subtable of a 
droplet's profile: its location, area, cirularity and any other available properties across every 
frame. The user must set a threshold value for to account for the minor deviations in position. The class also has methods 
to further exclude droplets that don't meet circularity requirements. The user must also set the preferred circularity range 
for this. This means that the main script is responsible for encoding the loop that will call this class for
all the droplets in the chosen frame. And the user is responsible for using droplets from the best frame 
to achieve a desired outcome.

USAGE:
The frame where the threshold value is obtained should be recorded. This should be the ideal frame the class is called for.
The loop in the main script should then call this class at that frame.  

This method is thus as effective as the user is at identifying the most useful frames to analyse. Droplets that don't show
up in the proposed frame will not be counted. This needn't be fatal. The class can easily be called at different starting
frames and the best outcome picked. This SHOULD converge to a similar set of frames, much like a Markov Chain converges to
some position of local minimum. 

INCOMING FEATURES:
In development is a function that will loop through the entire dataframe to find ideal primary frames based on droplet count 
per frame. Naturally, this will serve very specific cases but can be reasonably tweaked to find primary frames based on other
properties present in the data frame. For instance, the frame with the minimum spread in circularity about the ideal average.

Also, the class will be made to accept a folder path, check for data files within the directory and sequentially analyze every
data file found, then save the outputs in the same folder with the same file name plus a small appendage.
