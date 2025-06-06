import numpy as np
def prelu(x,a):
  x = np.asarray(x)
  a = np.asarray(a)
  return np.where(x>=0,x,a*x)
