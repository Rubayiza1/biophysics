import numpy as np
import pandas as pd
import xlrd

class droplets:
    global threshold, circularity
    
    threshold = 1  # threshold to track the droplet's position
    circularity = True  # option to exclude droplets that do not meet circularity requirements
    
    def __init__(self, data):
        self.data = pd.DataFrame(data)  # initialized dataframe with data object

    def track(self, index):
        """
        Filter records based on droplet position. Takes droplet index as input.
        """
        # get droplet position
        x = self.data.iloc[index]['X']  # x-position
        y = self.data.iloc[index]['Y']  # y-position
        R = np.sqrt(x**2 + y**2)  # euclidean
        condition = threshold
        # get subtable of droplet profile 
        profile = df[abs(np.sqrt(df['X']**2+df['Y']**2)-R) <= condition] 
        if circularity == True:
            profile = df[(abs(np.sqrt(df['X']**2+df['Y']**2)-R) <= condition) & (abs(df['Circularity']-1) <= 0.01)]
        return profile
    
    def max_size(profile):
        '''
        takes a droplet profile as input and selects the droplet at its max size and returns that record.
        '''
        df = pd.DataFrame(profile)
        output = df[df['Area']==df['Area'].max()]
        return output    
        
        '''
        Must be able to return both a summary of all droplets and the droplets at their max area 
        '''
    def rejects(output):
        '''
        looks for all non-circular droplets
        '''
        df = pd.DataFrame(output)
        reject = df[(df['Circularity'] <= 0.9) & (df['Circularity'] >= 1.0)]
