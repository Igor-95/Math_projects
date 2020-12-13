import numpy as np
import matplotlib.pyplot as plt
import tkinter.font as font
from tkinter import *


window = Tk()

class GetEntry():
    def __init__(self, window):
        width = 5
        self.window=window
        self.entry_contents1=0
        self.entry_contents2=0
        self.entry_contents3=0
        self.entry_contents4=0
        self.entry_contents5=0
        self.entry_contents6=0

        self.e1 = Entry(window, width=width, font=18)
        self.e1.insert(0, 0)
        self.e1.grid(row=0, column=1)
        self.e1.focus_set()
        self.e2 = Entry(window, width=width, font=18)
        self.e2.insert(0, 0)
        self.e2.grid(row=0, column=3)
        self.e2.focus_set()
        self.e3 = Entry(window, width=width, font=18)
        self.e3.insert(0, 0)
        self.e3.grid(row=0, column=5)
        self.e3.focus_set()
        self.e4 = Entry(window, width=width, font=18)
        self.e4.insert(0, 0)
        self.e4.grid(row=1, column=1)
        self.e4.focus_set()
        self.e5 = Entry(window, width=width, font=18)
        self.e5.insert(0, 0)
        self.e5.grid(row=1, column=3)
        self.e5.focus_set()
        self.e6 = Entry(window, width=width, font=18)
        self.e6.insert(0, 0)
        self.e6.grid(row=1, column=5)
        self.e6.focus_set()


        Button(window, text="get", width=10, font=18,
               command=self.callback).grid(row=10, column=0)

    def callback(self):
        """ get the contents of the Entry
        """
        self.entry_contents1=self.e1.get()
        self.entry_contents2=self.e2.get()
        self.entry_contents3=self.e3.get()
        self.entry_contents4=self.e4.get()
        self.entry_contents5=self.e5.get()
        self.entry_contents6=self.e6.get()


window.geometry("450x180")
window.title("input functions")
GE=GetEntry(window)

def close_window():
    window.destroy()
    exit


Button(window, text="run", width=10, font=18,
               command=close_window).grid(row=11, column=0)

Label(window, text="1. function: ", font=(18)).grid(row=0)
Label(window, text="2. function: ", font=(18)).grid(row=1)
Label(window, text="x² ", font=(22)).grid(row=0, column=2)
Label(window, text="x² ", font=(22)).grid(row=1, column=2)
Label(window, text="x ", font=(22)).grid(row=0, column=4)
Label(window, text="x ", font=(22)).grid(row=1, column=4)
Label(window, text="const", font=(22)).grid(row=0, column=6)
Label(window, text="const", font=(22)).grid(row=1, column=6)
Label(window, text="use . as decimal seperation", font=(22)).grid(row=12, column=0)

window.mainloop()

a1, a2, a3 = float(GE.entry_contents1), float(GE.entry_contents2), float(GE.entry_contents3)   # a1*x² + a2*x + a3, quadratic 1. function
a4, a5, a6 = float(GE.entry_contents4), float(GE.entry_contents5), float(GE.entry_contents6)    # a4*x² + a5*x + a6, quadratic 2. function
exp1, exp2, exp3 = 2, 1, 0

"""
plots the desired function
"""
def sqr_func(a, k1, k2, k3):
    y = ((k1*a**exp1) + (k2*a**exp2) + (k3*a**exp3))
    return (y) 


"""
calculates the interception between an quadtratic funktion and the x-axis .
if the quadratic functions only intercept in 1 point the pq-formula is reduced to a linear solving model. 
"""
def pq_formular(k1, k2 , k3):
    if k1 != 0:
        p, q = k2/k1, k3/k1
        try:
            O1 = -(p/2) + (((p/2)**2) - q)**(1/2)
            O2 = -(p/2) - (((p/2)**2) - q)**(1/2)
            if isinstance(O1, complex) and isinstance(O2, complex):
                return ([np.NaN, np.NaN])
            elif isinstance(O1, complex):
                return ([np.NaN, O2])
            elif isinstance(O2, complex):
                return ([O1, np.NaN])
            else:
                return([O1, O2])

        except ValueError:
            O1 = np.NaN
            O2 = np.NaN
            return ([O1, O2])
    else:
        try:
            p, q = k2, k3
            x = -(q/p)
            return([x])
        except ZeroDivisionError:
            return([np.NaN])

