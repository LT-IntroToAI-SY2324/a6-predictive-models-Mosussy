# Part 4 - Classification Writeup

After completing `a6_part4.py` answer the following questions

## Questions to answer

1. Comment out the StandardScaler and re-run your test. How accurate is the model? Why is that?
When the StandardScalar is commented out it decreases the accuracy of the model as it goes from approximately .83 to .68 which is a .15 difference. This is because without the data being standardized it means that the answer is going to be backed up by misrepresented data as the salary is going to be a greater number than age. To represent this properly we need to use the scalar so it can more so compare their spread than actual digit values. 

2. How accurate is the model with the StandardScaler? Is this model accurate enough for the given use case? Explain.
The model with the standardscaler is pretty accurate with an accuracy of .83. I believe the model is accurate enough for the given case as it'only has two options so if someone were to randomly guess it would be like a 50-50 chance of getting it right, so it being 83 percent accurate is fine.
3. Looking at the predicted and actual results, how did the model do? Was there a pattern to the inputs that the model was incorrect about?
The model did pretty good at predicting the results correctly. I didn't really notice a pattern with the inputs that were incorrect. 

4. Would a 34 year old Female who makes 56000 a year buy an SUV according to the model? Remember to scale the data before running it through the model.
no
