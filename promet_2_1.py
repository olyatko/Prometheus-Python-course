# Prometheus-Python-course
# working assignments for the course
import sys
import math 
a = float(sys.argv[1]) 
b = float(sys.argv[2])
c = float(sys.argv[3])
print math.exp((((a-b)**2)/(2*(c**2)))*-1)/(c*math.sqrt(2*math.pi))
# checked and accepted
# automatically generated answer was
# print (1/(a*math.sqrt(2*math.pi)))*math.exp(-(x-m)**2/(2*a**2))
