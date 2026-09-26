from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time
import numpy as np
import random

m1, m2, m3 = [float(random.random()), float(random.random()), float(random.random())]


init_pos_1 = [float(random.random()), float(random.random()), float(random.random())]
init_pos_2 = [float(random.random()), float(random.random()), float(random.random())]
init_pos_3 = [float(random.random()), float(random.random()), float(random.random())]

init_v_1 = [float(random.random()), float(random.random()), float(random.random())]
init_v_2 = [float(random.random()), float(random.random()), float(random.random())]
init_v_3 = [float(random.random()), float(random.random()), float(random.random())]

init_cond = np.array([
    init_pos_1, init_pos_2, init_pos_3,
    init_v_1, init_v_2, init_v_3
]).ravel()

def ODE_system(t, s, m1, m2, m3):
    p1, p2, p3 = s[0: 3], s[3:6], s[6:9]
    dp1_dt, dp2_dt, dp3_dt = s[9:12], s[12:15], s[15:18]
    
    f1, f2, f3 = dp1_dt, dp2_dt, dp3_dt

    df1_dt = m3*(p3 - p1)/np.linalg.norm(p3 - p1)**3 + m2*(p2 - p1)/np.linalg.norm(p2 - p1)**3
    df2_dt = m1*(p1 - p2)/np.linalg.norm(p1 - p2)**3 + m3*(p3 - p2)/np.linalg.norm(p3 - p2)**3
    df3_dt = m1*(p1 - p3)/np.linalg.norm(p1 - p3)**3 + m2*(p2 - p3)/np.linalg.norm(p2 - p3)**3

    return np.array([f1, f2, f3, df1_dt, df2_dt, df3_dt]).ravel()

start_time, end_time = 0, 60
time_points = np.linspace(start_time, end_time, 3000)

t1 = time.time()
solution = solve_ivp(
    fun=ODE_system,
    args=(m1, m2, m3),
    y0=init_cond,
    t_span=(start_time, end_time),
    t_eval=time_points
)
t2 = time.time()
print(f"{t2-t1:.3f} [s]")

time_solution = solution.t
p1_sol = solution.y[0:3]

p2_sol = solution.y[3:6]

p3_sol = solution.y[6:9]

fig, ax = plt.subplots(subplot_kw={"projection":"3d"})

p1_plt, = ax.plot(p1_sol[0], p1_sol[1], p1_sol[2], "yellow", label=f"A", linewidth=1)
p2_plt, = ax.plot(p2_sol[0], p2_sol[1], p2_sol[2], "blue", label=f"B", linewidth=1)
p3_plt, = ax.plot(p3_sol[0], p3_sol[1], p3_sol[2], "grey", label=f"C", linewidth=1)

p1_dot, = ax.plot(p1_sol[0, -1], p1_sol[1, -1], p1_sol[2, -1], "o", color="yellow", markersize=8)
p2_dot, = ax.plot(p2_sol[0, -1], p2_sol[1, -1], p2_sol[2, -1], "o", color="blue", markersize=8)
p3_dot, = ax.plot(p3_sol[0, -1], p3_sol[1, -1], p3_sol[2, -1], "o", color="grey", markersize=8)


# ax.set_title("The 3-Body Problem")
# ax.set_xlabel("x")
# ax.set_ylabel("y")
# ax.set_zlabel("z")

# ax.set_facecolor('black')
# fig.set_facecolor('black')
# p1_plt.set_visible(False)
# p2_plt.set_visible(False)
# p3_plt.set_visible(False)

# plt.grid()
# plt.legend()

def update(frame):

    p1x_current = p1_sol[0, 0:frame+1]
    p1y_current = p1_sol[1, 0:frame+1]
    p1z_current = p1_sol[2, 0:frame+1]

    p1_plt.set_data(p1x_current, p1y_current)
    p1_plt.set_3d_properties(p1z_current)

    p1_dot.set_data([p1x_current[-1]], [p1y_current[-1]])
    p1_dot.set_3d_properties([p1z_current[-1]])



    p2x_current = p2_sol[0, 0:frame+1]
    p2y_current = p2_sol[1, 0:frame+1]
    p2z_current = p2_sol[2, 0:frame+1]

    p2_plt.set_data(p2x_current, p2y_current)
    p2_plt.set_3d_properties(p2z_current)

    p2_dot.set_data([p2x_current[-1]], [p2y_current[-1]])
    p2_dot.set_3d_properties([p2z_current[-1]])



    p3x_current = p3_sol[0, 0:frame+1]
    p3y_current = p3_sol[1, 0:frame+1]
    p3z_current = p3_sol[2, 0:frame+1]

    p3_plt.set_data(p3x_current, p3y_current)
    p3_plt.set_3d_properties(p3z_current)

    p3_dot.set_data([p3x_current[-1]], [p3y_current[-1]])
    p3_dot.set_3d_properties([p3z_current[-1]])



    return p1_plt, p1_dot, p2_plt, p2_dot, p3_plt, p3_dot

animation = FuncAnimation(fig, update, frames=range(0, len(time_points), 1), interval=1, blit=True)

plt.show()