Here we have made a PID controller to make the drone achieve the given height
<br>
We have been given the altitude as a function of  time as 
<br>
h(t) = 2+0.03u(t) −0.002t
<br>
The desired height is is 10m.<br> 
Tasks-
<br>
1)PID controller has been successfully implemented in python and its code is attached in this folder.<br>
2)Graphs of both have been plotted<br>
3)As we increase the value of Kp, the graph achieves Pv plot moves up but after some increase, it starts oscilallating and on more increase, oscillates rigrously. The Throttle graph also moves up.<br>
If we increase the Ki,it achieves the setpoint, more the Ki , faster we achieve.Throttle graph first increases and then throttle becomes constant.<br>
Increasing Kd makes the situation worse by increasing th oscillation to a very high extent.Same happens in throttle graph.
<br>
In this controller,when all three control variables are zero, the PV plot goes down and does not achieve the setpoint at any time. 

<br>
Best result is obtained by keeping Kp and Kd equal to zero and increasing Ki as much as possible.Ki value of 100 decreases time to 1.407s
