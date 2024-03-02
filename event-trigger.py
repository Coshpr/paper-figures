# data from https://allisonhorst.github.io/palmerpenguins/
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

species = ("10%", "30%", "50%")
penguin_means = {
    'Random1': (10.35, 12.43, 12.13),
    'Random2': (12.79, 15.83, 17.00),
    'Top1': (42.03, 63.22, 65.33),
    'Top3': (59.23, 73.04,72.88),
}

matplotlib.rcParams['figure.figsize'] = (6, 4)
matplotlib.rcParams['figure.dpi'] = 300

x = np.arange(len(species))  # the label locations
width = 0.15  # the width of the bars
multiplier = 0

fig, ax = plt.subplots(layout='constrained')

for attribute, measurement in penguin_means.items():
    offset = width * multiplier
    rects = ax.bar(x + offset, measurement, width, label=attribute)
    # ax.bar_label(rects, padding=3)
    multiplier += 1

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('F1 score(%)')
# ax.set_title('Penguin attributes by species')
ax.set_xticks(x + width, species)
ax.legend(loc='upper left', ncols=4)
ax.set_ylim(0, 100)

# plt.show()
plt.savefig("event-trigger.pdf")
