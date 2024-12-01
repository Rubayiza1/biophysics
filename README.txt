The class has four methods and two attributes.
METHODS

1)init

initialize class with a dataframe object. 
eg.

# importing and making a dataframe df
df = pd.read_excel("sample_data.xlsx")
# initialize class with dataframe object (df)
table = droplets(df)

2)track & 3)max_size & 4) rejects

track every droplet in frame 62 (index 777-837) and return them each at their maximum sizes
eg. 

index = np.linspace(777,837,61)
df1 = pd.DataFrame()
for data in index:
    df2 = droplets.max_size(table.track(int(data)))
    df1 = pd.concat([df1,df2])
rejects = droplets.rejects(df1)  # return all non-circular droplets in the dataframe

ATTRIBUTES
1) threshold

change threshold values
eg.

droplets.threshold = 0.1

2) circularity

toggle filter for circularity: True or False 
eg.

droplets.circularity = True
DESCRIPTION
This class used to analyse droplets. It will produce a filtered subtable of a 
droplet's profile: its location, area, cirularity and any other available properties across every 
frame. The user must set a threshold value. The class also has methods to further exclude droplets
that don't meet circularity requirements. The user must also set a range for this. 
This means that the main script is responsible for encoding the loop that will call this class for
all the droplets in the frame. And the user is responsible for using droplets from the best frame 
to achieve a desired outcome.

Using the class:
The frame where the threshold value is obtained should be recorded. This should be the ideal frame the class is called for.
The loop in the main script should then call this class at that frame in both forward and backward directions for the entire
dataframe. This class can then be made to accept, as input, some 'primary frame' to locate the starting point. This means 
that the loop in the main script must accomodate for every droplet in the primary frame. 

This method is thus as effective as the user is at identifying the most useful frames to analyse. Droplets that don't show
up in the proposed frame will not be counted. This needn't be fatal. The class can easily be called at different starting
frames and the best outcome picked. This SHOULD converge to a similar set of frames, much like a Markov Chain converges to
some position of local minimum. 

