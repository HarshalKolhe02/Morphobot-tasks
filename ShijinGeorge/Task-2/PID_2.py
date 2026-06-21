import numpy as n
import matplotlib.pyplot as p

# As per question
dt=0.1
t_max=500
h_target=5.0  # target water level 
H=2.0  #initial water level at t=0

#Tuned PID gains by trial and error
kp=8
ki=30
kd=0.005

I=0.0
last_error= h_target - H
time=n.arange(0, t_max + dt, dt) #to get time intervals 
water_level=n.zeros(len(time))  #initiating with zeroes
u=n.zeros(len(time))

water_level[0]=H

for i in range(1, len(time)):
    t=time[i]
    error=h_target- H
    # PID terms
    P=error
    I+=error*dt
    D= (error-last_error)/dt
    u[i]=kp*P+ki*I+kd*D
    # Water tank model
    H = 2+0.01*t+0.05*u[i]
    water_level[i]=H
    last_error=error

# Values to display in graph
max_height=n.max(water_level)
final_error=h_target - water_level[-1]

max_inflow=n.max(u)
max_outflow=abs(n.min(u))  #took only magnitude since it is negative

# Plot-1
p.figure(figsize=(12, 5))
p.plot(time,water_level,color='red',linewidth=2.5,label='Water Level')
p.axhline(y=h_target,color='black',linestyle='--',linewidth=2,label='Setpoint (5 m)')
p.xlabel("Time (sec)")
p.ylabel("Water Level (metres)")
p.title("Water Level vs Time")
p.xlim(0, 500)
p.xticks(n.arange(0, 501, 50))
p.legend()
p.grid(True, linestyle=':', alpha=0.7)
p.text(350,max_height * 0.75,f'Kp = {kp}\nKi = {ki}\nKd = {kd}\n\n'f'Max Height = {max_height:.2f} m\n'f'Final Error = {final_error:.2f} m',bbox=dict(boxstyle='round',facecolor='white',alpha=0.8))
p.tight_layout()

#Plot-2
p.figure(figsize=(12, 5))
p.plot(time,u,color='blue',linewidth=2.5,label='Pump Flow Rate')
p.plot(time,u,color='blue',linewidth=0.5,marker='o',markevery=500)
p.fill_between(time, u, alpha=0.3)
p.xlabel("Time (s)")
p.ylabel("Pump Flow Rate")
p.title("Pump Flow Rate vs Time")
p.xlim(0, 500)
p.xticks(n.arange(0, 501, 50))
p.legend()
p.grid(True, linestyle=':', alpha=0.7)
#to print it in a box
p.text(350,n.max(u) * 0.4,f'Kp = {kp}\nKi = {ki}\nKd = {kd}\n\n'f'Max Inflow by pump = {max_inflow:.2f}\n'f'Max Outflow by pump = {max_outflow:.2f}',bbox=dict(boxstyle='round',facecolor='white',alpha=0.8))
p.tight_layout()
p.show()