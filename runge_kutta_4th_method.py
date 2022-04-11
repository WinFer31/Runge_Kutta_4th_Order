#Runge-Kutta method implementation, for 4th order equations

#Credits: Panchenko Dmitriy (D.Panchenko@stud.satbayev.university)

import numpy as np
import matplotlib.pyplot as plt

def runge_kutta(f, x_0, y_0, h):

    k_0 = f(x_0, y_0)
    k_1 = f(x_0 + h/2, y_0 + h/2 * k_0)
    k_2 = f(x_0 + h/2, y_0 + h/2 * k_1)
    k_3 = f(x_0 + h, y_0 + h * k_2)

    k = 1/6 * (k_0 + 2.0*k_1 + 2.0*k_2 + k_3)

    x_1 = x_0 + h
    y_1 = y_0 + h * k

    return x_1, y_1

#Init function
def df(x, y):
    return y + (np.exp(x)/x) 



#Initial Values
x_0 = 1.0
y_0 = 0.0
a = 1
b = 2
h = 0.2
range_values = np.arange(a, b, h)
x_values = [x_0]
y_values = [y_0]

y_calculated = np.exp(range_values)+np.log10(range_values)

#Calculate solution
x = x_0
y = y_0
for _ in range(len(range_values)):
    x, y = runge_kutta(df, x, y, h)
    y_calculated_2 = np.exp(x)+np.log10(x)
    x_values.append(x)
    y_values.append(y)
    print('x \t\t y \t\t f(x)')
    print('%f \t %f \t %f'% (x, y, y_calculated_2))

#Plot solution
plt.grid()
plt.title('y(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.plot(x_values, y_values,  "bs-", label="Runge_Kutta")
plt.plot(range_values, y_calculated,  "mh-", label="Groud Truth")
leg = plt.legend()
plt.show()