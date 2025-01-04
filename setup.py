import os
import sys
import subprocess

from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext

# A CMakeExtension needs a sourcedir instead of a file list.
# The name must be the _single_ output extension from the CMake build.
# If you need multiple extensions, see scikit-build.
class CMakeExtension(Extension):
    def __init__(self, name, sourcedir=""):
        Extension.__init__(self, name, sources=[])
        self.sourcedir = os.path.abspath(sourcedir)


class CMakeBuild(build_ext):
    def build_extension(self, ext):
        package_dir = os.path.join(os.path.dirname(__file__), "ToolBox")
        extdir = os.path.abspath(package_dir)

        # extdir = os.path.abspath(os.path.dirname(self.get_ext_fullpath(ext.name)))

        # required for auto-detection of auxiliary "native" libs
        if not extdir.endswith(os.path.sep):
            extdir += os.path.sep

        cfg = "Debug" if self.debug else "Release"

        # CMake lets you override the generator - we need to check this.
        # Can be set with Conda-Build, for example.
        cmake_generator = os.environ.get("CMAKE_GENERATOR", "")

        # Set Python_EXECUTABLE instead if you use PYBIND11_FINDPYTHON
        cmake_args = [
            "-DCMAKE_LIBRARY_OUTPUT_DIRECTORY={}".format(extdir),
            "-DPYTHON_EXECUTABLE={}".format(sys.executable),
            "-DCMAKE_BUILD_TYPE={}".format(cfg),  # not used on MSVC, but no harm
        ]

        if "CMAKE_ARGS" in os.environ:
            cmake_args += [item for item in os.environ["CMAKE_ARGS"].split(" ") if item]
        if os.getenv("INTERPOLATION_MODULE") == "ON":
            cmake_args.append("-DINTERPOLATION_MODULE=ON")
        build_args = []

        # Set CMAKE_BUILD_PARALLEL_LEVEL to control the parallel build level
        # across all generators.
        if "CMAKE_BUILD_PARALLEL_LEVEL" not in os.environ:
            # self.parallel is a Python 3 only way to set parallel jobs by hand
            # using -j in the build_ext call, not supported by pip or PyPA-build.
            if hasattr(self, "parallel") and self.parallel:
                # CMake 3.12+ only.
                build_args += ["-j{}".format(self.parallel)]

        if not os.path.exists(self.build_temp):
            os.makedirs(self.build_temp)
        # Create a unique build directory for each extension

        build_temp = os.path.join(self.build_temp, ext.name.replace(".", "_"))
        os.makedirs(build_temp, exist_ok=True)

        subprocess.check_call(
            ["cmake", ext.sourcedir] + cmake_args, cwd=build_temp
        )
        subprocess.check_call(
            ["cmake", "--build", "."] + build_args, cwd=build_temp
        )
        
        # Ensure proper package structure for shared libraries
        lib_output_dir = os.path.join(extdir, "ToolBox")
        os.makedirs(lib_output_dir, exist_ok=True)
        self._copy_shared_libraries(lib_output_dir)


    def _copy_shared_libraries(self, lib_output_dir):
        # Move all shared libraries to the ToolBox/ directory
        for root, _, files in os.walk(self.build_temp):
            for file in files:
                if file.endswith(".so"):
                    src_path = os.path.join(root, file)
                    dst_path = os.path.join(lib_output_dir, file)
                    os.rename(src_path, dst_path)
                    print(f"Moved {src_path} -> {dst_path}")




# The information here can also be placed in setup.cfg - better separation of
# logic and declaration, and simpler if you include description/version in a file.
setup(
    name="ToolBox",
    version="0.0.1",
    description="A DataFrame wrapper integration for python",
    long_description="",
    ext_modules=[CMakeExtension("DataFrameWrapper", sourcedir="STATISTICS"),
                 CMakeExtension("InterpolateWrapper", sourcedir="INTERPOLATION")
                 ],
    cmdclass={"build_ext": CMakeBuild},
    packages=["ToolBox"],
    package_dir={"ToolBox": "ToolBox"},
    zip_safe=False,
)
