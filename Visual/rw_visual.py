import matplotlib.pyplot as plt
from random_walk import RandomWalk

rw = RandomWalk(15000)
rw.fill_walk()
point_numbers = list(range(rw.num_points))
plt.figure(figsize=(15, 9.6))
plt.scatter(rw.x_val, rw.y_val, c=point_numbers, cmap=plt.cm.Blues, s=1)
plt.scatter(0, 0, c='#D35400', s=155)
plt.scatter(rw.x_val[-1], rw.y_val[-1], c='#2ECC71', s=150)
plt.show()