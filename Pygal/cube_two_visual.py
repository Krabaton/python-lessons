import pygal
from cube import Die

die_1 = Die()
die_2 = Die()

results = []

for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

frequencies = []
max_result = die_1.num_sides + die_2.num_sides

for val in range(2, max_result + 1):
    frequency = results.count(val)
    frequencies.append(frequency)

hist = pygal.Bar()

hist.title = 'Результат бросания двух кубиков 1000 раз'
hist.x_labels = list(range(2, max_result + 1))
hist.x_title = 'Результат'
hist.y_title = 'Частота'

hist.add('D6 + D6', frequencies)
hist.render_to_file('two_visual.svg')