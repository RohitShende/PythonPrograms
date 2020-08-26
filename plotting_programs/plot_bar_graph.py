import numpy as np
import matplotlib.pyplot as plt

csv_file = open('bar_plot.csv')
lines = csv_file.readlines()

headings = lines.pop(0).strip().split(',')
print('Headings are - ', headings)
number_of_bars = len(headings) - 1
print('Plotting {} bars'.format(number_of_bars))

# data to plot
n_groups = len(lines)
print('There is data for {} groups'.format(n_groups))

data = []
for i in range(number_of_bars + 1):
    data.append([])

for line in lines:
    line_data = line.strip().split(',')
    for j in range(len(line_data)):
        if j == 0:
            data[j].append(line_data[j])
        else:
            data[j].append(int(line_data[j]))

# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.35
opacity = 0.8

rectangles = []
colours = ['b', 'r', 'g']

for i in range(number_of_bars):
    print(headings[i+1])
    print(tuple(data[i + 1]))
    print(index)
    print(colours[i])
    if i == 0:
        rect1 = plt.bar(index, tuple(data[i + 1]), bar_width, alpha=opacity, color=colours[i], label=headings[i+1])
    else:
        rect1 = plt.bar(index+bar_width, tuple(data[i + 1]), bar_width, alpha=opacity, color=colours[i], label=headings[i + 1])
print(rectangles)

plt.xlabel('Institutions')
plt.ylabel('Confidence')
plt.title('Confidence In Institutions')
plt.xticks(index + bar_width, tuple(data[0]))
plt.legend()

plt.tight_layout()
plt.show()
