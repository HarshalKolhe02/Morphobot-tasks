import numpy as n
import matplotlib.pyplot as p
#as per question
dt=0.1  #time interval
t_max=500
t_target=24.0  #as we have to maintain 24 deg celsius as room temperature

T=35.0 #temp at t=0

#after testing many values of kp,ki,kd values; got this as optimal solution
kp=5            #prop gain
ki=19            #integral gain
kd=0.01         #derivative gain

I=0.0
last_error=t_target-T

time=n.arange(0, t_max + dt, dt)        # will generate 0-500 sec at an interval of 0.1 sec
temp=n.zeros(len(time))                 # initialising arrays
cooling_power=n.zeros(len(time))

temp[0]=T

for i in range(1, len(time)):
    t = time[i] 
    error=t_target-T
    P=error
    I+=error*dt
    I = max(-100, min(100, I)) # to prevent integral windup by integral clamping
    D=(error-last_error)/dt
    u= kp*P+ki*I+kd*D

    #Since it is cooling rate it can't be negative as AC cannot produce heat
    cooling= max(0,-u)   # as error is negative at T>24, as in qn it mentioned to take error as t_target - T; so we have to take u positive 
    T=35+0.02*t-0.05*cooling

    temp[i]=T
    cooling_power[i]=cooling
    last_error=error

final_temp=temp[-1]
final_error=t_target-final_temp
max_cooling=max(cooling_power)

#Plot-1
p.figure(figsize=(12, 5))
p.plot(time, temp,color='red',linewidth=2.5,label='Room Temperature')
p.axhline(y=t_target,color='black',linestyle='--',linewidth=2,label='Setpoint (24 deg C)')
p.xlabel("Time (s)")
p.ylabel("Temperature (deg C)")
p.title("Room Temperature vs Time")
p.xlim(0,500)   #limits of time axis
p.xticks(n.arange(0,501,50)) #to plot an interval of 50s on x axis
p.legend()
p.grid(True,linestyle=':',alpha=0.7)
p.text(350,30,f'Kp = {kp}\n'f'Ki = {ki}\n'f'Kd = {kd}\n\n'f'Final Temp = {final_temp:.2f} °C\n'f'Final Error = {final_error:.2f} °C',bbox=dict(boxstyle='round',facecolor='white',alpha=0.8))
p.tight_layout()

#Plot-2
p.figure(figsize=(12, 5))
p.plot(time, cooling_power,color='blue',linewidth=2.5,label='Cooling Power')
p.xlabel("Time (s)")
p.ylabel("Cooling Power")
p.title("Cooling Power vs Time")
p.xlim(0,500)
p.xticks(n.arange(0,501,50))   #to plot an interval of 50s on x axis
p.legend()
p.grid(True,linestyle=':',alpha=0.7)
p.plot(time,cooling_power,color='blue',linewidth=0.5,marker='o',markevery=500)
p.text(350,max_cooling * 0.5,f'Max Cooling Rate\n'f'= {max_cooling:.2f}',bbox=dict(boxstyle='round',facecolor='white',alpha=0.8))
p.fill_between(time,cooling_power,alpha=0.3)
p.tight_layout()
p.show() 