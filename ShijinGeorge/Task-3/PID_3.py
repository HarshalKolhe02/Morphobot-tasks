import numpy as n
import matplotlib.pyplot as p
from matplotlib.widgets import Slider

dt = 0.1                 # Time step
t_end = 200              # Simulation duration
time = n.arange(0, t_end + dt, dt)

h_set = 10.0             # Setpoint (m)

def simulate(Kp, Ki, Kd):
    h = n.zeros(len(time))      # Altitude
    u = n.zeros(len(time))      # Throttle
    error = n.zeros(len(time))
    h[0] = 2.0
    integral = 0
    error_last = h_set - h[0]

    for i in range(1, len(time)):
        error[i] = h_set - h[i - 1]
        integral += error[i] * dt
        derivative = (error[i] - error_last) / dt
        u[i] = Kp * error[i] + Ki * integral + Kd * derivative
        h[i] = 2 + 0.03 * u[i] - 0.002 * time[i]
        error_last = error[i]
    return h, u

# Initial PID values
Kp0 = 4
Ki0 = 15
Kd0 = 0.005

h, u = simulate(Kp0, Ki0, Kd0)

final_height = h[-1]
final_error = h_set - final_height
max_throttle = max(u)

#Plot-1
fig1, ax1 = p.subplots(figsize=(12, 5))
fig1.subplots_adjust(bottom=0.25)
ax1.axhline(y=h_set,color='red',linestyle='--',linewidth=2,label='Setpoint = 10 m')
(line1,) = ax1.plot(time,h,linewidth=2,label="Altitude h(t)")
ax1.set_xlabel("Time (s)")
ax1.set_ylabel("Altitude (m)")
ax1.set_title("PID Control of Drone Altitude")
ax1.grid(True)
ax1.legend()

#Plot-2
fig2, ax2 = p.subplots(figsize=(12, 5))
(line2,) = ax2.plot(time,u,linewidth=2,color='blue',label='Throttle')
marker_line, = ax2.plot(time,u,color='blue',linewidth=0.5,marker='o',markevery=500)
fill = ax2.fill_between(time, u, alpha=0.3)
ax2.set_xlabel("Time (s)")
ax2.set_ylabel("Throttle u(t)")
ax2.set_title("RC Throttle vs Time")
ax2.grid(True)
ax2.legend()
throttle_text = ax2.text(130,max_throttle * 0.5,f'Max Throttle = {max_throttle:.2f}',bbox=dict(boxstyle='round',facecolor='white',alpha=0.8))

# Sliders 
ax_kp = fig1.add_axes([0.15, 0.14, 0.70, 0.03])
ax_ki = fig1.add_axes([0.15, 0.09, 0.70, 0.03])
ax_kd = fig1.add_axes([0.15, 0.04, 0.70, 0.03])

slider_kp = Slider(ax_kp, 'Kp', 0, 20, valinit=Kp0)
slider_ki = Slider(ax_ki, 'Ki', 0, 30, valinit=Ki0)
slider_kd = Slider(ax_kd, 'Kd', 0, 5, valinit=Kd0)

# Update 
def update(val):
    global fill
    Kp = slider_kp.val
    Ki = slider_ki.val
    Kd = slider_kd.val
    h, u = simulate(Kp, Ki, Kd)
    line1.set_ydata(h)
    line2.set_ydata(u)
    marker_line.set_ydata(u)

    final_height = h[-1]
    final_error = h_set - final_height
    max_throttle = max(u)

    throttle_text.set_text(f'Max Throttle = {max_throttle:.2f}')
    throttle_text.set_position((130, max_throttle * 0.5))
    fill.remove()
    fill = ax2.fill_between(time, u, alpha=0.3)
    fig1.canvas.draw_idle()
    fig2.canvas.draw_idle()

slider_kp.on_changed(update)
slider_ki.on_changed(update)
slider_kd.on_changed(update)

p.show()
