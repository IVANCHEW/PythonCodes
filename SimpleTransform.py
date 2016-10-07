import numpy as np
import math

p = np.zeros((3))

p[0] = -0.35
p[1] = -0.25
PI = math.pi

deg1 = -0.7854
deg2 = 0.8854

r = np.zeros((2,3,3))

r[0][0][0] = 1
r[0][1][1] = math.cos(deg1)
r[0][1][2] = -math.sin(deg1)
r[0][2][1] = math.sin(deg1)
r[0][2][2] = math.cos(deg1)

r[1][1][1] = 1
r[1][0][0] = math.cos(deg2)
r[1][0][2] = math.sin(deg2)
r[1][2][0] = -math.sin(deg2)
r[1][2][2] = math.cos(deg2)

result = np.dot(r[1],r[0])
position = np.dot(result, p)

print position
