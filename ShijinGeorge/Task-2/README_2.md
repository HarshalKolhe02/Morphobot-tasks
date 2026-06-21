# Q2,PID Control of Water Level in a Storage Tank

## Objective

- Implement a PID controller in Python to regulate the water level in a storage tank.
- The inlet flow rate is the manipulated variable and the water level is the controlled variable.

- The water level is modeled as
- h(t) = 2 + 0.01t + 0.05u(t)

- h(t) = water level in the tank (m)
- u(t) = pump flow rate (control input)
- 2 + 0.01t represents the natural increase in water level due to a constant external inflow.

- Since the water level will keep on increasing at the given rate without external pumping.
- Inorder to include role of PID in fast filling of water and maintaining specific height of 5m, 
- I just carried out an idea of a pump which is capable of producing outward and inward flow of water from a sink and source.
- Thus the u(t) as the flow rate can be positive(inward-decreases filling time) and negative (outward- maintains saturation)

## Simulation Parameters

| Parameter | Symbol | Value |
|------------|----------|---------|
| Simulation Time | T | 500 s |
| Time Step | dt | 0.1 s |
| Initial Water Level | h(0) | 2 m |
| Desired Water Level | h_set | 5 m |

## PID Gains
- After many trial errors, got values of optimal gains of pid ensuring less overshoot and steady state error as:

| Gain | Description | Value |
|--------|----------------|---------|
| Kp | Proportional Gain | 8 |
| Ki | Integral Gain | 30 |
| Kd | Derivative Gain | 0.005 |


## Results
The following plots were generated:
1. Water Level vs Time
2. Pump Flow Rate vs Time

## Learnings
- Proportional term produces immediate correction,as it is directly prop to current error.it hepls in achieving saturation faster
- integral term reduces steady state error,resulting to saturation near to target value
- derivative term improves stability and reduces oscillation
- eventhough with this pid gain values,small value of steady state error occurd
- this system is highly dependent on integral term