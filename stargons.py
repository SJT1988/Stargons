'''
Program for drawing and saving stargons with 'a' points,
connecting every 'b' points counter-clockwise.
Can be used to quickly generate and compare cases.
First commit by Spencer Trumbore on December 07, 2023.
'''

import os
import math
import matplotlib.pyplot as plt
pi = math.pi

def generate_points(a):
    lst = []
    for i in range(a):
        point = (math.cos(i*2*math.pi/a), math.sin(i*2*math.pi/a))
        lst.append(point)
    return lst

def order_points(b,pts):
    ordered_lst = []
    ordered_lst.append(pts[0])
    i=b
    a = len(pts)
    while i != 0:
        ordered_lst.append(pts[i])
        i = (i + b)%a
    return ordered_lst

def save_stargon(a,b):
    points = generate_points(a)
    ordered_points = order_points(b%a, points)

    # Plot settings
    plt.rcParams["figure.figsize"] = [6.00, 6.00]
    plt.rc('font', size=15)
    plt.tight_layout(pad=.5) # increases padding
    plt.axis('off')

    # All points
    p_x = [point[0] for point in points]
    p_y = [point[1] for point in points]
    plt.plot(p_x, p_y, 'o', color='black')
    for i in range(a):
        plt.text(p_x[i]*1.15,
                 p_y[i]*1.15,
                 f'({i})',
                 ha='center',
                 va='center',
                 color = ('red' if i == b%a else 'blue'))

    # Connect ordered points
    ordered_points.append(ordered_points[0])
    op_x = [point[0] for point in ordered_points]
    op_y = [point[1] for point in ordered_points]
    plt.plot(op_x, op_y, 'bo', linestyle="-")
    plt.plot(op_x, op_y, 'ro')
    

    path = str(os.getcwd())
    subfolder = "\\a={}".format(n)
    if not os.path.exists(path+subfolder):
        os.makedirs(path+subfolder)

    digitsofa = len(str(a))
    plt.savefig(path+subfolder+f"\\{a}_{b:0{digitsofa}}")
    plt.close()
    return

def draw_stargon(a,b):
    points = generate_points(a)
    ordered_points = order_points(b%a, points)

    # Plot settings
    plt.rcParams["figure.figsize"] = [6.00, 6.00]
    plt.rc('font', size=15)
    plt.tight_layout(pad=.5) # increases padding
    plt.axis('off')

    # All points
    p_x = [point[0] for point in points]
    p_y = [point[1] for point in points]
    for i in range(a):
        plt.text(p_x[i]*1.15,
                 p_y[i]*1.15,
                 f'({i})',
                 ha='center',
                 va='center',
                 color = ('red' if i == b%a else 'blue'))

    # Connect ordered points
    ordered_points.append(ordered_points[0])
    op_x = [point[0] for point in ordered_points]
    op_y = [point[1] for point in ordered_points]
    plt.plot(op_x, op_y, 'bo', linestyle="-")
    plt.plot(op_x, op_y, 'ro')
    plt.show()
    return

n = 12
for k in range(n+1):
    save_stargon(n,k)