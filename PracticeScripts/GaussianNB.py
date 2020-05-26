import numpy as np
from sklearn.naive_bayes import GaussianNB

ScatterPlotDataPoints = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
ScatterPlotCategories = np.array([1, 1, 1, 2, 2, 2])

clf = GaussianNB()
clf.fit(ScatterPlotDataPoints, ScatterPlotCategories)
print(clf.predict([[-0.8, -1]]))

