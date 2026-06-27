import numpy as n
import matplotlib.pyplot as p
from matplotlib.widgets import Slider

# As per question
dt=0.1    #time interval
t_max=500  #duration
h_target=5.0  #target height

time=n.arange(0,t_max+dt,dt) # to get different time instants

# Simulation Function
def simulate(kp,ki,kd):
    H=2.0
    I=0.0

    last_error=h_target-H

    water_level=n.zeros(len(time))
    u=n.zeros(len(time))

    water_level[0]=H

    for i in range(1,len(time)):
        t=time[i]
        error=h_target- H
        # PID terms
        P=error
        I+=error*dt
        D=(error-last_error)/dt
        u[i] = kp*P + ki*I + kd*D
        
        H=2+0.01*t+0.05*u[i]   # eqn given in question
        water_level[i]=H
        last_error=error

    return water_level,u

# Initial PID values just for trial
kp0=8
ki0=30
kd0=0.005

water_level,u=simulate(kp0, ki0, kd0)

# Plot-1
fig1, ax1 = p.subplots(figsize=(12,5))
fig1.subplots_adjust(bottom=0.25)

ax1.axhline(y=h_target,color='lightgreen',linestyle='--',linewidth=2,label='Setpoint (5 m)')
(line1,)=ax1.plot(time,water_level,color='red',linewidth=2,label='Water Level')

ax1.set_xlabel("Time (s)")
ax1.set_ylabel("Water Level (m)")
ax1.set_title("Water Level vs Time")
ax1.set_xlim(-5,100)
ax1.set_xticks(n.arange(0,501,50))
ax1.set_yticks(n.arange(1.5,6, 0.5))
ax1.grid(True, linestyle=':',alpha=0.7)
ax1.legend()

# Plot 2 : Pump Flow Rate
fig2, ax2=p.subplots(figsize=(12, 5))
(line2,)=ax2.plot(time,u,color='blue',linewidth=2.5,marker='o',markevery=500,label='Pump Flow Rate')

fill=ax2.fill_between(time,u,alpha=0.3)

ax2.set_xlabel("Time (s)")
ax2.set_ylabel("Pump Flow Rate")
ax2.set_title("Pump Flow Rate vs Time")
ax2.set_xlim(-10, 500)
ax2.set_xticks(n.arange(0,501,50))
ax2.grid(True, linestyle=':',alpha=0.7)

max_inflow=n.max(u)
max_outflow=abs(n.min(u))
flow_text=ax2.text(350,max_inflow * 0.4,f'Max Inflow by pump = {max_inflow:.2f}\n'f'Max Outflow by pump = {max_outflow:.2f}',bbox=dict(boxstyle='round',facecolor='white',alpha=0.8))
ax2.legend()

# Sliders 
ax_kp=fig1.add_axes([0.15, 0.14, 0.70, 0.03])
ax_ki=fig1.add_axes([0.15, 0.09, 0.70, 0.03])
ax_kd=fig1.add_axes([0.15, 0.04, 0.70, 0.03])

slider_kp=Slider(ax_kp,'Kp',0,20,valinit=kp0)
slider_ki=Slider(ax_ki,'Ki',0,50,valinit=ki0)
slider_kd=Slider(ax_kd,'Kd',0,5,valinit=kd0)


# Update Function
def update(val):
    global fill
    kp=slider_kp.val
    ki=slider_ki.val
    kd=slider_kd.val
    water_level,u=simulate(kp,ki,kd)
    line1.set_ydata(water_level)
    line2.set_ydata(u)

    max_inflow=n.max(u)
    max_outflow=abs(n.min(u))

    flow_text.set_text(f'Max Inflow by pump = {max_inflow:.2f}\n'f'Max Outflow by pump = {max_outflow:.2f}')

    flow_text.set_position((350,max_inflow * 0.4))

    fill.remove()
    fill=ax2.fill_between(time,u,alpha=0.3)

    fig1.canvas.draw_idle()
    fig2.canvas.draw_idle()

slider_kp.on_changed(update)
slider_ki.on_changed(update)
slider_kd.on_changed(update)

p.show()