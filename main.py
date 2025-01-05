from ToolBox import DataFrameWrapper, InterpolateWrapper
from helpers import *
from math import sin

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
        # # Create an instance of DataFrameWrapper
    # print("TESTING DATAFRAMEWRAPPER \n Initializing DataFrameWrapper...")
    # dfw = DataFrameWrapperInt("r.csv", "oib.csv")

    # # Example usage of DataFrameWrapper methods
    # print("Instance created successfully.")

    # # If your bindings have a method to load a file, call it (example: `load_and_read_file`)
    # try:
        # # Example call to a method, replace with actual methods defined in your bindings
        # # dfw.load_and_read_file()
        # print("DataFrameWrapper methods can be called here.")
        #   # Load and read file
        # dfw.load_and_read_file()

        # # Column names
        # column_name1 = "Discount"  # index = 4
        # column_name2 = "Profit"    # index = 6

        # # print("Retrieving each information by itself")

        # # # Retrieve the Discount column by name
        # discount_column = dfw.columns_by_name(column_name1)
        # print(type(discount_column))
        # def filter(value):
        #     return value > 0
        # discount_sample = col_sample(dfw, column_name1, 50, filter)

        # print(discount_sample)
        # print("It is also possible to subset a DataFrameWrapper instance and create a new one on the fly")
        # smaller_dfw = reduce_dfw(dfw, "Discount", "Profit")
        # smaller_dfw.get_info() 
        # print(smaller_dfw.input_filename, smaller_dfw.output_filename, smaller_dfw.data_dir)
        
        # print(Enhance(smaller_dfw))
        # Enhance(smaller_dfw).plot("Discount", "Profit")
        # Enhance(smaller_dfw).__repr__()

        # # print("Let's now compare the performance of this binded class and its hybrid approach with the exclusively C++ one")
        # # compare_efficiency()

 

    # except Exception as e:
    #     print(f"An error occurred while interacting with the subpackages: {e}")

    print("TESTING INTERPOLATIONWRAPPER \n Initializing Interpolators...")
    t = 2; 
    n = 8; 
    lb = 0;
    ub = 4;
    tolerance = 0.5;
    vec_x = [1.0, 2.0, 3.0, 4.0, 5.0] 
    vec_y = [f(x) for x in vec_x] 
    ax_points = 10
    linear_interpolator = InterpolateWrapper.LinearInterpolator() 
    lagrange_interpolator= InterpolateWrapper.LagrangeInterpolator()
    spline_interpolator = InterpolateWrapper.SplineInterpolator()

    # Example usage of DataFrameWrapper methods
    print("Instances created successfully.")

    # If your bindings have a method to load a file, call it (example: `load_and_read_file`)
    # try:
    linear_interpolator.build(vec_x, vec_y, len(vec_y), lb, ub)
    Enhance(linear_interpolator).plot(graph_type = "plot", method_name = "Linear") 

    # lagrange_interpolator.build(vec_x, vec_y, len(vec_y), lb, ub)
    # error_lagrange = lagrange_interpolator.error(f, lb, ub) 
    # print(error_lagrange)
    # Enhance(lagrange_interpolator).plot(vec_func = fill_x_Cheby, graph_type = "plot", method_name = "Lagrange") 
    
    error_spline = spline_interpolator.error(f, lb, ub) 
    print(error_spline)

    # spline_interpolator.build(vec_x, vec_y, len(vec_y), lb, ub)
    # error = get_interpolation_method_error(spline_interpolator, method_name = "Spline") 
    # Enhance(spline_interpolator).plot(graph_type = "plot", method_name = "Spline") 
    
    # except Exception as e:
    #     print(f"An error occurred while interacting with the subpackages of InterpolateWrapper: {e}")


if __name__ == "__main__":
    main()


