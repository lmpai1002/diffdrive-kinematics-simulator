import math 

def body_velocity(vL, vR, L):
    
    if L <= 0 :

        raise ValueError("Vehicle separation must be greater than 0!")

    v = (vR+vL)/2

    omega = (vR-vL)/L
 

    return v, omega




def euler_step(x, y, theta, v, omega, dt):

    if dt <= 0 :
        raise ValueError("Time difference must be greater than 0!")

    x_new = x + v*math.cos(theta)*dt

    y_new = y + v*math.sin(theta)*dt

    theta_new = theta + omega*dt



    return x_new, y_new, theta_new

