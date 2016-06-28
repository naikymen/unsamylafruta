from uncertainties import ufloat
from uncertainties.umath import *
import csv
from numpy import genfromtxt
from uncertainties import unumpy
import numpy

f1 = '/media/naikymen/SD64/Unsam/FQ/TP4 2016/Errores/vol08.csv'
f2 = '/media/naikymen/SD64/Unsam/FQ/TP4 2016/Errores/vol008.csv'
f3 = '/media/naikymen/SD64/Unsam/FQ/TP4 2016/Errores/abs.csv'
f4 = '/media/naikymen/SD64/Unsam/FQ/TP4 2016/Errores/volAgua.csv'
f5 = '/media/naikymen/SD64/Unsam/FQ/TP4 2016/Errores/volVBC.csv'
f6 = '/media/naikymen/SD64/Unsam/FQ/TP4 2016/Errores/vol8.csv'

d1 = genfromtxt(f1, delimiter=',')
d2 = genfromtxt(f2, delimiter=',')
d3 = genfromtxt(f3, delimiter=',')
d4 = genfromtxt(f4, delimiter=',')
d5 = genfromtxt(f5, delimiter=',')
d6 = genfromtxt(f6, delimiter=',')

ar8 = unumpy.uarray(d6[:,0],d6[:,1])
ar08 = unumpy.uarray(d1[:,0],d1[:,1])
ar008 = unumpy.uarray(d2[:,0],d2[:,1])
arabs = unumpy.uarray(d3[:,0],d3[:,1])
aragua = unumpy.uarray(d4[:,0],d4[:,1])
arVBC = unumpy.uarray(d5[:,0],d4[:,1])


vol = (ar8 + ar08 + ar008 + aragua + arVBC)
mol = (ar8 * 0.8 + ar08 *0.08 + ar008 *0.008)

conc = mol/vol

mT = unumpy.matrix(conc)
filename = "resconc.csv"
numpy.savetxt(filename, mT, fmt='%r', delimiter='\n')

XB = arabs/(0.757)

mT = unumpy.matrix(XB)
filename = "resXB.csv"
numpy.savetxt(filename, mT, fmt='%r', delimiter='\n')

XHB = 1 - XB

mT = unumpy.matrix(XHB)
filename = "resXHB.csv"
numpy.savetxt(filename, mT, fmt='%r', delimiter='\n')

concH = (0.0000169)*(1+ XB)/(XHB)

mT = unumpy.matrix(concH)
filename = "resconcH.csv"
numpy.savetxt(filename, mT, fmt='%r', delimiter='\n')

FI = 0.5*(XB*4*0.0000169+XHB*0.0000169+2*conc)

mT = unumpy.matrix(FI)
filename = "resFI.csv"
numpy.savetxt(filename, mT, fmt='%r', delimiter='\n')

pkc = -(unumpy.log10(0.0000169*XB*(1+XB)/(1-XB)))

mT = unumpy.matrix(pkc)
filename = "respkc.csv"
numpy.savetxt(filename, mT, fmt='%r', delimiter='\n')

sqI = unumpy.sqrt(FI)
fi = (sqI)/(1+2.3 * sqI)

mT = unumpy.matrix(fi)
filename = "resfi.csv"
numpy.savetxt(filename, mT, fmt='%r', delimiter='\n')

#http://docs.scipy.org/doc/numpy/reference/generated/numpy.savetxt.html
