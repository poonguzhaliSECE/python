import matplotlib.pyplot as plt
import numpy as np
#Generating random data
np.random.seed(0)
data=np.random.normal(0, 1, 100)
#Creating a box plot
plt.boxplot(data)
#Adding labels and title
plt.xlabel('x axis')
plt.ylabel('y axix')
plt.title('Box Graph')
#Displaying the plot
plt.show()