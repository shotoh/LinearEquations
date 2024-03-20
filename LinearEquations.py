import numpy as np

f = open('input.txt', 'r')  # open file
equations = []
coefficients = []
for _ in range(4):
    # reads the line and splits with space delimiter
    # maps each element in the list from a string to an integer
    # converts the iterator into a list
    number_strings = list(map(int, f.readline().split(' ')))
    if len(number_strings) != 5:
        print('Invalid format.')
        exit(1)  # exit if invalid format
    equations.append(number_strings[0:4])  # appends the first 4 elements to the equation
    coefficients.append(number_strings[4])  # appends the last element to the coefficient list
matrix = np.array(equations)  # creates the 4x4 equation matrix
coefficients = np.array(coefficients)  # creates the 1x4 coefficients matrix

matrix_inverse = np.linalg.inv(matrix)  # finds the inverse of the matrix
solution = np.dot(matrix_inverse, coefficients)  # finds the solution with dot product
print(f'Solution: {solution}')
