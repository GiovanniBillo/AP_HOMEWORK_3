from DataFrameWrapper import DataFrameWrapperInt, DataFrameWrapperStr, check_condition
from random import sample 
import csv
import os
import time

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
def reduce_dfw(dfw, *colnames, data_dir = "data"):
   newdata = {}
   n_rows = 0
   # Ensure the data directory exists
   os.makedirs(data_dir, exist_ok=True)
   # Extract the specified columns and determine the number of rows
   for colname in colnames:
       col = dfw.columns_by_name(colname)
       newdata[colname] = col
       n_rows = len(col)  # Assuming all columns have the same number of rows

   input_csv = os.path.join(data_dir, "reduced_data_in.csv")
   # Print the full paths to the files
   # print(f"Output CSV path: {output_csv}")

   with open(input_csv, mode='w', newline='') as file:
       writer = csv.writer(file)
       writer.writerow(["index"] + list(colnames))  # Write the header row
       for i in range(n_rows):
           writer.writerow([i] + [newdata[colname][i] for colname in colnames])  # Write each row

   new_dfw = DataFrameWrapperInt("reduced_data_in.csv", "reduced_data_out.csv")
   new_dfw.load_and_read_file()
   return new_dfw



@timer
def compare_efficiency(data_dir = "data", filename="ranking.csv"):
   rankings = os.path.join(filename)
   dfw_rankings = DataFrameWrapperInt(filename, filename + "_out")
   dfw_rankings.load_and_read_file()


# class Enhance:
#     def __init__(self, dfw):
#         self.dfw = dfw
#     # def __repr__(self):

#     def __str__(self):
        

        
