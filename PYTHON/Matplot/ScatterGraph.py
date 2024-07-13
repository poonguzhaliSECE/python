import matplotlib.pyplot as plt
import numpy as np
#Gendrating random data
np.random.seed(0)
x=np.random.rand(50)
y=np.random.rand(50)

#Cretating the scatter plot
plt.scatter(x,y)

#Adding labels and title
plt.xlabel('x axis')
plt.ylabel('y axix')
plt.title('Scatter Graph')
#Displaying the plot
plt.show()