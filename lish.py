import numpy as np

def lish(x):
 x = np.asarray(x)
 return x * np.tanh(x)