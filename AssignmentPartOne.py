#import libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy import special

#qfunction
def Qfunction(x):
    return 0.5 * special.erfc( x / np.sqrt(2) )

#Values from 2 to 7 for x-axis with 1000 point
x = np.linspace(2, 7, num=1000)
y = Qfunction(x)

#A1
Q1 = np.exp(-(x**2)/2)

#A2
Q2 = 1/4 * np.exp(-(x**2)) + 1/4 * np.exp(-(x**2)/2)

#A3
Q3 = 1/12 * np.exp(-(x**2)/2) + 1/4 * np.exp(-(2*x**2)/3)


#First close all plots
plt.close('all')

#figure 1
plt.figure(1)
plt.title('Compare Q and Q1 functions')
# convert y-axis to Logarithmic scale
plt.yscale("log")
plt.plot(x, y,label='Qfunction')
plt.plot(x,Q1, linestyle='dashed', linewidth = 3, label='Q1 function')
plt.xlabel('x')
plt.ylabel('Q(x)')

#For showing labels for different graphs
plt.legend()


##figure 2
plt.figure(2)
plt.title('Compare Q and Q2 functions')
# convert y-axis to Logarithmic scale
plt.yscale("log")
plt.plot(x, y,label='Qfunction')
plt.plot(x,Q2, linestyle='dashed', linewidth = 3, label='Q2 function')
plt.xlabel('x')
plt.ylabel('Q(x)')

#For showing labels for different graphs
plt.legend()


##figure 3
plt.figure(3)
plt.title('Compare Q and Q3 functions')
# convert y-axis to Logarithmic scale
plt.yscale("log")
plt.plot(x, y,label='Qfunction')
plt.plot(x,Q3, linestyle='dashed', linewidth = 3, label='Q3 function')
plt.xlabel('x')
plt.ylabel('Q(x)')

#For showing labels for different graphs
plt.legend()

#For Q1 function, where y is Q(x) function
e1 = abs(Q1-y)/abs(y)

#We use trapz function from numpy library for calculate integration
print('e1 = %f' %np.trapz(e1,x))

#For Q2 function, where y is Q(x) function
e2 = abs(Q2-y)/abs(y)

print('e2 = %f' %np.trapz(e2,x))

#For Q3 function, where y is Q(x) function
e3 = abs(Q3-y)/abs(y)

print('e3 = %f' %np.trapz(e3,x))

