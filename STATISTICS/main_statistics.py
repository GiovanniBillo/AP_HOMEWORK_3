from DataFrameWrapper import DataFrameWrapperInt 
from helpers import reduce_dfw, col_sample, compare_efficiency, Enhance


def main():
    # Create an instance of DataFrameWrapper
    print("Initializing DataFrameWrapper...")
    dfw = DataFrameWrapperInt("r.csv", "oib.csv")

    # Example usage of DataFrameWrapper methods
    print("Instance created successfully.")

    # If your bindings have a method to load a file, call it (example: `load_and_read_file`)
    try:
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
        
        print(Enhance(smaller_dfw))
        Enhance(smaller_dfw).plot("Discount", "Profit")
        Enhance(smaller_dfw).__repr__()
        # print("Let's now compare the performance of this binded class and its hybrid approach with the exclusively C++ one")
        # compare_efficiency()

        # # Get column index for "Discount"
        # discount_index = dfw.get_col_index(column_name1)

        # # Retrieve the Discount column by index
        # discount_column_byindex = dfw.columns_by_index(discount_index)

        # # Retrieve a single entry from the Discount column (4th column, 2nd row)
        # discount_column_entry_byindex = dfw.columns_by_entry(4, 1)

        # # Retrieve a slice of the Discount column (4th column, rows 1 to 4)
        # discount_column_slice = dfw.columns_by_slice(4, 1, 4)

        # print(f"name and then index: {discount_column[1]}, {discount_column[2]}, {discount_column[3]}")
        # print(f"by column index: {discount_column_byindex[1]}, {discount_column_byindex[2]}, {discount_column_byindex[3]}")
        # print(f"indexing into a slice: {discount_column_slice[0]}, {discount_column_slice[1]}, {discount_column_slice[2]}")

        # # Statistical calculations
        # sd = dfw.standard_deviation(column_name1)
        # mean = dfw.mean(column_name1)
        # variance = dfw.variance(column_name1)
        # median = dfw.median(column_name1)
        # correlation = dfw.correlation(column_name1, column_name2)
        # frequency_counts = dfw.frequency_count(column_name1)

        # print(f"Standard Deviation: {sd}")
        # print(f"Mean: {mean}")
        # print(f"Variance: {variance}")
        # print(f"Median: {median}")
        # print(f"Correlation between {column_name1} and {column_name2}: {correlation}")
        # print(f"Frequency counts for {column_name1}: {frequency_counts}")

        # Summary function
        # print("Summary function:")
        # dfw.get_info()

        # print("Classifying column data based on specific criteria:")
        # print("Usage example: classify profit data as below or above average")

        # # Classification based on conditions
        # mean_profit = dfw.mean(column_name2)
        # profits = dfw.columns_by_name(column_name2)

        # categories = ["Below Mean", "Above Mean"]

        # # Define classification conditions as lambda functions //TODO: modify as c++ doesn;t like python lambda functions
        # def below_mean(value):
        #     return value < mean_profit
        # def above_mean(value):
        #     return value >= mean_profit


        # conditions = [
        #         below_mean,
        #         above_mean
        # ]

        # classifications = dfw.classify(column_name2, categories, conditions)

        # print(f"Average profit: {mean_profit}")
        # for i in range(5):  # Display the first 5 entries
        #     print(f"Profit: {profits[i]} -> {classifications[i]}")

    except Exception as e:
        print(f"An error occurred while interacting with DataFrameWrapper: {e}")

if __name__ == "__main__":
    main()


