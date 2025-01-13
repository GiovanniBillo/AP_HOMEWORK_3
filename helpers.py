from ToolBox.DataFrameWrapper import DataFrameWrapperInt, DataFrameWrapperStr, DataFrameWrapperDouble, check_condition
from ToolBox.InterpolateWrapper import Interpolator
from random import sample, uniform 
import csv
import os
import time
import matplotlib.pyplot as plt
import math
from re import L
import numpy as np 

def fill_x_equid(n, lb, ub):
    return [lb + (ub - lb) * i / (n - 1) for i in range(n)]

def fill_x_Cheby(n, lb, ub):
    x_Cheby = []
    for i in range(n):
        value = 0.5 * (ub + lb) + 0.5 * (ub - lb) * math.cos(math.pi * (2 * i + 1) / (2 * n))
        x_Cheby.append(value)
    return x_Cheby

def casual_vec(n, lb, ub):
    """
    Generate a list of `n` unique random points between `lb` and `ub`.
    """
    # if n > (ub - lb):  # Ensure we can generate `n` unique numbers in the range
    #     raise ValueError("Cannot generate more unique points than the range size.")

    unique_numbers = set()
    while len(unique_numbers) < n:
        num = uniform(lb, ub)
        unique_numbers.add(num)  # Ensure unique points

    return list(unique_numbers)


def timer(my_function):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = my_function(*args, **kwargs)
        t2 = time.time()
        print(f"{my_function.__name__} ran in {t2 - t1:.3f} sec")
        return result
    return wrapper

@timer
def col_sample(dfw, colname, n_sample, filter):
    colsample = sample(dfw.columns_by_name(colname), n_sample)
    check_condition(colsample, filter)
    return colsample

@timer
def reduce_dfw(dfw, *colnames, data_dir = "data", input_filename = "reduced_data_in.csv", output_filename = "reduced_data_out.csv"):
   newdata = {}
   n_rows = 0
   # Ensure the data directory exists
   os.makedirs(data_dir, exist_ok=True)
   # Extract the specified columns and determine the number of rows
   for colname in colnames:
       col = dfw.columns_by_name(colname)
       newdata[colname] = col
       n_rows = len(col)  # Assuming all columns have the same number of rows

   input_csv = os.path.join(data_dir, input_filename)
   # Print the full paths to the files
   # print(f"Output CSV path: {output_csv}")

   with open(input_csv, mode='w', newline='') as file:
       writer = csv.writer(file)
       writer.writerow(["INDEX"] + list(colnames))  # Write the header row
       for i in range(n_rows):
           writer.writerow([i] + [newdata[colname][i] for colname in colnames])  # Write each row

   new_dfw = DataFrameWrapperInt(input_filename, output_filename)
   new_dfw.load_and_read_file()
   return new_dfw

class Enhance:
    def __init__(self, wrapper):
        """
        Initialize Enhance with a generic wrapper object.
        Supports both DataFrameWrapper and InterpolateWrapper.
        """
        self.wrapper = wrapper

    def __call__(self, colname, transform_func = lambda data, base=np.e: np.log(data) / np.log(base), *args, **kwargs):
        """
        Apply a transformation function to the wrapper data dynamically. The default one is log transform.
        """
        if isinstance(self.wrapper, (DataFrameWrapperInt, DataFrameWrapperStr, DataFrameWrapperDouble)):
            # Assume `self.wrapper.data` contains the data
            column = self.wrapper.columns_by_name(colname) 
            transformed_data = transform_func(column, *args, **kwargs)
            return transformed_data
        elif isinstance(self.wrapper, Interpolator):
            raise TypeError("Transformation is not supported for Interpolator wrappers.")
        else:
            raise TypeError(f"Unsupported wrapper type: {type(self.wrapper)}")

    def __str__(self, n=10):
        """
        Display the first n rows of the data if it's a DataFrameWrapper.
        """
        if isinstance(self.wrapper, (DataFrameWrapperInt, DataFrameWrapperStr, DataFrameWrapperDouble)):
            path = self.wrapper.data_dir + "/" + self.wrapper.output_filename
            count = 0
            with open(path, mode='r') as file:
                csv_file = csv.reader(file)
                for lines in csv_file:
                    if count < n:
                        print(lines)
                        count += 1
            print(f"{self.wrapper.n_rows - n} more rows ...")
            return ""
        elif isinstance(self.wrapper, Interpolator):
            return f"InterpolateWrapper object with {len(self.wrapper.functions)} interpolation functions."
        else:
            raise TypeError(f"Unsupported wrapper type: {type(self.wrapper)}")

    def __repr__(self):
        """
        Display characteristics of the wrapper object.
        """
        if isinstance(self.wrapper, (DataFrameWrapperInt, DataFrameWrapperStr, DataFrameWrapperDouble)):
            return (
                f"DataFrameWrapper: {self.wrapper.n_rows} rows, {self.wrapper.n_cols} columns\n"
                f"Column info: {self.wrapper.column_info}"
            )
        elif isinstance(self.wrapper, Interpolator):
            return (
                f"InterpolateWrapper with {len(self.wrapper.functions)} interpolation functions:\n"
                f"{self.wrapper.functions}"
            )
        else:
            return "Unsupported wrapper type."

    def plot(self, colname_x = "x", colname_y = "y", 
             graph_type='scatter', 
             method_name = "Linear",
             # max_points = 10
             # lb = 0,
             # ub = 4
            vec_func = fill_x_equid 
             # y_func = f
             ):
        """
        Plot the data dynamically based on the graph type.
        """
        if isinstance(self.wrapper, (DataFrameWrapperInt, DataFrameWrapperStr, DataFrameWrapperDouble) ):
            x = self.wrapper.columns_by_name(colname_x)
            y = self.wrapper.columns_by_name(colname_y)
        elif isinstance(self.wrapper, Interpolator):
            errors = get_interpolation_method_error(self.wrapper, method_name = method_name, vec_func = vec_func)
            x = errors.keys()
            y = errors.values()
            colname_x = "n. of of points"
            colname_y = method_name + "Interpolator errors" 
        else:
            raise TypeError(f"Unsupported wrapper type: {type(self.wrapper)}")

        # Check if the graph_type is valid
        if not hasattr(plt, graph_type):
            raise ValueError(f"Invalid graph_type '{graph_type}'. Please use a valid matplotlib plotting method.")
        
        plot_func = getattr(plt, graph_type)
        plot_func(x, y)

        # Label axes and add title
        plt.xlabel(colname_x)
        plt.ylabel(colname_y)
        plt.title(f"{colname_x} vs. {colname_y}")

        # Show or save the plot
        show_plot = input("Would you like to show the plot? [Y/N] ").strip().upper()
        if show_plot == "Y":
            plt.show()
        else:
            plt.savefig("plot.png")

def get_interpolation_method_error(wrapper, method_name, vec_func, max_points = 10, y_func = lambda x: math.sin(x), lb = 0.0, ub = 3.14):
        error_dict = {}
        for i in range(1, max_points):
            n = 2*i
            vec_x = vec_func(n, lb, ub)
            # vec_x = [1.0, 2.0, 3.0, 4.0, 5.0] 
            vec_y = [y_func(x) for x in vec_x] 
            wrapper.build(vec_x, vec_y, len(vec_y), lb, ub)
        
            error = wrapper.error(y_func, lb, ub)
            error_dict[n] = error
        return error_dict

