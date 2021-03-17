import random
import matplotlib.pyplot as plt
import math
import numpy as np

coord_queue = []
coords = {}

theta = np.linspace(-1 * math.pi / 2, math.pi / 2, num=180)
r = []
for index, angle in enumerate(theta):
	r.append(random.random() * 10 + 5)
	coords.update({angle: r[index]})

print(coords)

ax = plt.subplot(111, projection='polar')
ax.plot(theta, r)
ax.set_rmax(20)
plt.savefig('test.png')