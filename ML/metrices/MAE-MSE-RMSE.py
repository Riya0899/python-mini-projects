'''
1. mean absolute error (MAE)- it is the average of absolute differences between predicted and actual values. It gives an idea of how much the predictions deviate from the actual values on average.
take the mistake difference,remove the negative sign , add them and divide by total number of predictions

2. mean squared error (MSE)- it is the average of squared differences between predicted and actual values. It penalizes larger errors more heavily than MAE.
take the mistake difference, square it, add them and divide by total number of predictions

3. root mean squared error (RMSE)- it is the square root of MSE. It is in the same units as the target variable and gives an idea of the typical magnitude of the prediction errors.
take the mistake difference, square it, add them and divide by total number of predictions and then take the square root of that result

'''

from sklearn.metrics import mean_absolute_error,mean_squared_error
import numpy as np

real_scores=[90,60,80,100]
model_guess=[85,70,70,95]

mae=mean_absolute_error(real_scores,model_guess)
mse=mean_squared_error(real_scores,model_guess)
rmse=np.sqrt(mse)

print("mean absolute error:",mae)
print("mean squared error:",mse)
print("root mean squared error:",rmse)