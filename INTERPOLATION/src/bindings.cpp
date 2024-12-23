#include "InterpolateWrapper.hpp"

#include <pybind11/pybind11.h>
#include <pybind11/functional.h>
#include <pybind11/stl.h>

namespace py = pybind11;

PYBIND11_MODULE(InterpolateWrapper, m) {
    m.doc() = "Interpolation toolbox using pybind11";  // Module docstring
    // Base class: Interpolator
    py::class_<Toolbox::intw::Interpolator<double>>(m, "Interpolator")
        .def("__call__", &Toolbox::intw::Interpolator<double>::operator())
        .def("plotError", [](Toolbox::intw::Interpolator<double>& self, 
                    py::function vector_generating_function,
                    py::function y_map_function,
                    py::function plot_function,
                    double lb, double ub, int max_points, 
                    const std::string& methodName){
             // Placeholder implementation
             std::cout << "Lambda placeholder for plotError called with methodName: " << methodName << std::endl;
             },
             "Base plotError shared across all derived classes");

    // Expose LinearInterpolator
    py::class_<Toolbox::intw::LinearInterpolator<double>, Toolbox::intw::Interpolator<double>>(m, "LinearInterpolator")
        .def(py::init<>())  // Default constructor
        .def("build", &Toolbox::intw::LinearInterpolator<double>::build,
             py::arg("x"), py::arg("y"), py::arg("n"), py::arg("a"), py::arg("b"),
             "Build the linear interpolator with given x, y, n, a, and b")
        .def("error", &Toolbox::intw::LinearInterpolator<double>::Error,
             py::arg("f"), py::arg("a"), py::arg("b"),
             "Calculate the error of the interpolation for a given function f over [a, b]")
        .def("__call__", &Toolbox::intw::LinearInterpolator<double>::operator(),
             py::arg("t"),
             "Evaluate the interpolator at point t");
    // Expose LagrangeInterpolator
    py::class_<Toolbox::intw::LagrangeInterpolator<double>, Toolbox::intw::Interpolator<double>>(m, "LagrangeInterpolator")
        .def(py::init<>())  // Default constructor
        .def("build", &Toolbox::intw::LagrangeInterpolator<double>::build,
             py::arg("x"), py::arg("y"), py::arg("n"), py::arg("a"), py::arg("b"),
             "Build the linear interpolator with given x, y, n, a, and b")
        .def("error", &Toolbox::intw::LagrangeInterpolator<double>::Error,
             py::arg("f"), py::arg("a"), py::arg("b"),
             "Calculate the error of the interpolation for a given function f over [a, b]")
        .def("__call__", &Toolbox::intw::LagrangeInterpolator<double>::operator(),
             py::arg("t"),
             "Evaluate the interpolator at point t");
    // Expose SplineInterpolator
    py::class_<Toolbox::intw::SplineInterpolator<double>, Toolbox::intw::Interpolator<double>>(m, "SplineInterpolator")
        .def(py::init<>())  // Default constructor
        .def("build", &Toolbox::intw::SplineInterpolator<double>::build,
             py::arg("x"), py::arg("y"), py::arg("n"), py::arg("a"), py::arg("b"),
             "Build the linear interpolator with given x, y, n, a, and b")
        .def("error", &Toolbox::intw::SplineInterpolator<double>::Error,
             py::arg("f"), py::arg("a"), py::arg("b"),
             "Calculate the error of the interpolation for a given function f over [a, b]")
        .def("__call__", &Toolbox::intw::SplineInterpolator<double>::operator(),
             py::arg("t"),
             "Evaluate the interpolator at point t");
    }

