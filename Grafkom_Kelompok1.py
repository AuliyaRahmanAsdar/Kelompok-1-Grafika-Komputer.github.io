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

elif y1 == y2:
    titikA = []
    titikB = []
    for i in range (1,y2,1):
        grafik.plot(titikA,titikB)
        grafik.show()

else:
    titikA = []
    titikB = []
    m_kemiringangaris = (y2 - y1) / (x2 - x1)
    N = x2 - x1 + 1
    for i in range (0,N,1):
        nilai_y = m_kemiringangaris * (x - x1) + y1
        kordinatY = round(nilai_y)
        print('Garis yang di lewati oleh titik A da titik B yaitu ', x,',', kordinatY)
        titikA.append(x)
        titikB.append(kordinatY)
        x+=1
        

    grafik.plot(titikA,titikB)
    grafik.show()
