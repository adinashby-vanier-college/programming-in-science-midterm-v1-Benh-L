import math

# Q1: Calculate the area of a circle
def area_of_circle(radius):
    area = math.pi * radius**2
    return round(area, 2)

# Q2: Hollow Right Triangle
def hollow_right_triangle(n):
    result = ""
    if n < 4:
        result = "The triangle height should be at least 4."
    else:
        for i in range (n + 1):
            for j in range (1, i + 1):
                if j == 1 or j == i or i == n:
                    result += "*"
                else:
                    result += " "
            result += "\n"
        
    return result.strip()
    



# Q3: Inverted Pyramid
def inverted_pyramid(n):
    if n < 3:
        result = "The pyramid height should be at least 3."
    else:
        row = n
        result = ""
        while row >= 1:
            line = (n - row) * " " + (2 * row - 1) * "*"
            result += line
            result += "\n"
            row -= 1
    return result.rstrip()


# ----------------------------------------------------------------
# print(area_of_circle(5))
# print()

#print(hollow_right_triangle(3))
#print()

print(hollow_right_triangle(4))
print()

# print(hollow_right_triangle(5))
# print()

# print(inverted_pyramid(3))
# print()

# print(inverted_pyramid(4))
# print()

print(inverted_pyramid(5))
print()