"""
the size function determines the outer bounds of the plot. if the x-axis interception is beyond the x = {-10 to 10} realm it gets adjusted.
"""
def size(list):
    size = 0
    for a in list:
        if isinstance(a, bool) == True:
            size is None
        elif abs(a) > size:
            size = abs(a)
        else:
            continue
    return (size)


"""
calculates the 1. derivative of the desired quadratic function
"""
def derivativ_1(a, k1, k2, k3):
    y = k1*a**exp1_1 + k2*a**exp2_1 + k3*a**exp3_1
    return (y)

"""
calculates the interception between a linear function and the x-axis 
"""
def der_1_zero(m, b):
    try:
        zero = -b / m
        if m < 0:
            ex_str = "maximum"
        elif m > 0:
            ex_str = "minimum"
        else:
            ex_str = ""
        return (zero, 0, ex_str)
    except ZeroDivisionError:
        return(np.NaN, np.NaN, "")

"""
calculates the 1. derivative of the desired function. returns its coeffizients 
"""
def koeff_derivativ(k1, k2, k3):
    koeff1, exp1_1 = k1 * exp1, exp1-1
    koeff2, exp2_1 = k2 * exp2, exp2-1
    koeff3, exp3_1 = k3 * exp3, exp3
    return(koeff1, koeff2, koeff3, exp1_1, exp2_1, exp3_1)


def intercept_sqr_func(p1_k1, p1_k2, p1_k3, p2_k1, p2_k2, p2_k3):
    if a1 or a4 != 0:
        k1 = p1_k1 - p2_k1
        k2 = p1_k2 - p2_k2
        k3 = p1_k3 - p2_k3
        x_cord = pq_formular(k1=k1, k2=k2, k3=k3)
        y_cord_quadratic = []
        for a in x_cord:
            y_cord_quadratic.append(sqr_func(a=a, k1=a1, k2=a2, k3=a3))
        return (x_cord, y_cord_quadratic)
    elif a2 or a5 != 0:
        try:    
            k2 = p1_k2 - p2_k2
            k3 = p1_k3 - p2_k3
            x_cord = []
            x_cord.append(-k3/k2)
            y_cord_quadratic = []
            y_cord_quadratic.append(sqr_func(a=x_cord[0], k1=a1, k2=a2, k3=a3))
            return(x_cord, y_cord_quadratic)
        except ZeroDivisionError:
            return([np.NaN], [np.NaN])
    else:
        return ([np.NaN], [np.NaN])


def label_str(k1):
    if k1 != 0:
        label = "quadratic function"
    else:
        label = "linear function"
    return(label)


"""
the new exponents and coefficient are computed from both motherfunctions. the exponents are redundand.
"""
a1_1, a2_1, a3_1, exp1_1, exp2_1, exp3_1 = koeff_derivativ(k1=a1, k2=a2, k3=a3)
a4_1, a5_1, a6_1, exp1_1, exp2_1, exp3_1 = koeff_derivativ(k1=a4, k2=a5, k3=a6)

""" 
the pq_formular function computes the x-axis interception of both motherfunctions given.
it detectes if the first coefficient is 0, resulting in a linear function wich is unable to pass the pq-formular.
"""
if a1 != 0:
    Zero_value1_1, Zero1_1 = pq_formular(k1=a1, k2=a2, k3=a3), [0, 0]
else:
    Zero_value1_1, Zero1_1 = pq_formular(k1=a1, k2=a2, k3=a3), [0]

if a4 != 0:
    Zero_value2_1, Zero2_1 = pq_formular(k1=a4, k2=a5, k3=a6), [0, 0]
