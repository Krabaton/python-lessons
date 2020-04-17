import csv
from matplotlib import pyplot as plt
from datetime import datetime
filename = 'death_valley_2014.csv'

with open(filename, encoding='utf-8') as f:
    reader = csv.reader(f)
    header_row = next(reader)
    highs, lows, dates = [], [], []

    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
    f.close()

# Нанесение данных
fig = plt.figure(dpi=128, figsize=(12, 6))
plt.plot(dates, highs, c="red", alpha=0.7)
plt.plot(dates, lows, c="blue", alpha=0.7)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.3)

# Форматирование диаграммы
plt.title('Температуры в Долине смерти в 2014', fontsize=18)
plt.xlabel('days', fontsize=16)
plt.ylabel('Temp (F)', fontsize=16)
plt.tick_params(axis='both', labelsize=14)

plt.show()