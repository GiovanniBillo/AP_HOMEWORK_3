#include "InterpolateWrapper.hpp"

#include <pybind11/pybind11.h>
#include <pybind11/functional.h>
#include <pybind11/stl.h>

namespace py = pybind11;

PYBIND11_MODULE(interpolation_toolbox, m) {
    m.doc() = "Interpolation toolbox using pybind11";  // Module docstring

    // Expose LinearInterpolator
    py::class_<Toolbox::intw::LinearInterpolator<double>>(m, "LinearInterpolator")
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

    /* // Expose LagrangeInterpolator */
    /* py::class_<Toolbox::intw::LagrangeInterpolator<double>>(m, "LagrangeInterpolator") */
    /*     .def(py::init<>())  // Default constructor */
    /*     .def("build", &Toolbox::intw::LagrangeInterpolator<double>::build, */
    /*          py::arg("x"), py::arg("y"), py::arg("n"), py::arg("a"), py::arg("b"), */
    /*          "Build the Lagrange interpolator with given x, y, n, a, and b") */
    /*     .def("build_equidistant", &Toolbox::intw::LagrangeInterpolator<double>::buildEquidistant, */
    /*          py::arg("x"), py::arg("y"), py::arg("n"), py::arg("a"), py::arg("b"), */
    /*          "Build the equidistant Lagrange interpolator") */
    /*     .def("build_chebyshev", &Toolbox::intw::LagrangeInterpolator<double>::buildChebyshev, */
    /*          py::arg("x"), py::arg("y"), py::arg("n"), py::arg("a"), py::arg("b"), */
    /*          "Build the Chebyshev Lagrange interpolator") */
    /*     .def("error", &Toolbox::intw::LagrangeInterpolator<double>::Error, */
    /*          py::arg("f"), py::arg("a"), py::arg("b"), */
    /*          "Calculate the error of the interpolation for a given function f over [a, b]") */
    /*     .def("__call__", &Toolbox::intw::LagrangeInterpolator<double>::operator(), */
    /*          py::arg("t"), */
    /*          "Evaluate the interpolator at point t"); */
}

