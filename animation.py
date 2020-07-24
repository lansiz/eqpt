# based on the code example in matplotlib.org
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import utils


def update_lines(num, data_lines, lines, text_iters, text_vgs):
    vgs_str = ''
    for line, data in zip(lines, data_lines):  # per person
        str_data, vgs_data = data
        # NOTE: there is no .set_data() for 3 dim data...
        line.set_data(str_data[0:2, :num])
        line.set_3d_properties(str_data[2, :num])
        text_iters.set_text('iterations: ' + str(num))
        vgs_str += ' ' + str(vgs_data[num])
    text_vgs.set_text('regret: ' + vgs_str)
    return lines


# Attaching 3D axis to the figure
fig = plt.figure()
ax = fig.add_subplot(projection="3d")

# load the pickle file
data = utils.read_pickle('./animation_data.pkl')
data_size = data[0][0].shape[1]

# Creating person * 2 lines with only inital dots
# NOTE: Can't pass empty arrays into 3d version of plot()
colors = ['blue', 'green', 'red', 'purple', 'pink', 'gray', 'brown', 'cyan', 'olive', 'orange']
colors_size = len(colors)
lines = []
i = 0
for str_a, vgs_a in data:
    color = colors[i % colors_size]
    lines.append(ax.plot(str_a[0, 0: 1], str_a[1, 0: 1], str_a[2, 0: 1], color)[0])
    text_iters = ax.text2D(0.0, 0.97, '', transform=ax.transAxes)
    text_vgs = ax.text2D(0.0, 0.94, '', transform=ax.transAxes)
    i += 1


# Setting the axes properties
ax.set_xlim3d([0.0, 1.0])
ax.set_xlabel('pure 1')
ax.set_ylim3d([0.0, 1.0])
ax.set_ylabel('pure 2')
ax.set_zlim3d([0.0, 1.0])
ax.set_zlabel('pure 3')
ax.set_title('Geometrical Regret Matching')

# plot the probability simplex
ax.plot((1, 0), (0, 1), (0, 0), linestyle='dotted', color='grey')
ax.plot((1, 0), (0, 0), (0, 1), linestyle='dotted', color='grey')
ax.plot((0, 0), (1, 0), (0, 1), linestyle='dotted', color='grey')

# Creating the Animation object
line_ani = animation.FuncAnimation(
    fig, update_lines, data_size, fargs=(data, lines, text_iters, text_vgs), interval=1)

plt.show()
# line_ani.save('./animation.mp4')
