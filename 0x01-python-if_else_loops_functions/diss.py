#!/usr/bin/python3
from dis import dis
from sys import argv
mgc = __import__(f'{argv[1]}').magic_calculation
dis(mgc)
