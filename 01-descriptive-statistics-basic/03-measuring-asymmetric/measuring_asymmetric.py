import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
 
jumlah_kucing = np.array([3, 2, 1, 1, 2, 3, 2, 1, 0, 2])


plt.hist(jumlah_kucing, bins=4)
plt.show()

jumlah_kucing_series = pd.Series(jumlah_kucing)
print(jumlah_kucing_series.skew())