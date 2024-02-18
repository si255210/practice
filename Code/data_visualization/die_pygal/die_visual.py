from die import Die
import pygal

die = Die(8)

results = [die.roll() for result in range(int(input('roll how many times?')))]

frequencies = []
for num in range(1,die.num_sides+1):
    frequencies.append(results.count(num))

hist = pygal.Bar()
hist.title = "Results of rolling one D6 1000 times."
hist.x_labels = ['1', '2', '3', '4', '5', '6','7','8']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add('D8',frequencies)
hist.render_to_file('die\die_visual.svg')