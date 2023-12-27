#=============MEASURING SPREAD/DISPERSION TENDENCY ====================
## RANGE, INTERQUARTILE RANGE (IQR), 

import numpy as np
import pandas as pd
 

jumlah_kucing = np.array([3, 2, 1, 1, 2, 3, 2, 1, 0, 2])

# Range
range = jumlah_kucing.max() - jumlah_kucing.min()
print("Range:", range) # RANGE = 3

# IQR
iqr = np.percentile(jumlah_kucing, 75) - np.percentile(jumlah_kucing, 25)
print("Interquartile Range:", iqr) 

# inisialisasi pandas series
jumlah_kucing_series = pd.Series(jumlah_kucing)

# Variance
print('Variance:', jumlah_kucing_series.var())

# Standard Deviation
print("Standard Deviation:", jumlah_kucing_series.std())

