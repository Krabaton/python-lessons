import matplotlib.pyplot as plt

from random_point import RandomPoint

rs = RandomPoint(1000, 1000, 25000)

rs.finding()
plt.figure(figsize=(15, 10))
point_numbers = list(range(rs.num_points))
plt.scatter(rs.x_val, rs.y_val, s=1)
plt.show()