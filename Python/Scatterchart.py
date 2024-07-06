import matplotlib.pyplot as plt
import numpy as np
#Generating random data
np.random.seed(0)
x=np.random.rand(50)
y=np.random.rand(50)
#Creating the scatter plot
plt.scatter(x,y)
#Adding the lables and title
plt.xlabel('x axis')
plt.ylabel('y axix')
plt.title('Scatter Graph')
#Displaying the graph
plt.show()