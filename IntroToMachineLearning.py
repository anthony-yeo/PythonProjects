#-------
#SciKit Learn Diagram to determine what type of sorting to use
#-------

import matplotlib.pyplot as plt

from sklearn import datasets
from sklearn import svm #support vector machine, group your labeled data on a  plot

digits = datasets.load_digits()

clf = svm.SVC(gamma = 0.0001, C=100)
#classifier, gamma alters the speed of the algorithm but will affect its precision

print(len(digits.data))

x,y = digits.data[:-10], digits.target[:-10]
clf.fit(x,y)

print('Prediction of last:',clf.predict(digits.data[[-2]]))

plt.imshow(digits.images[-2], cmap = plt.cm.gray_r, interpolation = "nearest")
plt.show()
