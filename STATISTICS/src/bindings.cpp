#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/functional.h>
#include <pybind11/stl_bind.h>
#include "DataFrameWrapper.hpp"

namespace py = pybind11;

PYBIND11_MODULE(DataFrameWrapper, m) {
    m.doc() = "Python bindings for DataFrameWrapper";

    m.def("check_condition", &Toolbox::dfw::check_condition, py::arg("col"), py::arg("filter"));
//INT
    py::class_<Toolbox::dfw::DataFrameWrapper<int>>(m, "DataFrameWrapperInt")
        .def(py::init<>())

        .def(py::init<const char *, const char *>(),
             py::arg("inputFilename"), py::arg("outputFilename"))
        
        // GETTER METHODS
        .def_property_readonly("column_info", 
               [](const Toolbox::dfw::DataFrameWrapper<int> &self) {
                return self.getColumnInfo();
            })
        .def_property_readonly("n_rows", 
               [](const Toolbox::dfw::DataFrameWrapper<int> &self) {
                return self.getRowCount();
            })
        .def_property_readonly("n_cols", 
               [](const Toolbox::dfw::DataFrameWrapper<int> &self) {
                return self.getColCount();
            })
        .def_property_readonly("input_filename", 
               [](const Toolbox::dfw::DataFrameWrapper<int> &self) {
                return self.getInputFilename();
            })
        .def_property_readonly("output_filename",
                [](const Toolbox::dfw::DataFrameWrapper<int> &self) {
                return self.getOutputFilename();
            })
        .def_property_readonly("data_dir", 
                [](const Toolbox::dfw::DataFrameWrapper<int> &self) {
                return self.getDataDirectory().string();
                })

        .def("load_and_read_file", &Toolbox::dfw::DataFrameWrapper<int>::loadAndReadFile,
             "Load and read the input file.")

        .def("get_col_index", &Toolbox::dfw::DataFrameWrapper<int>::getColIndex,
             py::arg("columnName"),
             "Get the index of a column by name.")

        .def("columns_by_name", [](Toolbox::dfw::DataFrameWrapper<int> &self, const char *columnName) {
                return self.columns<double>(columnName); // Explicit template argument
            },
            /* py::arg("columnName"), */
            "Retrieve a column by name.")

        .def("columns_by_index",[](Toolbox::dfw::DataFrameWrapper<int> &self, size_t col_index) {
                 return self.columns<double>(col_index); // Explicit template argument
            },
           "Retrieve a column by index.")

        .def("columns_by_entry",[](Toolbox::dfw::DataFrameWrapper<int> &self, size_t col_index, size_t row_index) {
                return self.columns<double>(col_index, row_index); // Explicit template argument
            },
             /* py::arg("col_index"), py::arg("row_index"), */
             "Retrieve a specific entry in a column.")

        .def("columns_by_slice", [](Toolbox::dfw::DataFrameWrapper<int> &self, size_t col_index, size_t start, size_t stop) {
                return self.columns<double>(col_index, start, stop); // Explicit template argument
            },
             /* py::arg("col_index"), py::arg("start"), py::arg("stop"), */
             "Retrieve a slice of a column.")

        .def("standard_deviation", &Toolbox::dfw::DataFrameWrapper<int>::template StandardDeviation<double>,
             py::arg("columnName"),
             "Calculate the standard deviation of a column.")

        .def("mean", &Toolbox::dfw::DataFrameWrapper<int>::template Mean<double>,
             py::arg("columnName"),
             "Calculate the mean of a column.")

        .def("variance", &Toolbox::dfw::DataFrameWrapper<int>::template Variance<double>,
             py::arg("columnName"),
             "Calculate the variance of a column.")

        .def("median", &Toolbox::dfw::DataFrameWrapper<int>::template Median<double>,
             py::arg("columnName"),
             "Calculate the median of a column.")

        .def("correlation", &Toolbox::dfw::DataFrameWrapper<int>::template Correlation<double>,
             py::arg("columnName1"), py::arg("columnName2"),
             "Calculate the correlation between two columns.")

        .def("frequency_count", &Toolbox::dfw::DataFrameWrapper<int>::template frequencyCount<double>,
             py::arg("columnName"),
             "Get the frequency count of a column.")

        .def("classify", &Toolbox::dfw::DataFrameWrapper<int>::template Classify<double>,
             py::arg("columnName1"), py::arg("categories"), py::arg("conditions"),
             "Classify column data based on conditions.")

#ifdef INTERPOLATION_MODULE
        .def("interpolate", &Toolbox::dfw::DataFrameWrapper<int>::template Interpolate<double>,
             py::arg("columnName1"), py::arg("columnName2"), py::arg("categories"), py::arg("conditions"),
             "Interpolate column data based on conditions.")
#endif

        .def("get_info", &Toolbox::dfw::DataFrameWrapper<int>::getInfo,
             "Retrieve basic information about the DataFrame.");

// DOUBLE
    py::class_<Toolbox::dfw::DataFrameWrapper<double>>(m, "DataFrameWrapperDouble")
        .def(py::init<>())
        .def(py::init<const char *, const char *>(),
             py::arg("inputFilename"), py::arg("outputFilename"))

        .def_property_readonly("input_filename", 
               [](const Toolbox::dfw::DataFrameWrapper<int> &self) {
                return self.getInputFilename();
            })
        .def_property_readonly("output_filename",
                [](const Toolbox::dfw::DataFrameWrapper<int> &self) {
                return self.getOutputFilename();
            })
        .def_property_readonly("data_dir", 
                [](const Toolbox::dfw::DataFrameWrapper<int> &self) {
                return self.getDataDirectory().string();
                })

        .def("load_and_read_file", &Toolbox::dfw::DataFrameWrapper<double>::loadAndReadFile,
             "Load and read the input file.")

        .def("get_col_index", &Toolbox::dfw::DataFrameWrapper<double>::getColIndex,
             py::arg("columnName"),
             "Get the index of a column by name.")

        .def("columns_by_name", [](Toolbox::dfw::DataFrameWrapper<double> &self, const char *columnName) {
                return self.columns<double>(columnName); // Explicit template argument
            },
            /* py::arg("columnName"), */
            "Retrieve a column by name.")

        .def("columns_by_index",[](Toolbox::dfw::DataFrameWrapper<double> &self, size_t col_index) {
                 return self.columns<double>(col_index); // Explicit template argument
            },
           "Retrieve a column by index.")

        .def("columns_by_entry",[](Toolbox::dfw::DataFrameWrapper<double> &self, size_t col_index, size_t row_index) {
                return self.columns<double>(col_index, row_index); // Explicit template argument
            },
             /* py::arg("col_index"), py::arg("row_index"), */
             "Retrieve a specific entry in a column.")

        .def("columns_by_slice", [](Toolbox::dfw::DataFrameWrapper<double> &self, size_t col_index, size_t start, size_t stop) {
                return self.columns<double>(col_index, start, stop); // Explicit template argument
            },
             /* py::arg("col_index"), py::arg("start"), py::arg("stop"), */
             "Retrieve a slice of a column.")

        .def("standard_deviation", &Toolbox::dfw::DataFrameWrapper<double>::template StandardDeviation<double>,
             py::arg("columnName"),
             "Calculate the standard deviation of a column.")

        .def("mean", &Toolbox::dfw::DataFrameWrapper<double>::template Mean<double>,
             py::arg("columnName"),
             "Calculate the mean of a column.")

        .def("variance", &Toolbox::dfw::DataFrameWrapper<double>::template Variance<double>,
             py::arg("columnName"),
             "Calculate the variance of a column.")

        .def("median", &Toolbox::dfw::DataFrameWrapper<double>::template Median<double>,
             py::arg("columnName"),
             "Calculate the median of a column.")

        .def("correlation", &Toolbox::dfw::DataFrameWrapper<double>::template Correlation<double>,
             py::arg("columnName1"), py::arg("columnName2"),
             "Calculate the correlation between two columns.")

        .def("frequency_count", &Toolbox::dfw::DataFrameWrapper<double>::template frequencyCount<double>,
             py::arg("columnName"),
             "Get the frequency count of a column.")

        .def("classify", &Toolbox::dfw::DataFrameWrapper<double>::template Classify<double>,
             py::arg("columnName1"), py::arg("categories"), py::arg("conditions"),
             "Classify column data based on conditions.")

#ifdef INTERPOLATION_MODULE
        .def("interpolate", &Toolbox::dfw::DataFrameWrapper<double>::template Interpolate<double>,
             py::arg("columnName1"), py::arg("columnName2"), py::arg("categories"), py::arg("conditions"),
             "doubleerpolate column data based on conditions.")
#endif

        .def("get_info", &Toolbox::dfw::DataFrameWrapper<double>::getInfo,
             "Retrieve basic information about the DataFrame.");



/* STRING */
     py::class_<Toolbox::dfw::DataFrameWrapper<std::string>>(m, "DataFrameWrapperStr")
        .def(py::init<>())
        .def(py::init<const char *, const char *>(),
             py::arg("inputFilename"), py::arg("outputFilename"))

        .def_property_readonly("input_filename", 
               [](const Toolbox::dfw::DataFrameWrapper<int> &self) {
                return self.getInputFilename();
            })
        .def_property_readonly("output_filename",
                [](const Toolbox::dfw::DataFrameWrapper<int> &self) {
                return self.getOutputFilename();
            })
        .def_property_readonly("data_dir", 
                [](const Toolbox::dfw::DataFrameWrapper<int> &self) {
                return self.getDataDirectory().string();
                })

        .def("load_and_read_file", &Toolbox::dfw::DataFrameWrapper<std::string>::loadAndReadFile,
             "Load and read the input file.")

        .def("get_col_index", &Toolbox::dfw::DataFrameWrapper<std::string>::getColIndex,
             py::arg("columnName"),
             "Get the index of a column by name.")

        .def("columns_by_name", [](Toolbox::dfw::DataFrameWrapper<std::string> &self, const char *columnName) {
                return self.columns<double>(columnName); // Explicit template argument
            },
            /* py::arg("columnName"), */
            "Retrieve a column by name.")

        .def("columns_by_index",[](Toolbox::dfw::DataFrameWrapper<std::string> &self, size_t col_index) {
                 return self.columns<double>(col_index); // Explicit template argument
            },
           "Retrieve a column by index.")

        .def("columns_by_entry",[](Toolbox::dfw::DataFrameWrapper<std::string> &self, size_t col_index, size_t row_index) {
                return self.columns<double>(col_index, row_index); // Explicit template argument
            },
             /* py::arg("col_index"), py::arg("row_index"), */
             "Retrieve a specific entry in a column.")

        .def("columns_by_slice", [](Toolbox::dfw::DataFrameWrapper<std::string> &self, size_t col_index, size_t start, size_t stop) {
                return self.columns<double>(col_index, start, stop); // Explicit template argument
            },
             /* py::arg("col_index"), py::arg("start"), py::arg("stop"), */
             "Retrieve a slice of a column.")

        .def("standard_deviation", &Toolbox::dfw::DataFrameWrapper<std::string>::template StandardDeviation<double>,
             py::arg("columnName"),
             "Calculate the standard deviation of a column.")

        .def("mean", &Toolbox::dfw::DataFrameWrapper<std::string>::template Mean<double>,
             py::arg("columnName"),
             "Calculate the mean of a column.")

        .def("variance", &Toolbox::dfw::DataFrameWrapper<std::string>::template Variance<double>,
             py::arg("columnName"),
             "Calculate the variance of a column.")

        .def("median", &Toolbox::dfw::DataFrameWrapper<std::string>::template Median<double>,
             py::arg("columnName"),
             "Calculate the median of a column.")

        .def("correlation", &Toolbox::dfw::DataFrameWrapper<std::string>::template Correlation<double>,
             py::arg("columnName1"), py::arg("columnName2"),
             "Calculate the correlation between two columns.")

        .def("frequency_count", &Toolbox::dfw::DataFrameWrapper<std::string>::template frequencyCount<double>,
             py::arg("columnName"),
             "Get the frequency count of a column.")

        .def("classify", &Toolbox::dfw::DataFrameWrapper<std::string>::template Classify<double>,
             py::arg("columnName1"), py::arg("categories"), py::arg("conditions"),
             "Classify column data based on conditions.")

#ifdef INTERPOLATION_MODULE
        .def("interpolate", &Toolbox::dfw::DataFrameWrapper<std::string>::template Interpolate<double>,
             py::arg("columnName1"), py::arg("columnName2"), py::arg("categories"), py::arg("conditions"),
             "Interpolate column data based on conditions.")
#endif

        .def("get_info", &Toolbox::dfw::DataFrameWrapper<std::string>::getInfo,
             "Retrieve basic information about the DataFrame.");
    
 
    py::bind_map<std::unordered_map<std::string, unsigned long>>(m, "UnorderedMap");
}

