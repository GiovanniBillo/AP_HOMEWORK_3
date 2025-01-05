set terminal pngcairo size 800,600
set output 'error_plot_Cubicspline.png'
set xlabel 'Number of Points (n)'
set ylabel 'Error'
set title 'Error vs Number of Points (Cubicspline)'
plot 'error_data_Cubicspline.dat' using 1:2 with linespoints title 'Error'
