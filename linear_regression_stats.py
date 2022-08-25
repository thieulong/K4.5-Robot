import numpy as np
from sklearn.linear_model import LinearRegression

array = [89.02642965316772, 288.36825370788574, 245.44684410095215, 224.36920166015625, 219.76252555847168]

x = np.array(range(0,len(array))).reshape((-1,1))
y = np.array(array)

model = LinearRegression()
model = LinearRegression().fit(x, y)

r_sq = model.score(x, y)
print(f"coefficient of determination: {r_sq}")

print(f"intercept: {model.intercept_}")

print(f"slope: {model.coef_[0]}")