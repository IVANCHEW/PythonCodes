from plotting import *

#To plot a bar chart, uncomment the line below
#barchart([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], 5)

#To plot a differential equation, uncomment the lines below
import math
from udacityplots import *

@show_plot
def simple():
    x_data = numpy.linspace(0., 100., 1000)

    for x in x_data:
        y = x**2
        matplotlib.pyplot.scatter(x, y)

    axes = matplotlib.pyplot.gca()
    axes.set_xlabel('x')
    axes.set_ylabel('y')

simple()

#See following link for tutorial:
#https://www.udacity.com/wiki/plotting-graphs-with-python
