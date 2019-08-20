import numpy as np
# import matplotlib.pyplot as plt
# import argparse

angle = np.load('angle_col.npy')
angle_shift = angle[1:]
angle_new = np.append(angle_shift, 1)
ll = (angle_new - angle) < 0
print('angle development:')
print(np.nonzero(ll)[0].shape[0] / 1.0 / angle.shape[0])
print(np.nonzero(ll))

svg = np.load('SVG_col.npy')
svg_shift = svg[1:]
svg_new = np.append(svg_shift, 0)
ll = (svg_new - svg) > 0
print('SVG development:')
print(np.nonzero(ll)[0].shape[0] / 1.0 / angle.shape[0])
print(np.nonzero(ll))
