#!/usr/bin/python3

def pascal_triangle(n):
    
    triangle = []
    if n <= 0:
        return triangle
    triangle = [[1]]  # Initialize the triangle with the first row
    for i in range(1, n):
	# Calculate the value based on the two values above it
        temp = [1]
        for j in range(len(triangle[i - 1]) - 1):
            curr = triangle[i - 1]
            temp.append(triangle[i - 1][j] + triangle[i - 1][j + 1])
        temp.append(1)
        triangle.append(temp)
    return triangle
