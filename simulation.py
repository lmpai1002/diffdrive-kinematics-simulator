import configs 
import inputs
import matplotlib.pyplot as plt
from model import body_velocity, euler_step




N = int(configs.T/configs.dt)
dt = configs.dt
L = configs.L

# Preallocation

x = [0.0] * (N+1)
y = [0.0] * (N+1)
theta = [0.0] * (N+1)
t = [0.0] * (N+1)


x[0] = configs.x0
y[0] = configs.y0
theta[0] = configs.theta0
t[0] = 0.0


for k in range(N) :

    tk = t[k]

    vL, vR = inputs.straight(tk)

    v, omega = body_velocity(vL, vR, L)

    x_new, y_new, theta_new = euler_step(x[k], y[k], theta[k], v, omega, dt)


    x[k+1] = x_new
    y[k+1] = y_new
    theta[k+1] = theta_new
    t[k+1] = t[k] + dt


# Testing
print(x[-1])
print(y[-1])
print(theta[-1])
    
# Plotting
plt.figure()
plt.plot(t, x, 'b-')
plt.xlabel("Time (s)")
plt.ylabel("X-Axis Distance (m)")
plt.title("X-Axis Trajection")
plt.grid(True)
plt.show(block=True)


plt.figure()
plt.plot(t, y, 'r-')
plt.xlabel("Time (s)")
plt.ylabel("Y-Axis Distance (m)")
plt.title("Y-Axis Trajection")
plt.grid(True)
plt.show(block=True)

plt.figure()
plt.plot(t, theta, 'g-')
plt.xlabel("Time (s)")
plt.ylabel("Angular Motion (rad)")
plt.title("Angular Trajection")
plt.grid(True)
plt.show(block=True)
