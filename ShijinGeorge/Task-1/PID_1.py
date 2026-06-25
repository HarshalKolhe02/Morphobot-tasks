import numpy as n
import matplotlib.pyplot as p
from matplotlib.widgets import Slider

# as per question
dt=0.1
t_max=500
t_target=24.0
time=n.arange(0,t_max+dt,dt)  # to get different time instants

def simulate(kp, ki, kd):
    T=35.0
    I=0.0
    last_error=t_target - T

    temp=n.zeros(len(time))
    cooling_power=n.zeros(len(time))

    temp[0]=T

    for i in range(1,len(time)):
        t=time[i]
        error=t_target-T
        P=error   #Proportional
        I+=error*dt    #Integral
        D=(error-last_error)/dt  #Derivative

        u=kp*P+ki*I+kd*D

        # Since it is cooling rate it can't be negative
        cooling=max(0,-u)
        T=35+0.02*t-0.05*cooling
        temp[i]=T
        cooling_power[i]=cooling
        last_error=error

    return temp,cooling_power

# Initial PID values(just a trial and error)
kp0=5
ki0=10
kd0=0.01
temp,cooling_power=simulate(kp0,ki0,kd0)
fig1,ax1 = p.subplots(figsize=(12,5))
fig2,ax2 = p.subplots(figsize=(12,5))

fig1.subplots_adjust(bottom=0.25)

# Plot 1: Temperature
ax1.axhline(y=t_target,color='lightgreen',linestyle='--',linewidth=2,label='Setpoint (24 deg C)')
(line1,)=ax1.plot(time,temp,color='red',linewidth=2,label='Room Temperature')
ax1.set_xlabel("Time (s)")
ax1.set_ylabel("Temperature (deg C)")
ax1.set_title("Room Temperature vs Time")
ax1.set_xlim(-50, 500)
ax1.set_xticks(n.arange(0, 501, 50))
ax1.grid(True, linestyle=':', alpha=0.7)
ax1.legend()

# Plot 2: Cooling Power
(line2,)=ax2.plot(time,cooling_power,color='blue',linewidth=2,label='Cooling Power')
fill=ax2.fill_between(time,cooling_power,alpha=0.3)
ax2.set_xlabel("Time (s)")
ax2.set_ylabel("Cooling Power")
ax2.set_title("Cooling Power vs Time")
ax2.set_xlim(-50,500)
ax2.set_xticks(n.arange(0,501,50))
ax2.grid(True, linestyle=':', alpha=0.7)
max_cooling= n.max(cooling_power)
cooling_text=ax2.text(350,max_cooling * 0.5,f'Max Cooling Power = {max_cooling:.2f}',bbox=dict(boxstyle='round',facecolor='white',alpha=0.8))
ax2.legend()

# Added Sliders for better tuning

ax_kp = fig1.add_axes([0.15,0.14,0.70,0.03])
ax_ki = fig1.add_axes([0.15,0.09,0.70,0.03])
ax_kd = fig1.add_axes([0.15,0.04,0.70,0.03])

slider_kp=Slider(ax_kp, 'Kp', 0, 20, valinit=kp0)
slider_ki=Slider(ax_ki, 'Ki', 0, 30, valinit=ki0)
slider_kd=Slider(ax_kd, 'Kd', 0, 5, valinit=kd0)

# Update Function
def update(val):
    global fill
    kp=slider_kp.val
    ki=slider_ki.val
    kd=slider_kd.val
    temp,cooling_power=simulate(kp,ki,kd)
    line1.set_ydata(temp)
    line2.set_ydata(cooling_power)
    fill.remove()
    fill=ax2.fill_between(time,cooling_power,alpha=0.3)
    fig1.canvas.draw_idle()
    fig2.canvas.draw_idle()
    max_cooling = n.max(cooling_power)
    cooling_text.set_text(f'Max Cooling Power = {max_cooling:.2f}')
    cooling_text.set_position((350, max_cooling * 0.5))

slider_kp.on_changed(update)
slider_ki.on_changed(update)
slider_kd.on_changed(update)

p.show()