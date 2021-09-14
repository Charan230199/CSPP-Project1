"""Implementing the wc shell command in python."""

"""the import statement import sys from python module along with the function of lib.sys"""
import sys

"""from lib.helper module we are importing the built in function wc and readfile"""
from lib.helper import wc, readfile

"""None ype value is assigned into variable TEXT"""
TEXT = None

"""ARG_CNT is a variable it is assigned with int value len(sys.argv)-1 len() function gives the len of given input"""
ARG_CNT = len(sys.argv) - 1

"""if the condition ARG_CNT ==0 is true then that condition will execute and reads the input standard input function"""
if ARG_CNT == 0:
    TEXT = sys.stdin.read()

"""if the condition ARG_CNT ==1 is true then it execute the first line sys.argv[1] then it return the filname and store in it"""
if ARG_CNT == 1:
    filename = sys.argv[1]
    TEXT = readfile(filename)
response = wc(TEXT)

"""the print function is used to print the output in the terminal the below text is printed in the output window"""
print(" " + str(response[0]) + "  " + str(response[1]) + " " + str(response[2]))