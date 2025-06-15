import numpy as np
def lrelu(a,x):
 # a is a fixed constant differing from the prelu
 a = np.float64()
 x = np.asarray(x)
 return np.where(x>=0,x,x*a)

