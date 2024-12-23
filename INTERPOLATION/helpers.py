from re import L
import matplotlib.pyplot as plt
import numpy as np 


class Enhance:
    def __init__(self, intw):
        self.intw = intw
    def plot_errors(self, max_points, vec_func, plot_func, y_func, lb, ub, method_name):
        error_dict = {}
        for i in range(max_points):
            n = 2*i
            x = vec_func(n, lb, ub)
            y = [y_func(n) for n in x] 
            self.intw.build(x, y, len(y), lb, ub)
        
            error = self.intw.error(y_func, lb, ub)
            error_dict[n] = error
        plot_func(error_dict.keys(), error_dict.values(), method_name) 
