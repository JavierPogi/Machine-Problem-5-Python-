import matplotlib.pyplot as plt
import math as math
import numpy as np

num = np.linspace(0,199,200)
def xofn(n):
    return math.sin(math.pi*3*n/100)
#Gives value to x in the problem, to be called in a future function
def yofn(n):
    if n==0:
        return -1.5*xofn(n) + 2*xofn(n+1)- 0.5*xofn(n+2)
    elif n >= 0 and n <= 198:
        return 0.5*xofn(n+1) - 0.5*xofn(n-1)
    else:
        return 1.5*xofn(n) - 2*xofn(n-1)+0.5*xofn(n-2)
    #xofn now acts as x in the problem, with the expression(sin(n*pi*3/100))
    
    
x = [xofn(n) for n in num]
y = [yofn(n) for n in num]
#x and y will be used as data points for the plot
plt.plot(num,x,label = 'X(n)')
plt.plot(num,y,label = 'Y(n)')
#Gives x and y labels that will appear when the legend is enabled
plt.autoscale(enable = True, axis = 'both', tight = True)
#Will make the margins of the graph touch the highest and lowest point of the plotted points.
plt.title("n = 0:199")
#Will be seen on the top of the graph as the title
plt.xlabel("X(n)")
plt.ylabel("Y(n)")
#Will be the labels on the x and y axis
plt.legend(loc="upper right")
#Will enable the legend and let the programmer select its position
plt.grid()
#Will enable grid boxes in the graph
plt.xlim(0,199)
#Will limit the x-values seen upto the set number(199)

    



    
    
        