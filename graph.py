# Importing necessary libraries
import numpy as np
import matplotlib.pyplot as plt

#Create an array of values from 0 to 2π (one full cycle)
x_values=np.linspace(0, 2 * np.pi, 100)

#Calculate sine and cosine values for each x
sine_values=np.sin(x_values)
cosine_values=np.cos(x_values)

#Set up the plot area
plt.figure(figsize=(10, 5))

#Plot sine wave
plt.plot(x_values,sine_values,label='Sine',color='blue',linewidth=2)

#Plot cosine wave
plt.plot(x_values,cosine_values,label='Cosine',color='red',linestyle='--',linewidth=2)

#Add chart title and axis labels
plt.title('Sine and Cosine Waves')
plt.xlabel('Angle (radians)')
plt.ylabel('Amplitude')

#Add a grid and legend for clarity
plt.grid(True,linestyle='--',alpha=0.6)
plt.legend(loc='upper right')

#Adjust layout and display the plot
plt.tight_layout()
plt.show()


