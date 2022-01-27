import numpy as np
import pandas as pd
import seaborn
import matplotlib.pyplot as plt

seaborn.set(rc={'figure.figsize':(11.7,8.27)})

# Get a vector of 100 uniform distributed values
# between 0 and 2
X = 2 * np.random.rand(100, 1)
# Setup the linear model, with an additional 
# error term that is normally distributed
Y = 4 + 3 * X + np.random.randn(100, 1)
data = pd.DataFrame({"X": X.T[0], "Y": Y.T[0]})
seaborn.scatterplot(data=data, x="X", y="Y")
plt.show()