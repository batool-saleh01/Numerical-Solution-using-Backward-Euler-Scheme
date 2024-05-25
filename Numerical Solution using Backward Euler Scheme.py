import numpy
import matplotlib.pyplot

# Parameters
delta_t = 0.1  # Time step
w = 1.0  # Angular frequency

# Initial values
u_prev = 1.0
v_prev = 0.0

# Number of time steps
num_steps = 100

# Arrays to store u and v values
u_values = numpy.zeros(num_steps + 1)
v_values = numpy.zeros(num_steps + 1)

u_values[0] = u_prev
v_values[0] = v_prev

# Backward Euler scheme
for n in range(1, num_steps + 1):
    u = u_prev + delta_t * v_prev
    v = (v_prev - delta_t * w**2 * u) / (1 + delta_t**2 * w**2)
    
    u_values[n] = u
    v_values[n] = v
    
    u_prev = u
    v_prev = v

# Plotting u values
time = numpy.linspace(0, num_steps * delta_t, num_steps + 1)

matplotlib.pyplot.figure(figsize=(12, 6))
matplotlib.pyplot.plot(time, u_values, label='u values', color='blue')
matplotlib.pyplot.xlabel('Time')
matplotlib.pyplot.ylabel('u values')
matplotlib.pyplot.title('Numerical Solution for u using Backward Euler Scheme')
matplotlib.pyplot.legend()
matplotlib.pyplot.grid(True)
matplotlib.pyplot.show()

# Plotting v values
matplotlib.pyplot.figure(figsize=(12, 6))
matplotlib.pyplot.plot(time, v_values, label='v values', color='red')
matplotlib.pyplot.xlabel('Time')
matplotlib.pyplot.ylabel('v values')
matplotlib.pyplot.title('Numerical Solution for v using Backward Euler Scheme')
matplotlib.pyplot.legend()
matplotlib.pyplot.grid(True)
matplotlib.pyplot.show()
