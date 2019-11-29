# Rondom-walk distribution
# Jelmer Mulder
import time
start = time.time()
import random
import math
import matplotlib.pyplot as plt
import numpy as np
N = 100000
def create_empty_list(N):
    xpos = []
    ypos = []
    for i in range(N):
        xpos.append(0)
        ypos.append(0)
    return xpos, ypos
xpos, ypos = create_empty_list(N)

steps = 0
def points_gen(steps, N):
    while steps < 100:
        for i in range(N):
            xpos[i-1] += math.cos(random.random()*2*math.pi)
            ypos[i-1] += math.sin(random.random()*2*math.pi)
        steps += 1
    return xpos, ypos
xpos, ypos = points_gen(steps, N)
print(time.time() - start)
#fig1 = plt.figure()
plt.plot(xpos, ypos, 'bo', markersize=1)
plt.xlim(-40, 40)
plt.ylim(-40, 40)
plt.show()

