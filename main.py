from ToolBox import DataFrameWrapper, InterpolateWrapper

def main():
    try:
        dfw = DataFrameWrapper.DataFrameWrapperInt("r.csv", "oib.csv")
        linear_interpolator = InterpolateWrapper.LinearInterpolator() 
    except Exception as e:
        print(f"An error occurred while interacting with the subpackages: {e}")

if __name__ == "__main__":
    main()


