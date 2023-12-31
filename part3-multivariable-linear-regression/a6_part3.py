import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

#imports and formats the data
data = pd.read_csv("part3-multivariable-linear-regression/car_data.csv")
x = data[["miles","age"]].values
y = data["Price"].values

#split the data into training and testing data
xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size = .2)

#create linear regression model
model = LinearRegression().fit(xtrain, ytrain)

#Find and print the coefficients, intercept, and r squared values. 
#Each should be rounded to two decimal places. 
coef = np.around(model.coef_, 2)
bias = round(float(model.intercept_), 2)
r_squared = round(model.score(x, y),2)

print(f"Model's Liner Equation: y={coef[0]}x1 + {coef[1]}x2 + {bias}")
print("R Squared value: ", r_squared)

predict = model.predict(xtest)
predict = np.around(predict, 2)

#Loop through the data and print out the predicted prices and the 
#actual prices
print("***************")
print("Testing Results")
print("\nTesting Multivariable Model With Testing Date:")

for index in range (len(xtest)):
    real_val = ytest[index]
    expected_val = predict[index]
    x_coordinate = xtest[index]
    print(f"Car miles: {x_coordinate[0]} \nCar age: {x_coordinate[1]} \nActual: {real_val} \nPredicted: {expected_val}")
    print("\n")
