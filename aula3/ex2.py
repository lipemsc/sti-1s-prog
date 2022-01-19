from math import sqrt

point1 = {
    "x": 1,
    "y": 1
}
point2 = {
    "x": 10,
    "y": 10
}

distance = sqrt((point2["x"] - point1["x"]) ** 2 + (point2["y"] - point1["y"]) ** 2)
print(distance)
