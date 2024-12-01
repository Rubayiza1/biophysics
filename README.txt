The following is a class used to analyse droplets. It will produce a filtered subtable of a 
droplet's profile: its location, area, cirularity and any other available properties across every 
frame. The user must set a threshold value. The class also has methods to further exclude droplets
that don't meet circularity requirements. The user must also set a range for this. 
This means that the main script is responsible for encoding the loop that will call this class for
all the droplets in the frame. And the user is responsible for using droplets from the best frame 
to achieve a desired outcome.

The frame where the threshold value is obtained should be recorded. This should be the ideal frame the class is called for.
The loop in the main script should then call this class at that frame in both forward and backward directions for the entire
dataframe. This class can then be made to accept, as input, some 'primary frame' to locate the starting point. This means 
that the loop in the main script must accomodate for every droplet in the primary frame. 

This method is thus as effective as the user is at identifying the most useful frames to analyse. Droplets that don't show
up in the proposed frame will not be counted. This needn't be fatal. The class can easily be called at different starting
frames and the best outcome picked. This SHOULD converge to a similar set of frames, much like a Markov Chain converges to
some position of local minimum. 

