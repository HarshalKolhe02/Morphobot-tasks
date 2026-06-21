# Q3, PID-Based Drone Altitude Control

## Objective

To implement a PID controller to regulate the altitude of a quadcopter drone.The RC throttle command is used as the control input, while the drone altitude is the controlled variable.

The drone model is:
h(t)=2+0.03u(t)−0.002t

where:
* h(t)=altitude (m)
* u(t)=RC throttle command
* t=time (s)

Target altitude (setpoint):**10 m**

---

## Simulation Parameters and Performance Summary

| Parameter                | Value   |
| ------------------------ | ------- |
| Setpoint Altitude        | 10 m    |
| Initial Altitude         | 2 m     |
| Proportional Gain (Kp)   | 4       |
| Integral Gain (Ki)       | 15      |
| Derivative Gain (Kd)     | 0.005   |
| Simulation Time          | 200 s   |
| Time Step (dt)           | 0.1 s   |
| Achieved Height          | 10.00 m |
| Final Error              | 0.00 m  |
| Maximum Throttle Command | 279.85  |

Created arrays for storing values of altitude,throttle and error values for plotting and comparing values

---

## Altitude control

Initially the drone is at a height of 2m, at around 13 seconds with a sudden increase in throttle command it reaches at height of 10m and the term in height equation which is producing constant decrease in height gets balanced by constantly increasing throttlr command which results in a maintained constant height of 10m from the ground.Thus by making sure of appropriate values kp,ki,kd values by trial error; achieved a stable height of 10m (setpoint) according to the given height equation.

---

## RC Throttle Command 

It is increased at a sudden to achieve a height of 10m initially and then maintain constant increase to overcome the constant decrease in height maintaining constant desired height of 10m.

---

## Controller Performance

### Effect of Proportional Control (Kp)

As it produces an output proportional to the current altitude error. When i increased the kp value, the response speed increased and it resulted in early achievement of setpoint of 10m.

### Role of Integral Control (Ki)

The integral term adds past errors and eliminates steadystate error.When I tried lower values of ki it reaulted in increase in steady state error (it got saturated above 10m).After trial and errror of many values resulted in a theoretical 0 steady state error by mainataining constant height of 10m.

### Effect of Derivative Control (Kd)

It responds to the rate of change of error. when increased kd value it started oscillated and thus decreased the value kd to ensure smooth non oscillating response

### Overall Performance

The PID controller successfully maintained the drone altitude at the desired height of 10 m (as mentioned in question).The final steadystate error was approx zero,reulted in accurate altitude regulation..
