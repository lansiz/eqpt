import numpy as np
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser(description='plot SVG and angle data')
parser.add_argument(
    '--from', dest='from_', default=0,
    help='the beginnig iteration to plot (Default: 0)')
parser.add_argument(
    '--to', dest='to', default=10 ** 8,
    help='the ending iteration to plot (Default: 10 ** 8)')
args = parser.parse_args()
since = int(args.from_)
untils = int(args.to)

# angle_row = np.log(np.load('angle_row.npy'))
# angle_col = np.log(np.load('angle_col.npy'))
# angle_row = np.load('angle_row.npy')
# angle_col = np.load('angle_col.npy')
SVG_row = np.log(np.load('SVG_row.npy'))
SVG_col = np.log(np.load('SVG_col.npy'))

print('SVG row:', SVG_row.max(), SVG_row.min())
print('SVG col:', SVG_col.max(), SVG_col.min())

scale = 100

# since = -5 * 10 ** 4
print('print data from iteration %s to %s' % (since, untils))
plt.plot(SVG_row[since:untils])
plt.plot(SVG_col[since:untils])
# plt.plot(angle_row[since:untils] * scale, linestyle=':')
# plt.plot(angle_col[since:untils] * scale, linestyle=':')
plt.grid(True)
plt.show()

# plt.savefig('./svg_angle.png', dpi=120)
