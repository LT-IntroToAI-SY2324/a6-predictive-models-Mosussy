# Part 3 - Multivariable Linear Regression Writeup

After completing `a6_part3.py` answer the following questions

## Questions to answer

1. What is the R Squared coefficient for your model? What does that mean about the model in relation to your data?
The r squared value for the model is .86 which means that there is a strong correlation which can help us conclude that as age and mileage on a car increase the price of said car decreases. 

2. Is your model accurate? Why or why not?
The model is fairly accurate as its predictions are typically 500 dollars off in either direction of the actual value for the mileage and year of the car. There are also few outliers in our data, but they are not big enough to cause our mean to skew left or right. 

3. What does the model predict a 10-year-old car with 89000 miles is worth? What about a car that is 20 years old with 150000 miles?
The model predicts:
10 year old car with 89,000 miles = $9,273.66
20 year old car with 150,000 miles = $2442.09

4. You may notice that some of your predicted results are negative. This is occurring when the value of age and the mileage of the car are very high. Why do you think this is happening?
This is happening because our model is linear so it has to consistently move down in a straight line rather than the line moving like a exponentially decreasing line which would better represent the price of a car as you can’t possibly owe someone money when you sell a car. 