else:
    Zero_value2_1, Zero2_1 = pq_formular(k1=a4, k2=a5, k3=a6), [0]

""" 
 if the first derivative of the motherfunction would be a liner funktion with a slope unequal to 0, the if statement computes the x-axis interception of the first derivative.
 else the motherfunction is treated as an liner function itself and the x-axis interception is computed.
"""
if a1 != 0:
    Zero_value1_2, Zero1_2, ex_str1,  = der_1_zero(m=a1_1, b=a2_1)
    Zero_yvalue1_1 = sqr_func(a=Zero_value1_2, k1=a1, k2=a2, k3=a3)
else:
    Zero_value1_2, Zero1_2, ex_str1 = der_1_zero(m=a2, b=a3)

if a4 != 0:
    Zero_value2_2, Zero2_2, ex_str2 = der_1_zero(m=a4_1, b=a5_1)
    Zero_yvalue2_1 = sqr_func(a=Zero_value2_2, k1=a4, k2=a5, k3=a6)
else:
    Zero_value2_2, Zero2_2, ex_str2 = der_1_zero(m=a5, b=a6)


""" 
calculates the interception between both motherfunctions
"""
x_inter, y_inter = intercept_sqr_func(p1_k1=a1, p1_k2=a2, p1_k3=a3, p2_k1=a4, p2_k2=a5, p2_k3=a6)

"""
determines the outer bounds of the plot
"""
size_x, size_x1, size_x_inter = size(list=Zero_value1_1), size(list=Zero_value2_1), size(list=x_inter)
if size_x1 > size_x:
    if size_x1 > size_x_inter:
        size_x = size_x1
    else:
        size_x = size_x_inter
elif size_x_inter > size_x:
    size_x = size_x_inter

if size_x > 10:
    x = np.linspace(start=-size_x-1, stop=size_x+1, num=100_000)
else:
    x = np.linspace(start=-10, stop=10, num=100_000)


"""
here the plotting is happening 
"""
y1_1_list, y1_2_list, y1_3_list = [], [], []
y2_1_list, y2_2_list, y2_3_list = [], [], []

for a in x:
    if a1 + a2 == 0:
        y1_1_list.append(np.NaN)
        y1_2_list.append(np.NaN)
    else:
        y = sqr_func(a=a, k1=a1, k2=a2, k3=a3)
        y1_1_list.append(y)
        y = derivativ_1(a=a, k1=a1_1, k2=a2_1, k3=a3_1)
        y1_2_list.append(y)

for a in x:
    if a4 + a5 == 0:
        y2_1_list.append(np.NaN)
        y2_2_list.append(np.NaN)
    else:
        y = sqr_func(a=a, k1=a4, k2=a5, k3=a6)
        y2_1_list.append(y)
        y = derivativ_1(a=a, k1=a4_1, k2=a5_1, k3=a6_1)
        y2_2_list.append(y)

label_1, label_2 = label_str(k1=a1), label_str(k1=a4)

plt.rcParams.update({'font.size': 14})

"""
plots the 1. function, its derivative, the x-axis interception points and the maximum/minimum of that function
"""
if a1 or a2 != 0:
    plt.plot(x, y1_1_list, color="b", label=f"1. function, type: {label_1}")
    plt.plot(x, y1_2_list, color="dodgerblue", label=f"1. function, 1. derivative")

if Zero_value1_1[0] is np.NaN and a1 != 0:
    textstr = "no x-axis interception"
    plt.text(-5,5, textstr, fontsize=15, color="royalblue")
    plt.plot(Zero_value1_2, Zero1_2, ".", color="green")
    plt.plot(Zero_value1_2, Zero_yvalue1_1, ".", color="green", label=f"1. function, {ex_str1}, x={round(Zero_value1_2, 3)}, y={round(Zero_yvalue1_1, 3)}")
