# from ToolBox import DataFrameWrapperInt, DataFrameWrapperStr, InterpolationWrapper
from DataFrameWrapper import DataFrameWrapperInt, DataFrameWrapperStr, check_condition
from random import sample 
import csv
import os
import time
import matplotlib.pyplot as plt
import math

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



@timer
def compare_efficiency(data_dir = "data", filename="ranking.csv"):
   rankings = os.path.join(filename)
   dfw_rankings = DataFrameWrapperInt(filename, filename + "_out")
   dfw_rankings.load_and_read_file()


class Enhance:
    def __init__(self, wrapper):
        """
        Initialize Enhance with a generic wrapper object.
        Supports both DataFrameWrapper and InterpolationWrapper.
        """
        self.wrapper = wrapper

    def __str__(self, n=10):
        """
        Display the first n rows of the data if it's a DataFrameWrapper.
        """
        if isinstance(self.wrapper, DataFrameWrapperInt):
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
        elif isinstance(self.wrapper, InterpolationWrapper):
            return f"InterpolationWrapper object with {len(self.wrapper.functions)} interpolation functions."
        else:
            raise TypeError(f"Unsupported wrapper type: {type(self.wrapper)}")

    def __repr__(self):
        """
        Display characteristics of the wrapper object.
        """
        if isinstance(self.wrapper, DataFrameWrapper):
            return (
                f"DataFrameWrapper: {self.wrapper.n_rows} rows, {self.wrapper.n_cols} columns\n"
                f"Column info: {self.wrapper.column_info}"
            )
        elif isinstance(self.wrapper, InterpolationWrapper):
            return (
                f"InterpolationWrapper with {len(self.wrapper.functions)} interpolation functions:\n"
                f"{self.wrapper.functions}"
            )
        else:
            return "Unsupported wrapper type."

    def plot(self, colname_x, colname_y, graph_type='scatter', method_name = "Linear"):
        """
        Plot the data dynamically based on the graph type.
        """
        if isinstance(self.wrapper, DataFrameWrapper):
            x = self.wrapper.columns_by_name(colname_x)
            y = self.wrapper.columns_by_name(colname_y)
        elif isinstance(self.wrapper, InterpolationWrapper):
            get_interpolation_method_error("Linear")
            
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

def fill_x_equid(n, lb, ub):
    return [lb + (ub - lb) * i / (n - 1) for i in range(n)]

def get_interpolation_method_error(self, max_points = 10, vec_func = fill_x_equid, y_func = lambda x: math.sin(x), lb = 0.0, ub = 3.14, method_name):
        error_dict = {}
        for i in range(max_points):
            n = 2*i
            x = vec_func(n, lb, ub)
            y = [y_func(n) for n in x] 
            self.intw.build(x, y, len(y), lb, ub)
        
            error = self.intw.error(y_func, lb, ub)
            error_dict[n] = error
        return error_dict
# class Enhance:
#     def __init__(self, dfw):
#         self.dfw = dfw
#     # def __repr__(self):

#     def __str__(self, n = 10):
#         path = self.dfw.data_dir +"/"+ self.dfw.output_filename
#         count = 0
#         with open(path, mode ='r') as file:
#           csvFile = csv.reader(file)
#           for lines in csvFile :
#             if count < n:
#                print(lines)
#                count = count + 1
#         print(f"{self.dfw.n_rows - 10} more rows ...")
#         return ""
#     def __repr__(self):
#         print("A DataFrameWrapper object with the following characteristics:")
#         print("Number of rows:", self.dfw.n_rows, "Number of columns:", self.dfw.n_cols, "\n with names and types:")
#         print(self.dfw.column_info)
#         return ""
     

#     def plot(self, colname_x, colname_y, graph_type = 'scatter'):
#         # Check if the graph_type is valid
#         if not hasattr(plt, graph_type):
#             raise ValueError(f"Invalid graph_type '{graph_type}'. Please use a valid matplotlib plotting method.")

#         # Dynamically call the appropriate matplotlib function
#         plot_func = getattr(plt, graph_type)
#         x = self.dfw.columns_by_name(colname_x)
#         y = self.dfw.columns_by_name(colname_y)
        
#         plot_func(x, y)

#         # naming the x axis  
#         plt.xlabel(colname_x)  
#         # naming the y axis  
#         plt.ylabel(colname_y)  
            
#         # giving a title to my graph  
#         plt.title(colname_x + " vs. " + colname_y)  
        
#         show_plot = input("Would you like to show the plot? [Y/N]")
#         if (show_plot == "Y"):
#             plt.show() 
#         else:
#             plt.savefig("plot.png")

# #     def somefunctionforNUmpy(...):
# #     def somefunctionforScioy(...):
        

        
