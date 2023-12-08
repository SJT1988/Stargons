'''
Program for drawing and saving stargons with 'a' points,
connecting every 'b' points clockwise,
lying on a circle with radius 'r'.

Can be used to quickly generate cases.
First commit by Spencer Trumbore on December 07, 2023.
'''

import os
import math
import matplotlib.pyplot as plt
pi = math.pi

def generate_points(a, radius):
    lst = []
    for i in range(a):
        point = (radius*math.cos(i*2*math.pi/a), radius*math.sin(i*2*math.pi/a))
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

def save_stargon(a,b,r):
    points = generate_points(a,r)
    ordered_points = order_points(b%a, points)
    plt.rcParams["figure.figsize"] = [5.00, 5.00]
    plt.rcParams["figure.autolayout"] = True

    ordered_points.append(ordered_points[0])
    x_vals = [point[0] for point in ordered_points]
    y_vals = [point[1] for point in ordered_points]

    plt.plot(x_vals, y_vals, 'bo', linestyle="-")

    path = str(os.getcwd())
    subfolder = "\\a={}".format(n)
    if not os.path.exists(path+subfolder):
        os.makedirs(path+subfolder)

    dir = os.getcwd()
    #plt.savefig(path+subfolder+"\\a={}_b={}".format(a,b))
    digitsofa = len(str(a))
    plt.savefig(path+subfolder+f"\\{a}_{b:0{digitsofa}}")
    plt.close()
    return

def draw_stargon(a,b,r):
    points = generate_points(a,r)
    ordered_points = order_points(b%a, points)
    plt.rcParams["figure.figsize"] = [5.00, 5.00]
    plt.rcParams["figure.autolayout"] = True

    ordered_points.append(ordered_points[0])
    x_vals = [point[0] for point in ordered_points]
    y_vals = [point[1] for point in ordered_points]

    plt.plot(x_vals, y_vals, 'bo', linestyle="-")
    plt.show()
    plt.close()
    return

n = 15
for k in range(n+1):
    save_stargon(n,k,1)

#draw_stargon(5,2,1)