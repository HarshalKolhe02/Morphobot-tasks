import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider #slider for changing values of Kp,Ki and Kd

def simulation_values(Kp,Ki,Kd,duration=500,dt=0.1):
    steps=int(duration/dt) #steps is the number of iterations which will occur in the for loop
    time_arr=np.linspace(0,duration,steps) #time array will have the time duration but it has been evenly divided into the number of steps by the linspace function

    pv_arr=np.zeros(steps)  #it will include the process variable as an array to plot the graph, for now all the values in this array is zero
    sv_arr=np.full(steps,24) #similarly this is set point array, all its vales are equal to the setpoint provided in question which is 24
    control_output_arr=np.zeros(steps) #similarly this array will store the control output or in this case cooling power

    pv=35 #putting t=0 in the provided equation for temperature of room, we get that at start temperature is 35 so pv=35    
    
    integral=0
    prev_error=-11 #previous error = 24-35=-11

    for i in range(steps):
        error=sv_arr[i]-pv #error is equal to setpoint-process variable
        integral+=error*dt #it is the sum of all errors
        derivative=(error-prev_error)/dt 

        control_output=Kp*error+Ki*integral+Kd*derivative #this is similar to the quation provided in  the question about the cooling power of AC, we have named it as control output

        
        pv=35+0.02*time_arr[i]-0.05*control_output #this is similar to the temperature of room fiunction provided in the question, we have substituted the cooling power which we got in prev eqn

        prev_error=error #for next iteration
        #storing in array
        pv_arr[i]=pv 
        control_output_arr[i]=control_output

    return time_arr,pv_arr,sv_arr,control_output_arr #we return these values(it will be more clear once you read further part of code)
#initializing the given values of Kp,Ki and Kd given in question
initial_Kp=5 
initial_Ki=0.05
initial_Kd=1
#running the function and   getting vales from it
t,pv,sp,control_output=simulation_values(initial_Kp,initial_Ki,initial_Kd)

#now we are going to plot the graph and soon implement sliders
#here fig is nothing but the window that will be created on our screen, once we run the code. 10,8 are its dimensions in inches. ax1 and ax2 are the graphs for temperature and cooling power respectively
fig, (ax1, ax2)=plt.subplots(2,1,figsize=(10,8))#here 2,1 means there will be 2 rows and 1 column while showing the graphs, or in simple words second graph will be below the first one
plt.subplots_adjust(left=0.2,bottom=0.35,hspace=0.5) #adjusting the position of graphs, left means how much space will be available from left and right sides, same goes for bottom and hspace is the gap to be left between the two graphs

line_pv, =ax1.plot(t,pv,lw=2,color='blue',label='Process Variable') #this is the plot of process variable or here the temperature of room vs time, the comma after the line_pv is needed as this graph will be dynamic as we change the values of kp,ki and kd
line_sv=ax1.plot(t,sp,lw=2,color='red',label='Setpoint')# this will plot the setpoint on same graph, it will remain constant throughout

ax1.set_xlim(0,100) #setting limits within the given time
ax1.set_ylim(20,50)

#additional labellings
ax1.set_title("PID Control of Room Temperature")
ax1.set_xlabel("Time in seconds")
ax1.set_ylabel("Room temperature")
ax1.legend(loc='upper right')

#plot for AC power vs time, the reason for comma after it was explained before
line_control_output, =ax2.plot(t,control_output,lw=2,color='blue',label='Process Variable')


ax2.set_xlim(0,100) #setting limits for given time
# ax2.set_ylim(0,100)

#additional labellings
ax2.set_title(" Control output of Room Temperature")
ax2.set_xlabel("Time in seconds")
ax2.set_ylabel("Control output")
ax2.legend(loc='upper right')


#code for sliders
                #[left,bottom,width,height]
ax1_Kp=plt.axes([0.15,0.20,0.65,0.03]) #position and dimensions for axes which will be used as sliders 
ax1_Ki=plt.axes([0.15,0.15,0.65,0.03])
ax1_Kd=plt.axes([0.15,0.10,0.65,0.03])

# implementing the slider 
                #(axis,labelling,start value,end value,initial value, scale)
slider_Kp=Slider(ax1_Kp,'Kp proportional',-100,10.0, valinit=initial_Kp,valstep=0.001)
slider_Ki=Slider(ax1_Ki,'Ki integral',-100,50.0, valinit=initial_Ki,valstep=0.001)
slider_Kd=Slider(ax1_Kd,'Kd derivative',-100,20.0, valinit=initial_Kd,valstep=0.001)

#for updating values in slider, we use this function
def update(val):
    #these are the values of kp,ki and kc that we will receive upon changing the slider
    current_Kp=slider_Kp.val 
    current_Ki=slider_Ki.val
    current_Kd=slider_Kd.val
    #we run the PID again to with new value of Kp,Ki and Kd but we only take the Pv and AC power from the function as rest all are same
    _,new_pv,_,new_control_output =simulation_values(current_Kp,current_Ki,current_Kd)

    #these two functions are used to implement the new values of pv and AC power in the graph, note that if you will not put comma when line_pv was written before,this function will become useless
    line_pv.set_ydata(new_pv) 
    line_control_output.set_ydata(new_control_output)
    

   
#finally we implement the update function in the new values of of sliders 
slider_Kp.on_changed(update) #.on_changed provides the new values to the update fucntionn
slider_Ki.on_changed(update)
slider_Kd.on_changed(update)
plt.show() #its time to finally plot the graph but based on the sliders, teh graph will be dynamic and change accordingly
