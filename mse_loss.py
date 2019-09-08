import numpy as np


def mse_loss(param_true,param_predicted):
    #true and predicted are arrays of same length
    return ((param_true-param_predicted)**2).mean()

true_vals   = np.array([1,0,0,1])
false_vals = np.array([0,0,0,0])

print(mse_loss(true_vals,false_vals))