elif Zero_value1_1[0] is not np.NaN and a1 != 0:
    plt.plot(Zero_value1_1, Zero1_1, ".", color="r", label=f"1. function x-axis interception: {round(Zero_value1_1[0], 3)} // {round(Zero_value1_1[-1], 3)}")
    plt.plot(Zero_value1_2, Zero1_2, ".", color="green")
    plt.plot(Zero_value1_2, Zero_yvalue1_1, ".", color="green", label=f"1. function, {ex_str1}, x={round(Zero_value1_2, 3)}, y={round(Zero_yvalue1_1, 3)}",)
elif Zero_value1_1[0] is not np.NaN and a1 == 0:
    plt.plot(Zero_value1_1, Zero1_1, ".", color="r", label=f"1. function x-axis interception: {round(Zero_value1_1[0], 3)}")
elif Zero_value1_1[0] is np.NaN and a2 != 0:
    plt.plot(Zero_value1_2, Zero1_2, ".", color="green")
else:
    textstr = "No valid function given"
    plt.text(-5,5, textstr, fontsize=15, color="royalblue")


"""
plots the 2. function, its derivative, the x-axis interception points and the maximum/minimum of that function
"""
if a4 or a5 != 0:
    plt.plot(x, y2_1_list, color="darkorange", label=f"2. function, type: {label_2}")
    plt.plot(x, y2_2_list, color="orange", label=f"2. function, 1. derivative of")

if Zero_value2_1[0] is np.NaN and a4 != 0:
    textstr = "no x-axis interception"
    plt.text(1.5,5, textstr, fontsize=15, color="darkorange")
    plt.plot(Zero_value2_2, Zero2_2, ".", color="green")
    plt.plot(Zero_value2_2, Zero_yvalue2_1, ".", color="green", label=f"2. function, {ex_str2}, x={round(Zero_value2_2, 3)}, y={round(Zero_yvalue2_1, 3)}")
elif Zero_value2_1[0] is not np.NaN and a4 != 0:
    plt.plot(Zero_value2_1, Zero2_1, ".", color="r", label=f"2. function x-axis interception: {round(Zero_value2_1[0], 3)} // {round(Zero_value2_1[-1], 3)}")
    plt.plot(Zero_value2_2, Zero2_2, ".", color="green")
    plt.plot(Zero_value2_2, Zero_yvalue2_1, ".", color="green", label=f"2. function, {ex_str2}, x={round(Zero_value2_2, 3)}, y={round(Zero_yvalue2_1, 3)}")
elif Zero_value2_1[0] is not np.NaN and a4 == 0:
    plt.plot(Zero_value2_1, Zero2_1, ".", color="r")
elif Zero_value2_1[0] is np.NaN and a2 != 0:
    plt.plot(Zero_value2_2, Zero2_2, ".", color="green")
else:
    textstr = "No valid function given"
    plt.text(1.5,5, textstr, fontsize=15, color="forestgreen")

if size_x > 5:
    plt.xlim(-size_x-2, size_x+2)
else:
    plt.xlim(-10, 10)
if a1 == 0:
    if a2 == 0:
        if a4 == 0:
            if a5 == 0:
                plt.ylim(-10, 10)


"""
plots the interception between both functions, if the first two coefficients of the functions are 0, nothing happens
"""
if a1 + a2 == 0:
    "nothing"
elif a4 + a5 == 0:
    "nothing"
elif x_inter[0] and x_inter[-1] is np.NaN:
    textstr = "no function interception"
    plt.text(1,-5, textstr, fontsize=15, color="k")
elif x_inter[0] == x_inter[-1]:
    plt.plot(x_inter, y_inter, ".", color="k", label=f"interception 1: x={round(x_inter[0], 3)} / y={round(y_inter[0], 3)}")
else:
    plt.plot(x_inter[0], y_inter[0], ".", color="k", label=f"interception 1: x={round(x_inter[0], 3)} / y={round(y_inter[0], 3)}")
    plt.plot(x_inter[-1], y_inter[-1], ".", color="k", label=f"interception 2: x={round(x_inter[-1], 3)} / y={round(y_inter[-1], 3)}")

plt.grid(which="major", color="k")
plt.title("Quadratic functions differential analysis")
plt.legend(loc="upper center")
plt.show()
