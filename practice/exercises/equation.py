import math


def equation_solution(a,b,c):
    delta = b ** 2 - 4 *  (a * c)
    if delta > 0:
        solution_one = (-b + math.sqrt(b**2 - 4 * a * c)) / (2 * a)
        solution_two = (-b - math.sqrt(b**2 - 4 * a * c)) / (2 * a)
        print("Solution 1: " ,solution_one)
        print("Solution 2: ", solution_two)

    elif delta == 0:
        solution = -b / 2* a
        print("Solution: ",solution)
    else:
        print("There is no solution")



