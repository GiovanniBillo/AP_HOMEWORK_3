import InterpolateWrapper as ip
from helpers import Enhance
import matplotlib.pyplot as plt
import numpy as np
from math import pi, sin

def f(x):
    return sin(x)
# Define the vector generating function
def generate_vector(n, lb, ub):
    """Generate n evenly spaced points between lb and ub."""
    return np.linspace(lb, ub, n)

# Define the mapping function for y-values
def map_function(x):
    """Map function to calculate y-values based on x."""
    print("THIS IS X:", x)
    return [val**2 for val in x]  # Example: y = x^2

# Define the plot function
def plot_function(x_values, y_values, method_name):
    """Plot the x and y values using matplotlib."""
    plt.figure(figsize=(8, 6))
    plt.plot(x_values, y_values, label=f"Method: {method_name}")
    plt.xlabel("x-values")
    plt.ylabel("y-values")
    plt.title(f"Plot for {method_name}")
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
   t = 2; 
   n = 8; 
   lb = 0;
   ub = 4;
   tolerance = 0.5;
   vec_x = [1.0, 2.0, 3.0, 4.0, 5.0] 
   vec_y = [f(x) for x in vec_x] 
   max_points = 10
   linear_interpolator = ip.LinearInterpolator() 
   lagrange_interpolator= ip.LagrangeInterpolator()
   spline_interpolator = ip.SplineInterpolator()

   linear_interpolator.build(vec_x, vec_y, len(vec_y), lb, ub)
   Enhance(linear_interpolator).plot_errors(max_points, generate_vector, plot_function, f, lb, ub, "Linear") 

   # lagrange_interpolator.build(vec_x, vec_y, len(vec_y), lb, ub)
   # Enhance(lagrange_interpolator).plot_errors(max_points, generate_vector, plot_function, f, lb, ub, "Lagrange") 
    
    
   # spline_interpolator.build(vec_x, vec_y, len(vec_y), lb, ub)
   # Enhance(spline_interpolator).plot_errors(max_points, generate_vector, plot_function, f, lb, ub, "Spline") 
    

    


if __name__ == "__main__":
    main()
