# Hopfield pattern recognition implementation

#Credits: Panchenko Dmitriy (D.Panchenko@stud.satbayev.university)

import numpy as np

#Samples
x1 = np.array([-1, 1, -1, 1])
x2 = np.array([1, -1, 1, 1])
x3 = np.array([-1, 1, -1, -1])

# x1 = np.array([-1, 1, 1, -1])
# x2 = np.array([-1, 1, -1, 1])
# x3 = np.array([-1, 1, 1, 1])

#Input
y = np.array([-1, 1, -1, -1])

#Convert vector to column and transpose it
def transpose_to_column(x):
    x_t = x.reshape(len(x), 1)
    return np.dot(x_t, x_t.T)


def hopfield(x1, x2, x3, y):

    #Create matrix of transposed samples
    W = transpose_to_column(x1) + transpose_to_column(x2) + transpose_to_column(x3)
    #Set the diagonal of the matrix to zero
    np.fill_diagonal(W, 0)
    #Multiply the matrix by the input vector
    W_y = np.dot(W, y)
    #Get the sign of the result
    sign_y = np.sign(W_y)

    #Find the similar pattern
    if (sign_y == x1).all():
        print("x1:")
    elif (sign_y == x2).all():
        print("x2:")
    elif (sign_y == x3).all():
        print("x3:")
    else:
        print("no simillar pattern")
    return sign_y

print(hopfield(x1, x2, x3, y))