import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider,Button

def simulation_values(Kp,Ki,Kd,duration=500,dt=0.1):
    steps=int(duration/dt)
    time_arr=np.linspace(0,duration,steps)

    pv_arr=np.zeros(steps)
    sv_arr=np.full(steps,10)
    control_output_arr=np.zeros(steps)

    pv=2
    
    
    integral=0
    prev_error=8

    for i in range(steps):
        error=sv_arr[i]-pv
        integral+=error*dt
        derivative=(error-prev_error)/dt

        control_output=Kp*error+Ki*integral+Kd*derivative

        
        pv=2-0.002*time_arr[i]+0.03*control_output

        prev_error=error
        pv_arr[i]=pv
        control_output_arr[i]=control_output

    return time_arr,pv_arr,sv_arr,control_output_arr
    
initial_Kp=1
initial_Ki=0
initial_Kd=0

t,pv,sp,control_output=simulation_values(initial_Kp,initial_Ki,initial_Kd)

fig, (ax1, ax2)=plt.subplots(2,1,figsize=(10,8))
plt.subplots_adjust(left=0.2,bottom=0.35,hspace=0.5)

line_pv, =ax1.plot(t,pv,lw=2,color='blue',label='Process Variable')
line_sv=ax1.plot(t,sp,lw=2,color='red',label='Setpoint')

ax1.set_xlim(0,500)
ax1.set_ylim(0,20)
ax1.set_title("Altitude vs time")
ax1.set_xlabel("Time in seconds")
ax1.set_ylabel("Height in metres")
ax1.legend(loc='upper right')


line_control_output, =ax2.plot(t,control_output,lw=2,color='blue',label='Control output')


ax2.set_xlim(0,500)
ax2.set_ylim(0,500)
ax2.set_title(" RC throttle command vs time")
ax2.set_xlabel("Time in seconds")
ax2.set_ylabel("Throttle")
ax2.legend(loc='upper right')


ax1_Kp=plt.axes([0.15,0.20,0.65,0.03],facecolor='green')
ax1_Ki=plt.axes([0.15,0.15,0.65,0.03],facecolor='green')
ax1_Kd=plt.axes([0.15,0.10,0.65,0.03],facecolor='green')
slider_Kp=Slider(ax1_Kp,'Kp proportional',0.0,100.0, valinit=initial_Kp,valstep=0.1)
slider_Ki=Slider(ax1_Ki,'Ki integral',0.0,100.0, valinit=initial_Ki,valstep=0.1)
slider_Kd=Slider(ax1_Kd,'Kd derivative',0.0,20.0, valinit=initial_Kd,valstep=0.1)

def update(val):
    current_Kp=slider_Kp.val
    current_Ki=slider_Ki.val
    current_Kd=slider_Kd.val

    _,new_pv,_,new_control_output =simulation_values(current_Kp,current_Ki,current_Kd)
    line_pv.set_ydata(new_pv)
    line_control_output.set_ydata(new_control_output)
    

    

slider_Kp.on_changed(update)
slider_Ki.on_changed(update)
slider_Kd.on_changed(update)
plt.show()