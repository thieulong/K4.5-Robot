import numpy as np
from sklearn.linear_model import LinearRegression

array = [114.66867685317993, 116.8715500831604, 118.66491079330444, 123.63198280334473, 129.02202129364014, 135.0426721572876, 141.81342601776123, 151.02843761444092, 162.7940797805786, 175.3644561767578, 187.33444690704346, 201.72775268554688, 216.85930252075195, 230.8872127532959, 240.2050495147705, 252.20131874084473, 260.0706195831299, 274.49864387512207, 294.4688415527344, 338.37284088134766]

x = np.array(range(0,len(array))).reshape((-1,1))
y = np.array(array)

model = LinearRegression()
model = LinearRegression().fit(x, y)

r_sq = model.score(x, y)
print(f"coefficient of determination: {r_sq}")

print(f"intercept: {model.intercept_}")

print(f"slope: {model.coef_}")