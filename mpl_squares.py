import matplotlib.pyplot as plt

x_values = list(range(101))
y_values = [x**2 for x in x_values]
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolors='none', s=10)
# plt.show()
plt.savefig('plot.png', bbox_inches='tight')