#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/stl_bind.h>
#include "DataFrameWrapper.hpp"

namespace py = pybind11;

PYBIND11_MODULE(dataframe_wrapper, m) {
    m.doc() = "Python bindings for DataFrameWrapper";

    py::class_<Toolbox::dfw::DataFrameWrapper<double>>(m, "DataFrameWrapper")
        .def(py::init<>())
        .def(py::init<const char *, const char *>(),
             py::arg("inputFilename"), py::arg("outputFilename"))

        .def("load_and_read_file", &Toolbox::dfw::DataFrameWrapper<double>::loadAndReadFile,
             "Load and read the input file.")

        .def("get_col_index", &Toolbox::dfw::DataFrameWrapper<double>::getColIndex,
             py::arg("columnName"),
             "Get the index of a column by name.")

        /* .def("columns_by_name", &Toolbox::dfw::DataFrameWrapper<double>::columns<double>, */
        /*      py::arg("columnName"), */
        /*      "Retrieve a column by name."); */

        /* .def("columns_by_index", &Toolbox::dfw::DataFrameWrapper<double>::template columns<double>, */
        /*      py::arg("col_index"), */
        /*      "Retrieve a column by index.") */

        /* .def("columns_by_entry", &Toolbox::dfw::DataFrameWrapper<double>::template columns<double>, */
        /*      py::arg("col_index"), py::arg("row_index"), */
        /*      "Retrieve a specific entry in a column.") */

        /* .def("columns_by_slice", &Toolbox::dfw::DataFrameWrapper<double>::template columns<double>, */
        /*      py::arg("col_index"), py::arg("start"), py::arg("stop"), */
        /*      "Retrieve a slice of a column.") */

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
             "Interpolate column data based on conditions.")
#endif

        .def("get_info", &Toolbox::dfw::DataFrameWrapper<double>::getInfo,
             "Retrieve basic information about the DataFrame.");

    py::bind_map<std::unordered_map<std::string, unsigned long>>(m, "UnorderedMap");
}

