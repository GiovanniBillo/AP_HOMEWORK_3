from ToolBox import DataFrameWrapper, InterpolateWrapper
from helpers import *
from math import sin

def main():
    print("TESTING DATAFRAMEWRAPPER \n Initializing DataFrameWrapper...")
    dfw = DataFrameWrapperInt("r.csv", "oib.csv")
    print("Instance created successfully.")

    # If your bindings have a method to load a file, call it (example: `load_and_read_file`)
    # Example call to a method, replace with actual methods defined in your bindings
    # dfw.load_and_read_file()
    print("DataFrameWrapper methods can be called here.")
      # Load and read file
    dfw.load_and_read_file()

    # Column names
    column_name1 = "Discount"  # index = 4
    column_name2 = "Profit"    # index = 6

    # print("Retrieving each information by itself")

    # # Retrieve the Discount column by name
    discount_column = dfw.columns_by_name(column_name1)
    print(type(discount_column))
    def filter(value):
        return value > 0
    discount_sample = col_sample(dfw, column_name1, 50, filter)

    print(discount_sample)
    print("It is also possible to subset a DataFrameWrapper instance and create a new one on the fly")
    smaller_dfw = reduce_dfw(dfw, "Discount", "Profit")
    smaller_dfw.get_info() 
    print(smaller_dfw.input_filename, smaller_dfw.output_filename, smaller_dfw.data_dir)
    
    enhanced_dfw = Enhance(smaller_dfw) 
    print(Enhance(smaller_dfw))
    print("By calling the enhance functor, we can apply different useful methods to our data")
    print("e.g Log transformation (or any transformation of choice)")
    log_transformed_data = enhanced_dfw(column_name2) 
    print(log_transformed_data)
    print("e.g MatplotLib plots ")
    enhanced_dfw.plot("Discount", "Profit")
    print("We can also print the information about the object itself thanks to the __str__ and __repr__ magic methods:")
    print(enhanced_dfw) 


    print("TESTING INTERPOLATIONWRAPPER \n Initializing Interpolators...")
    t = 2; 
    n = 8; 
    lb = 0;
    ub = 4;
    vec_x = [1.0, 2.0, 3.0, 4.0, 5.0] 
    vec_y = [math.sin(x) for x in vec_x] 

    linear_interpolator = InterpolateWrapper.LinearInterpolator() 
    lagrange_interpolator= InterpolateWrapper.LagrangeInterpolator()
    spline_interpolator = InterpolateWrapper.SplineInterpolator()

    # Example usage of DataFrameWrapper methods
    print("Instances created successfully.")

    # If your bindings have a method to load a file, call it (example: `load_and_read_file`)
    # try:
    linear_interpolator.build(vec_x, vec_y, len(vec_y), lb, ub)
    Enhance(linear_interpolator).plot(vec_func = fill_x_equid, graph_type = "plot", method_name = "Linear") 

    lagrange_interpolator.build(vec_x, vec_y, len(vec_y), lb, ub)
    Enhance(lagrange_interpolator).plot(vec_func = casual_vec, graph_type = "plot", method_name = "Lagrange") 
    
    spline_interpolator.build(vec_x, vec_y, len(vec_y), lb, ub)
    Enhance(spline_interpolator).plot(graph_type = "plot", method_name = "Spline") 
    


if __name__ == "__main__":
    main()


