import numpy as np

u = np.random.normal(loc=1, size=2)
v = np.random.normal(loc=-3, size=2)

print("%8s %8s %8s %8s" % ('step', 'angle_old', 'angle_new', 'angle_dlt'))
for i in np.linspace(0, 2, 40):
    u_new = u + i * v
    u_len = np.sqrt(np.sum(u * u))
    u_new_len = np.sqrt(np.sum(u_new * u_new))
    v_len = np.sqrt(np.sum(v * v))
    angle = np.sum(u * v) / u_len / v_len
    angle_new = np.sum(u_new * v) / u_new_len / v_len
    angle_delta = angle_new - angle
    print("%8s %8s %8s %8s" % (
        np.round(i, 2),
        np.round(angle, 4),
        np.round(angle_new, 4),
        np.round(angle_delta, 4)))
