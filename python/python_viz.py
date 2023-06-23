
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# Example 1 
x = np.linspace(0, 10, 100)

plt.figure()
  plt.plot(x, np.sin(x))
  plt.plot(x, np.cos(x))
  plt.show()
plt.close() # Very important to close the figure 


# Example 2
plt.figure()
  plt.plot(x, np.sin(x), '-')
  plt.plot(x, np.cos(x), '--');
  plt.show()
plt.close()


# Example 3: color and line style
plt.figure()
  plt.plot(x, np.sin(x), '-r') # solid red
  plt.plot(x, np.cos(x), '--b') # dashed blue
  plt.show()
plt.close()

# Example 4
t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2*np.pi*t)

plt.figure()
  plt.plot(t, s)
  plt.xlabel('time')
  plt.ylabel('sine function')
  plt.title('This is a title')
  plt.grid(True)
  #plt.savefig("test.png") # save figure
  plt.show()
plt.close()



# Example 5: Subplots
plt.figure()  # create a plot figure

       # create the first of two panels and set current axis
       plt.subplot(2, 1, 1) # (rows, columns, panel number)
       plt.plot(x, np.sin(x))

       # create the second panel and set current axis
       plt.subplot(2, 1, 2)
       plt.plot(x, np.cos(x))
plt.show()
plt.close()


# Axes limits
plt.figure()
  plt.plot(x, np.sin(x), '-')
  plt.plot(x, np.cos(x), '--')
  plt.xlim(-10,15)
  plt.ylim(-2,2)
  plt.grid()
  plt.show()
plt.close()


# Legend
plt.figure()
  plt.plot(x, np.sin(x), '-r', label="sin(x)")
  plt.plot(x, np.cos(x), '--b',label="cos(x)")
  plt.grid()
  plt.legend()
  plt.show()
plt.close()


# Scatter
x = np.random.normal(size=100)  
plt.figure()
  plt.plot(x, 'or', label="Normal Random Numbers")
  plt.grid()
  plt.legend()
  plt.show()
plt.close()


#  Plot a data set
from sklearn.datasets import load_iris 
iris = load_iris()
df_iris = pd.DataFrame(iris.data)
df_iris.columns = iris.feature_names
plt.figure()
  plt.scatter(df_iris.iloc[:,0],df_iris.iloc[:,1], c=iris.target,s=100*df_iris.iloc[:,3])
  plt.xlabel(iris.feature_names[0])
  plt.ylabel(iris.feature_names[1])
  plt.grid()
  plt.legend()
  plt.show()
plt.close()



#  boxplot
plt.figure()
  plt.boxplot(df_iris)
  plt.xticks([1, 2, 3, 4], iris.feature_names)
  plt.grid()
  plt.show()
plt.close()




#  histogram
plt.figure()
  plt.hist(df_iris.iloc[:,0])
  plt.show()
plt.close()
