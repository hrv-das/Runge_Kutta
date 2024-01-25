import numpy as np
import matplotlib.pyplot as plt
l1 = 3
l2 = -3
f1 = lambda t,y: l1*y
f2 = lambda t,y: l2*y 
h = [0.5,0.1]
y0 = 1
t = [[],[]]
y_l1 = [[],[]]
y_l2 = [[],[]]
for i in range(len(h)):
    yi = y0
    for j in np.arange(0,10.1,h[i]):
        t[i].append(j)
        y_l1[i].append(yi)
        k1 = h[i]*f1(j,yi)
        k2 = h[i]*f1(j+(h[i]/2),yi+(k1/2))
        k3 = h[i]*f1(j+(h[i]/2),yi+(k2/2))
        k4 = h[i]*f1(j+h[i],yi+k3)
        yi = yi+((k1+(2*k2)+(2*k3)+k4)/6)
for i in range(len(h)):
    yi = y0
    for j in np.arange(0,10.1,h[i]):
        y_l2[i].append(yi)
        k1 = h[i]*f2(j,yi)
        k2 = h[i]*f2(j+(h[i]/2),yi+(k1/2))
        k3 = h[i]*f2(j+(h[i]/2),yi+(k2/2))
        k4 = h[i]*f2(j+h[i],yi+k3)
        yi = yi+((k1+(2*k2)+(2*k3)+k4)/6)


t_ax = np.linspace(0,10,100)
y_l1_exact = np.exp(l1*t_ax)
y_l2_exact = np.exp(l2*t_ax)

fig,(ax1,ax2) = plt.subplots(1,2,figsize=(15,5))
ax1.plot(t[0],y_l1[0],'ro-',label="h = 0.5")
ax1.plot(t[1],y_l1[1],'yo-',label="h = 0.1")
ax1.plot(t_ax,y_l1_exact,'k--',label="Exact Analytic Solution")
ax1.set_title(r'$\lambda$ = +3', size = 15)
ax1.set_xlabel(r't $\rightarrow$', size = 12)
ax1.set_ylabel(r'y(t) $\rightarrow$', size = 12)
ax1.legend(loc="best")
ax1.grid(True,which="both")
ax2.plot(t[0],y_l2[0],'ro-',label="h = 0.5")
ax2.plot(t[1],y_l2[1],'yo-',label="h = 0.1")
ax2.plot(t_ax,y_l2_exact,'k--',label="Exact Analytic Solution")
ax2.set_title(r'$\lambda$ = -3', size = 15)
ax2.set_xlabel(r't $\rightarrow$', size = 12)
ax2.set_ylabel(r'y(t) $\rightarrow$', size = 12)
ax2.legend(loc="best")
ax2.grid(True,which="both")
plt.suptitle("Plot for Comparison of Different Solutions",size = 18, weight= "bold")
plt.show()
