# PID Control of Room Temperature

## Objective

To implement a PID controller in Python to regulate the temperature of a room using an air conditioner using PID
The cooling power supplied by the AC is the manipulated variable,the room temperature is the controlled variable.

The room temperature model is given by:
T(t)=35+0.02t−0.05u(t)

where:
* T(t)=Room temperature (degree Celsius)
* u(t)=Cooling power supplied by the AC
* 35+0.02t represents heating from the surroundings

The desired room temperature is:
Tset=24 deg C

---

## Working of the Code

### 1. Simulation

* Simulation Duration=500 s
* Time Step=0.1 s

Arrays are created to store the room temperature and cooling power values at each time step. (initially I used list,then thought arrays would be better)
The initial room temperature is:
T(0)=35 deg C

---

### 2. Error Calculation

The error is defined according to the question
e(t) = Tset − T(t)

Initially:
e=24−35= -11 deg C

The controller continuously calculates this error and attempts to reduce it to zero.

---

### 3. PID Controller Implementation

The PID controller consists of three components.

#### Proportional Term

The proportional term responds to the current error:
P = error
A larger error produces immediate response.

#### Integral Term

The integral term accumulates past errors using numerical integration:
I += error*dt
This helps eliminate steadystate error.

#### Derivative Term

The derivative term predicts future error behavior using finite differences:
D =(error − last_eror)/dt
This reduces oscillations and improves stability.

---

### 4. Controller Output

The PID controller output is calculated as:
u= Kp * P + Ki * I + Kd * D

where optimal solution after tuning is:
* Kp = 0.48
* Ki = 0.98
* Kd = 0.091

I did many trial and errors and ended up in these values which only produces less overshoot and steady state error

---

### 5. Why I used `cooling = max(0, -u)` in my code?

In the question, the error is defined as:
e(t)=Tset−T(t)

Since the initial room temperature is higher than the desired temperature:
e=24−35=-11  (I didnt change the error definition)
the PID output becomes negative.
(Impractical for an AC to cause heating)
Therefore I used:
cooling = max(0,-u)

For example:
If:
u = -200
then:
cooling = max(0, 200)
which gives:
cooling = 200

This converts the negative controller output into a positive cooling command while still following the error definition provided in the assignment.

Initially I didn't use this,but that time instead saturating at 24 ;temp was increasing from 35 going to higher value 

---

## Simulation Parameters and Performance Summary

| Parameter                  | Value    |
| -------------------------- | -------- |
| Desired Temperature        | 24 C     |
| Initial Temperature        | 35 C     |
| Proportional Gain (Kp)     | 0.48     |
| Integral Gain (Ki)         | 0.98     |
| Derivative Gain (Kd)       | 0.091    |
| Simulation Duration        | 500s     |
| Time Step (dt)             | 0.1s     |
| Maximum Cooling Rate       | 419.80   |

---

## Temperature Profile

The temperature profile shows the room temperature decreasing from the initial value of 35 deg C and approaching the desired setpoint of 24 deg C.
After achieving a temp of 24 deg C, eventhough the surrounding temp is being increasing constantly gets balanced by the constant cooling rate after saturation near to 24 deg C.

---

## Cooling Power Profile

The cooling power profile shows the controller effort required to regulate the room temperature.
Initially the temp is at 35 deg C,a sudden descent is produced for maintaining 24 deg C. after that it produces adequate constantly incrreasing cooling rte for maintaing constant temp of desired 24 deg C by balancing the increasing surrounding temp.

