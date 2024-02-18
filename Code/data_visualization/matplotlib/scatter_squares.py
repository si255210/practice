import matplotlib.pyplot as plt
x_values = list(range(1, 6))
print(x_values)
y_values = [x**3 for x in x_values]
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolors='none', s=100)
plt.title('Square Number', fontsize= 24)
plt.xlabel('Value', fontsize=24)
plt.ylabel('Square of Value')
plt.tick_params(axis='both', which='major',labelsize=8)
plt.savefig('squares_plot.png',bbox_inches='tight')