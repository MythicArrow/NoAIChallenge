import matplotlib.pyplot as plt
import numpy as np
class Graph:
  def __init__(self,a,x,b):
    self.a = a
    self.x = x
    self.b = b
  def createLinGraph(a,x,b):
    y = a*x + b
    plt.plot(x,y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()
  def createQuadraticGraph(a,x,b):
    y = a*x**2 + b
    plt.plot(x,y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()
  def createSinGraph(a,x,b):
    y = np.sin(a*x+b)
    plt.plot(x,y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()
#Trials
Graph.createLinGraph(1,2,3)
Graph.createQuadraticGraph(1,2,3)
Graph.createSinGraph(1,2,3)
