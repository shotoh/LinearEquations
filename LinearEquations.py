import numpy as np

f = open('input.txt', 'r')  # open file
equations = []
for _ in range(4):
    # reads the line and splits with space delimiter
    # maps each element in the list from a string to an integer
    # converts the iterator into a list and appends to equations
    equations.append(list(map(int, f.readline().split(' '))))
matrix = np.array(equations)  # creates the 4x4 matrix
# do the same thing above but for the coefficients
coefficients = np.array(list(map(int, f.readline().split(' '))))

matrix_inverse = np.linalg.inv(matrix)  # finds the inverse of the matrix
solution = np.dot(matrix_inverse, coefficients)  # finds the solution with dot product
print(f'Solution is: {solution}')
