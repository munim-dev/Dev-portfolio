#the goal of this excercise is to help me re-learn functions again in python starting with this simple unit convertor

import math #to convert RPM to radians /s

#the problem is the user has to write exactly what written in the options ill try to come back later and find a solution if i do not forget

convert = input("please state which unit of convertion you want mtr,mmtr,kel,rs:  ")

#defining all needed functions 
def mmtr_to_mtr(in_mmtr):
    mtr=in_mmtr*1000
    return mtr

def mtr_to_mmtr(in_mtr):
    mmtr=in_mtr/1000
    return mmtr

def cel_to_kel(in_cel):
    kel=in_cel+273.15
    return kel

def rpm_to_rs(in_rpm):
    rs=in_rpm*(math.pi * 2)/60
    return rs

#all if statements according to the user convertion needs :)

if convert == "mtr":
    mmtr = int(input("what the unit of millimeters : "))
    print("the unit of meters is: ", mmtr_to_mtr(mmtr))

if convert == "mmtr":
    mtr = int(input("what the unit of meters : "))
    print("the unit of millimeters is: ", mtr_to_mmtr(mtr))

if convert == "kel":
    cel = int(input("what the unit of celcius : "))
    print("the unit of kelvin is: ", cel_to_kel(cel))

if convert == "rs":
    rpm = int(input("what the unit of rpm : "))
    print("the unit of r/s is: ", rpm_to_rs(rpm))



