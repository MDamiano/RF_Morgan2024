from sklearn.utils import shuffle
import sklearn.ensemble
import pandas as pd
import numpy as np
import os

path = os.path.abspath(__file__)
file_dir = os.path.dirname(path) + '/'

class RF_Morgan2024:
    def __init__(self, mod):
        self.seed = np.random.seed(42)  # DON'T PANIC!
        assert mod == 'VIS' or mod == 'NUV' or mod == 'NIR', "Please select one of the following wavelength band: 'VIS', 'NUV', or 'NIR'."
        self.mod = mod
        self.fldr = file_dir

        # Load the dataset
        xls = pd.ExcelFile(self.fldr + 'Morgan2024_dataset.xls')
        self.dat = pd.read_excel(xls, 'Morgan2024_dataset')

        # Filter for the wavlength band
        self.dat = self.dat.loc[self.dat['mode'] == self.mod]

        # Filter for yield lower than 5
        self.dat = self.dat.loc[self.dat['chars_earth_unique'] > 5]

        # Shuffle the DataFrame
        train_df = shuffle(self.dat)

        # Drop non useful columns from the DataFrame
        train_X, train_y = train_df.drop(['experiment', 'mode', 'Diameter', 'contrast', 'Throughput', 'chars_earth_unique', 'detections_earth_all', 'detections_earth_unique', 'ensemble_size'], axis = 1), train_df.chars_earth_unique
        
        # Define and fit the RF
        self.model = sklearn.ensemble.RandomForestRegressor(800, max_depth=10, random_state=self.seed)
        self.model.fit(train_X.values, train_y.values)
        
    def sim(self, diameter, logc, tput, iwa):
        # Check if the input values are within the learning boundaries
        assert 6 <= diameter <= 9, "The telescope diameter must be provided in the range [6, 9]."
        
        assert -11 <= logc <= -9 , "The log-contrast ratio must be provided in the range [-11, -9]."

        assert 0.1 <= tput <= 0.6, "The telescope throughput must be provided in the range [0.1, 0.6]."
        
        assert 20 <= iwa <= 70, "The IWA must be provided in the range [20, 70]."
        
        # Calculate the effective area
        ea = ((diameter / 2.) ** 2.) * tput
        # Define the input array for the RF
        arr = np.array([logc, iwa, ea]).reshape(1, -1)
        # Return the simulated Earth-like characterization yield value
        return self.model.predict(arr)[0]
