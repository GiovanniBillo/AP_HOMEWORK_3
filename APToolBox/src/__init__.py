# Import specific classes and functions from the .so libraries
from .DataFrameWrapper import DataFrameWrapperInt, DataFrameWrapperStr, DataFrameWrapperDouble, check_condition
from .InterpolateWrapper import Interpolator

# Import helper functions and classes from helpers.py
from .helpers import (
    fill_x_equid,
    fill_x_Cheby,
    casual_vec,
    timer,
    col_sample,
    reduce_dfw,
    Enhance,
    get_interpolation_method_error,
)

# Package metadata
__version__ = "1.0.0"
__author__ = "billogiovanni"

# Define what should be exposed when `from package import *` is used
__all__ = [
    "DataFrameWrapperInt",
    "DataFrameWrapperStr",
    "DataFrameWrapperDouble",
    "check_condition",
    "Interpolator",
    "fill_x_equid",
    "fill_x_Cheby",
    "casual_vec",
    "timer",
    "col_sample",
    "reduce_dfw",
    "Enhance",
    "get_interpolation_method_error",
]

