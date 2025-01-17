# -*- coding: utf-8 -*-
"""Copy of w_modelslab-1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/199EwuDElIMm0dJsCxtMLWYnOKnLmgIBD
"""

import matplotlib.pyplot as plt
import numpy as np


def quad_model(Time,a,b,c):
        temp = a * (Time**2) + b * Time + c
        return temp


def main():
        a = 0.1
        b = -1
        c = 30
        time_v = np.linspace(0, 10, 50)
        temp_hardcoded = quad_model(time_v,a,b,c)
        plt.plot(time_v, temp_hardcoded, label=f"hardcoded values: {a,b,c}")
        plt.xlabel("time")
        plt.ylabel('temp')
        plt.legend()
        plt.title("weather modeling with user given values and range in QE")
        plt.show()


if __name__ == "__main__":
        main()

import matplotlib.pyplot as plt
import numpy as np
def quad_model(Time,a,b,c1) :
        temp=a*(Time**2)+b*Time+c
        return temp
def main():
        a=float(input("enter the value of a "))
        b=float(input("entr the value of b "))
        c=float(input("enetr the value of c "))
        print("give a time range")
        x=int(input("enter the start range"))
        y=int(input("enter the final range"))
        time_v=np.linspace(x,y,50)
        temp_user=quad_model(time_v,a,b,c)
        plt.plot(time_v,temp_user,label=f"user given values :{a,b,c}")
        plt.xlabel("time")
        plt.ylabel('temp')
        plt.legend()
        plt.title("weather modeling with user given values and range in QE")
        plt.show()
if __name__=="__main__":
        main()

import matplotlib.pyplot as plt
import numpy as np

def quad_model(Time, a, b, c):
    temp = a * (Time**2) + b * Time + c
    return temp

def main():
    with open("morev3.txt", "r") as file:
        lines = file.readlines()
        a, b, c = map(float, lines)

    print(f"Read values: a = {a}, b = {b}, c = {c}")

    print("Give a time range:")
    x = int(input("Enter the start range: "))
    y = int(input("Enter the final range: "))
    time_v = np.linspace(x, y, 50)
    temp_user = [quad_model(t, a, b, c) for t in time_v]

    plt.plot(time_v, temp_user, label=f"file given values:{a,b,c}")
    plt.xlabel("Time")
    plt.ylabel("Temperature")
    plt.legend()
    plt.title("Weather modeling with values given in file and user given range in QE")
    plt.show()

if __name__ == "__main__":
    main()

import matplotlib.pyplot as plt
import numpy as np

def quad_model(Time, coeffs):
    a, b, c = coeffs
    temp = a * (Time**2) + b * Time + c
    return temp

def main():
    # Input coefficients as a set
    set1 = {float(input("Enter the value of 'a': ")), float(input("Enter the value of 'b': ")), float(input("Enter the value of 'c': "))}
    print(set1)
    print("Give a time range:")
    x = float(input("Enter the start range: "))
    y = float(input("Enter the final range: "))

    time_v = np.linspace(x, y, 50)
    temp_user = quad_model(time_v, set1)
    plt.plot(time_v, temp_user, label=f"Set: {set1}")
 81   plt.xlabel("time")
    plt.ylabel("temp")
    plt.legend()
    plt.title("Weather modeling with user given values and range in QE")
    plt.show()

if __name__ == "__main__":
    main()

import matplotlib.pyplot as plt
import numpy as np

def quad_model(Time, coeffs):
    a, b, c = coeffs
    temp = a * (Time**2) + b * Time + c
    return temp

def main():
    num_sets = int(input("Enter the number of coefficient sets: "))
    all_sets = []

    for _ in range(num_sets):
        a = float(input("Enter the value of 'a': "))
        b = float(input("Enter the value of 'b': "))
        c = float(input("Enter the value of 'c': "))
        all_sets.append((a, b, c))

    print("Give a time range:")
    x = float(input("Enter the start range: "))
    y = float(input("Enter the final range: "))

    time_v = np.linspace(x, y, 50)

    plt.figure(figsize=(8, 6))
    for coeffs in all_sets:
        temp_user = quad_model(time_v, coeffs)
        plt.plot(time_v, temp_user, label=f"Set: {coeffs}")

    plt.xlabel("Time")
    plt.ylabel("Temperature")
    plt.legend()
    plt.title("Weather modeling with user given coefficient sets")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()

import matplotlib.pyplot as plt
import numpy as np


def quad_model(Time,a,b,c):
        temp = a * (Time**2) + b * Time + c
        return temp
def quad_model2(Time,a,b,c) :
        temp=a*(Time**2)+b*Time+c
        return temp
def main():
        a = 0.1
        b = -1
        c = 30
        a2=float(input("enter the value of a "))
        b2=float(input("entr the value of b "))
        c2=float(input("enetr the value of c "))
        time_v = np.linspace(0, 10, 50)
        temp_hardcoded = quad_model(time_v,a,b,c)
        plt.plot(time_v, temp_hardcoded, label=f"hardcoded values :{a,b,c}")
        temp_user=quad_model2(time_v,a2,b2,c2)
        plt.plot(time_v,temp_user,label=f"user given values :{a2,b2,c23}")
        plt.xlabel("time")
        plt.ylabel('temp')
        plt.legend()
        plt.title("weather modeling with user given values and range in QE")
        plt.show()


if __name__ == "__main__":
        main()

