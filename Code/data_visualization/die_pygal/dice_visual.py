import pygal
import matplotlib.pyplot as plt
from die import Die

die_1 = Die()
die_2 = Die(10)
die_3 = Die()

# for 前面是取值，后面是循环条件
results = [die_1.roll() + die_2.roll() +die_3.roll() for result in range(100000)]

frequencies = [results.count(value) 
               for value in range(3, die_1.num_sides + die_2.num_sides +die_3.num_sides +1)]

hist = pygal.Bar()
hist.title = "Results of rolling two D6 dice 1000 times."
hist.x_labels = [str(num) for num in range(3, die_1.num_sides + die_2.num_sides + die_3.num_sides +1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add('D6 + D10 + D6', frequencies)
hist.render_to_file('die\dice_visual.svg')

plt.plot(range(3,23), frequencies)
plt.show()