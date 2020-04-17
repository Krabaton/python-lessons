import pygal
from cube import Die

die = Die()

results = []

for roll_num in range(100):
    result = die.roll()
    results.append(result)

frequencies =[]

for val in range(1, die.num_sides+1):
    frequency = results.count(val)
    frequencies.append(frequency)

hist = pygal.Bar()
hist.title = 'Результат бросания кубика'
hist.x_labels = [1, 2, 3, 4, 5, 6]
hist.x_title = 'Результат'
hist.y_title = 'Частота'

hist.add('D6', frequencies)
hist.render_to_file('visual.svg')