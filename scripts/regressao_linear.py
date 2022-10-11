from matplotlib.animation import FuncAnimation
import numpy
from pandas import *
import matplotlib.pyplot as p
from matplotlib.animation import FuncAnimation

# lê os dados
filepath = "data.txt"
data = read_csv(filepath, names=["index", "x", "y"], dtype={'index': int, 'x': float, 'y': float}, delim_whitespace=True)

def h(x, teta_0, teta_1) :
    return teta_0 + teta_1 * x

def minimize(data, teta_0, teta_1, alpha) :
    gradient_teta_0 = 0.0
    gradient_teta_1 = 0.0
    n = len(data)
    for i in range(n) :
        row = data.loc[i]
        x = row.at['x']
        y = row.at['y']
        gradient_teta_0 += h(x, teta_0, teta_1) - y
        gradient_teta_1 += (h(x, teta_0, teta_1) - y) * x
    gradient_teta_0 /= n
    new_teta_0 = teta_0 - gradient_teta_0 * alpha
    gradient_teta_1 /= n
    new_teta_1 = teta_1 - gradient_teta_1 * alpha
    return new_teta_0, new_teta_1

def get_values_plot() :
    data_len = len(data)
    x_axis = [data.loc[i].at['x'] for i in range(data_len)]
    y_axis = [data.loc[i].at['y'] for i in range(data_len)]
    return x_axis, y_axis

def get_line_plot(teta_0, teta_1) :
    x_axis = [0, data['x'].max()]
    y_axis = [h(i, teta_0, teta_1) for i in x_axis]
    return x_axis, y_axis

# define alpha, teta0 e teta1
alpha = .001
teta_0 = numpy.random.random()
teta_1 = numpy.random.random()

# plota pontos e linha
p.ion()
fig = p.figure()
ax = fig.add_subplot(111)
values_x, values_y = get_values_plot()
values, = ax.plot(values_x, values_y, 'ro')
line_x, line_y = get_line_plot(teta_0, teta_1)
line, = ax.plot(line_x, line_y)
    
for i in range(1000) :
    # atualiza teta0 e teta1
    resulting_teta_0, resulting_teta_1 = minimize(data, teta_0, teta_1, alpha)
    teta_0 = resulting_teta_0
    teta_1 = resulting_teta_1

    # printa teta0 e teta1
    print(teta_0, teta_1)
    
    # atualiza a linha
    new_xvalues, new_yvalues = get_line_plot(teta_0, teta_1)
    line.set_ydata(new_yvalues)
    fig.canvas.draw()
    fig.canvas.flush_events()