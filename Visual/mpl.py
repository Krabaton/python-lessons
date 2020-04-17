import matplotlib.pyplot as plt
#  pip --user matplotlib

x_val = [1, 2, 3, 4, 5]
y_val = [1, 4, 9, 16, 25]

plt.plot(x_val, y_val, linewidth=2)
plt.scatter(x_val, y_val, s=10)

plt.title('x = y^2', fontsize=24)
plt.xlabel('Value', fontsize=12)
plt.ylabel('Square of value', fontsize=12)
plt.tick_params(axis='both', labelsize=10)

plt.show()