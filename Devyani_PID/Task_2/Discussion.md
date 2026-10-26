There is a '2+0.01t' term for  natural increase in water level due to a constant external inflow.
So when the desired level is reached, the flow must now start becoming negative or external inflow must be stopped
In other words we must either drain(negative flow) or stop external flow.
The code is conditioned to work only till flow reaches zero but both graphs have been attatched.
In terms of PID i saw that the derivative wasnt affecting as there were no specific overshoots, so I have made it PI and it works fine enough.
