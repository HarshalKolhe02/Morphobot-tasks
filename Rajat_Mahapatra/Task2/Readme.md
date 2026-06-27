We are supposed to make a PID model to control the water level in tank to achieve a partcular level by manipulating the flow rate.
<br>
We have been given the water level as a function of  time as 
<br>
h(t) = 2+0.01t+0.05u(t)
<br>
The desired level is is 5m.<br> 
Tasks-
<br>
1)Numerical integration and finite differences has been implemented.<br>
2)System has been simulated for 500s with time step of 0.1s.<br>
3)Graphs of both have been plotted 

In this controller,when all three control variables are zero, the PV plot criss crosses the Setpoint at around 300s. 
<br>
Increasing the value of Kp does not affect much the time at which the plots criss cross but it decreases the slope of PV vs t graph and after sometime, it also oscillates the graph. At first pump flow rate does not suffer any change but later it oscillates abruptly,
<br>
Increasing Ki,helps in achieving the setpoint, the more we keep the value of Ki, faster we get the value. The pump flow rate first increases steeply and then slowly decreases.
<br>
Increasing Kd does not help much in achieving the setpoint, it just makes the system oscillate making things worse. Pump flow rate also oscillates in the same manner.
<br>
Best result is obtained by keeping Kp and Kd equal to zero and increasing Ki as much as possible.For Ki value of 100 decreases time to 0.660s.

