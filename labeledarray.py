# Pandas Labeled Array Exercise

import numpy as np
import pandas as pd

a = np.array([5, 7, 19, 20, 32, 2, 5, 8, 13, 4])
a_series = pd.Series(a,index=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"])

b = np.array([[4, 2, 3, 8],
              [1, 5, 7, 4],
              [6, 3, 9, 3],
              [7, 8, 4, 3]])

b_df = pd.DataFrame(b, columns=["A", "B", "C", "D"],
                    index=["I", "II", "III", "IV"])