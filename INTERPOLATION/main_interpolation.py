import InterpolationPython as ip
from math import sin
def f(x):
    return sin(x)

def main():
   t = 2; 
   n = 8; 
   lb = -4;
   ub = 4;
   tolerance = 0.5;
   vec_x = [1.0, 2.0, 3.0, 4.0, 5.0] 
   vec_y = [f(x) for x in vec_x] 
   linear_interpolator = ip.LinearInterpolator() 
   # lagrange_interpolator= ip.LagrangeInterpolator()
   # spline_interpolator = ip.SplineInterpolator()

   linear_interpolator.build(vec_x, vec_y, len(vec_y), lb, ub)

    


if __name__ == "__main__":
    main()
