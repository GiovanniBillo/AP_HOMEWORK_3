from helpers import timer
from ToolBox import DataFrameWrapper, InterpolateWrapper
import pandas as pd
import os
import math
from scipy.interpolate import interp1d, lagrange, CubicSpline


class Compare:
    '''
    Compare the efficiency of the program (C++ code bound to python) vs some python libraries/standard operations
    By default, a very large (~10000) dataset is considered).

    '''
    def __init__(self, data_dir = "data", filename = "ranking.csv", dftype = "int",
                 t = 2.5, n = 8, lb = 0, ub = 4, tolerance = 0.5, 
                 vec_x = [1.0, 2.0, 3.0, 4.0, 5.0], 
                 max_points = 10):
       self.data_dir = data_dir
       self.filename = filename
       self.dftype = dftype
       self.t = n
       self.ub = ub
       self.lb = lb 
       self.vec_x = vec_x
       self.vec_y = [math.sin(x) for x in self.vec_x] 
       self.max_points = max_points

    @timer
    def myprogram_import(self):
        rankings = os.path.join(self.filename)
        if (self.dftype == "int"):
            dfw = DataFrameWrapper.DataFrameWrapperInt(self.filename, self.filename + "_out")
            dfw.load_and_read_file()
            print(dfw)
        elif (self.dftype == "str"):
            dfw = DataFrameWrapper.DataFrameWrapperStr(self.filename, self.filename + "_out")
            dfw.load_and_read_file()
            print(dfw)
        return 

    @timer
    def python_import(self):
        path = self.data_dir + "/" + self.filename 
        ranking = pd.read_csv(path)
        ranking.head() 
        return
    @timer
    def my_program_interpolate(self):
        linear_interpolator = InterpolateWrapper.LinearInterpolator() 
        lagrange_interpolator= InterpolateWrapper.LagrangeInterpolator()
        spline_interpolator = InterpolateWrapper.SplineInterpolator()
        
        linear_interpolator.build(self.vec_x, self.vec_y, len(self.vec_y), self.lb, self.ub)
        lagrange_interpolator.build(self.vec_x, self.vec_y, len(self.vec_y), self.lb, self.ub)
        spline_interpolator.build(self.vec_x, self.vec_y, len(self.vec_y), self.lb, self.ub)
        
        linear_interpolator(self.t)
        lagrange_interpolator(self.t)
        spline_interpolator(self.t)
        pass
    @timer
    def python_interpolate(self):
        py_lin = interp1d(self.vec_x, self.vec_y, kind='linear', bounds_error=False, fill_value='extrapolate')
        py_lagrange = lagrange(self.vec_x, self.vec_y)
        py_spline = CubicSpline(self.vec_x, self.vec_y, extrapolate=True)


        pass
    def __call__(self):
        print("Comparing performance for the statistics module...")
        self.myprogram_import()
        self.python_import()
        print("Comparing performance for the interpolation module...")
        self.my_program_interpolate()
        self.python_interpolate()

def main():
    comparison = Compare()
    comparison()
    print("The Pandas implementation dwarfs the implemented one, because the third party library DataFrame needs the csv to be in a specific format. \n  Much time is therefore wasted to infer column types and format it.\n  However when we compare performance on a Dataset that is already formatted: \n ")
    comparison2 = Compare(data_dir = "data", filename = "IBM.csv", dftype = "str")
    comparison2()
    print("our implementation is slighly faster. \n For interpolation, the ALGLIB library is slightly faster or just as fast as scipy to compute a single point with 3 interpolators, depending on the input.")


if __name__ == "__main__":
    main()


