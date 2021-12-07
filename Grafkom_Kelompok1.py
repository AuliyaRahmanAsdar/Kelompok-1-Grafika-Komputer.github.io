import numpy as np
import matplotlib.pyplot as grafik


x1 = int(input('Masukan Nilai X1  : '))
y1 = int(input('Masukan Nilai Y1  : '))
x2 = int(input('Masukan Nilai X2  : '))
y2 = int(input('Masukan Nilai Y2  : '))
print('------------------------------------------------')

x = x1
y = y1

if x1 == x2:
    Koor_x = []
    Koor_y = []
    for i in range (1,y2,1):
        grafik.plot(Koor_x,Koor_y)
        grafik.show()

elif y1 == y2:
    koor_x = []
    koor_y = []
    for i in range (1,y2,1):
        grafik.plot(Koor_x,Koor_y)
        grafik.show()

else:
    koor_x = []
    koor_y = []
    m_kemiringangaris = (y2 - y1) / (x2 - x1)
    N = x2 - x1 + 1
    for i in range (0,N,1):
        nilai_y = m_kemiringangaris * (x - x1) + y1
        kordinatY = round(nilai_y)
        print('Garis yang di lewati oleh titik A da titik B yaitu ', x,',', kordinatY)
        koor_x.append(x)
        koor_y.append(kordinatY)
        x+=1
        

    grafik.plot(koor_x,koor_y)
    grafik.show()
