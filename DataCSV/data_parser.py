import csv
import numpy as np
from matplotlib import pyplot as plt
from datetime import datetime
filename = {'2016_may_final.csv': 6, '2016_dec_final.csv': 7,  '2017_jun_final.csv': 6}
median = []
for item in filename:
    print(filename[item])
    with open(item, encoding='utf8') as f:
        reader = csv.reader(f)
        header_row = next(reader)
        zp = []
        sum = 0
        for row in reader:
            try:
                current_zp = int(row[filename[item]])
                sum += current_zp
            except ValueError:
                print(current_zp, 'missing data')
            else:
                zp.append(current_zp)
        f.close()
    median.append(sum / len(zp))

print(median)
ind = np.arange(len(median))
print(ind)
fig = plt.figure(dpi=128, figsize=(12, 6))
plt.bar(['may-2016', 'dec-2016', 'jun-2017'], median, 0.5)
plt.show()