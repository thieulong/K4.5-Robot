import numpy as np
from sklearn.linear_model import LinearRegression

array = [70.93960762023926, 71.3591480255127, 68.57952833175659, 100.8836317062378, 206.76780223846436]

x = np.array(range(0,len(array))).reshape((-1,1))
y = np.array(array)

model = LinearRegression()
model = LinearRegression().fit(x, y)

r_sq = model.score(x, y)
print(f"coefficient of determination: {r_sq}")

print(f"intercept: {model.intercept_}")

print(f"slope: {model.coef_[0]}")