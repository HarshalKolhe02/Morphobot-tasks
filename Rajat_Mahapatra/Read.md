This Readme.md file is dedicated to the information which are common in all codes.
<br>
I have learnt all these codes from gemini pro with extended thinking level,here is the [link](https://gemini.google.com/share/28d8a405dc4e) of the same and the code provided by gemini is in this [link](https://gemini.google.com/share/d745808cd569).
<br>

Although there were several things which were used by gemini which I could not understand or I felt extra, I have removed them from my solution code.

I have commented in most parts of the code regarding their uses in first task and I feel like the other two tasks are very similar to the first task thats why I have not commented anything there. One can easily understand the code in task2 and task3 if he/she refers to the code in task1.

In brief in the code what really happens is that, at first we are making a function in whcich we make arrays to store the values of process variable,time, setpoint and control output at every iteration.In each iteration, we change the process variable as per the given equation. The control output equation is also provided in the question and we are using the same in the code.

Error=Setpoint-PV
<br>
integral+=(error)x(dt)<br>
derivative=(error-error in prev iteration)/dt<br>
Equation of control output=(Kp)x(error)+(Ki)x(integral)+(Kd)x(derivative)

After storing things in array, the function return the same upon call. Then we plot their respective graphs and sliders using matplotlib

One can use the sliders to adjust the values of Kp, Ki and Kd to get the desired results
