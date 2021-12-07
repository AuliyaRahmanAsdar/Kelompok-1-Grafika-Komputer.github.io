import numpy as np
import matplotlib.pyplot as grafik


x1 = int(input('Masukan nilai x1  : '))
y1 = int(input('Masukan nilai y1  : '))
x2 = int(input('Masukan nilai x2  : '))
y2 = int(input('Masukan nilai y2  : '))
print('------------------------------------------------')

x = x1
y = y1

if x1 == x2:
    titikA = []
    titikB = []
    for i in range (1,y2,1):
        grafik.plot(titikA,titikB)
        grafik.show()
