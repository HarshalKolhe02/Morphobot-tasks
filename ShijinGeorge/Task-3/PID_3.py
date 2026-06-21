import numpy as n
import matplotlib.pyplot as p

dt=0.1                 # Time step
t_end=200              # Simulation duration
time=n.arange(0,t_end+dt,dt)

h_set=10.0             # Setpoint (m)

Kp=4    #proportional gain
Ki=15   #integral gain
Kd=0.005    #derivative gain

h=n.zeros(len(time))      # Altitude
u=n.zeros(len(time))      # Throttle
error=n.zeros(len(time))

h[0]=2.0    # Initial altitude

integral=0
error_last=h_set-h[0]


for i in range(1,len(time)):
    error[i]=h_set-h[i-1]    # Error
    integral+=error[i]*dt    #integral term
    derivative =(error[i]-error_last)/dt       #derivative term
    
    u[i]=Kp*error[i]+ Ki*integral+Kd*derivative    # PID output 
    h[i]=2+0.03*u[i]-0.002*time[i]   #height equation
    error_last=error[i]

final_height=h[-1]
final_error=h_set-final_height
max_throttle=max(u)

#plot-1
p.figure(figsize=(12,5)) # figure size of plot 1
p.plot(time,h,linewidth=2,label="Altitude h(t)")
p.axhline(y=h_set,color='red',linestyle='--',linewidth=2,label='Setpoint = 10 m')
p.xlabel("Time (s)")
p.ylabel("Altitude (m)")
p.title("PID Control of Drone Altitude")
p.grid(True)
p.legend()
p.text(130,max(h) * 0.7,f'Kp = {Kp}\n'f'Ki = {Ki}\n'f'Kd = {Kd}\n\n'f'Final Height = {final_height:.2f} m\n'f'Final Error = {final_error:.2f} m',bbox=dict(boxstyle='round',facecolor='white',alpha=0.8))
p.tight_layout()
p.show()


#plot-2
p.figure(figsize=(12, 5)) # figure size of plot 2
p.plot(time,u,linewidth=2,color='blue',label='Throttle')
p.plot(time,u,color='blue',linewidth=0.5,marker='o',markevery=500)     # Markers at intervals at 500
p.fill_between(time,u,alpha=0.3)       # Area shaded below the curve
p.xlabel("Time (s)")
p.ylabel("Throttle u(t)")
p.title("RC Throttle vs Time")
p.grid(True)
p.legend()
p.text(130,max_throttle * 0.5,f'Kp = {Kp}\n'f'Ki = {Ki}\n'f'Kd = {Kd}\n\n'f'Max Throttle = {max_throttle:.2f}',bbox=dict(boxstyle='round',facecolor='white',alpha=0.8))
p.tight_layout()
p.show()
