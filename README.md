# Numerical Solution using Backward Euler Scheme #
This ```Python``` script demonstrates the application of the ```Backward Euler scheme``` to solve a simple differential equation numerically. It generates plots for the values of ```u``` and ```v``` over time.

## Prerequisites ##
### Required libraries ###
```numpy``` and ```matplotlib```
You can install them using this command line

> pip install numpy matplotlib.

## Understanding the Code ##
- ```delta_t``` Time step used for the numerical integration.
- ```w``` Angular frequency.
- ```u_prev``` ```v_prev``` Initial values for ```u``` and ```v```.
- ```num_steps``` Number of time steps for the simulation.

## Running the Script ##
1- Download or clone the Python script backward_euler.py.

2- Open a terminal or command prompt.

3- Navigate to the directory containing backward_euler.py.

4- Run the script using the command python backward_euler.py.

## Results ##
Two plots will be generated:

```Plot 1``` Numerical solution for ```u``` over time.

```Plot 2``` Numerical solution for ```v``` over time.

## Customization ##
- You can modify the parameters such as ```delta_t```, ```w``` and initial values to observe different behaviors.
- Experiment with changing the number of time steps ```num_steps``` for a more detailed simulation.

## Acknowledgements ##
This script was inspired by the concept of numerical methods for solving differential equations 
