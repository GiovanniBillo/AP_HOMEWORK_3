# Profiling report 

## Overview
This document provides guidance on profiling the project to identify performance bottlenecks.

## Tools Used
- `valgrind`: For memory profiling and cache analysis.

If built with -DCMAKE_BUILD_TYPE=Debug, all C++ code automatically enables the -pg flag for profiling.

## Profiling with `valgrind`
```bash (example with main_stats)
valgrind --tool=callgrind ./main_stats
kcachegrind callgrind.out
```
By profiling the code, there seemed to be a significant bottleneck when importing data that wasn't already formated as expected by the DataFrame library.
This resulted in implemented libraries like pandas being almost 15 times faster than our implementation. 
The main reason for this overhead was this:

[Kcache grind report (unoptimized)](kcache_grind_unoptimized.pdf)

The CSVparser::parse module called a function to update the column type at each row entry, resulting in an enormous waste of time expecially for large datasets (see the example in `comparison.py`).
To reduce this bottleneck then, we restricted this operation (needed to provide the correctly formatted file, but redundant as it was implemented) to the first 10 rows of the dataset.
This significantly reduced the execution time for our package, both in C++ directly and python.

[Kcache grind report (after optimization)](kcache_grind_grapth_optimized.pdf)

One can see the drastic reduction in calls for UpdateColumnType from CSVparser::parse (first 2 circles): before it was almost 10 times as much.


