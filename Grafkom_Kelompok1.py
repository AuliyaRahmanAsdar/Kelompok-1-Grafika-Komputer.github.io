# Numpy merupakan singkatan Numerical Python yang digunakan dalam memproses array
# Matplotlib digunakan untuk menggambarkan titik koordinat menjadi sebuah garis
import numpy as np
import matplotlib.pyplot as graphic


x1 = int(input('Masukan Nilai X1  : '))
y1 = int(input('Masukan Nilai Y1  : '))
x2 = int(input('Masukan Nilai X2  : '))
y2 = int(input('Masukan Nilai Y2  : '))
print('------------------------------------------------')
# koordinar awal x dan y
x = x1
y = y1
# membuat pengkondisian dengan beberapa syarat seperti :

# ---> Jika nilai x1 = x2 (garis vertikal), maka :
#       a. y = y + 1 dan x tetap
#       b. gambar titik kordinat (x,y) 
#       c. tampilkan garis dari titik-titik koordinat yang terbentuk (selesai)

if x1 == x2:
    koor_x = []
    koor_y = []
    for i in range (1,y2,1):
        graphic.plot(Koor_x,Koor_y)
        graphic.show()
        
# ---> Jika nilai y1 = y2 (garis horizontal), maka :
#       a. x = x + 1 dan y tetap
#       b. gambar titik kordinat (x,y)
#       c. tampilkan garis dari titik-titik koordinat yang terbentuk (selesai)

elif y1 == y2:
    koor_x = []
    koor_y = []
    for i in range (1,x2,1):
        graphic.plot(Koor_x,Koor_y)
        graphic.show()
# ---> Jika ke-2 syarat di atas tidak memenuhi,  maka proses penentuan titik koordinat berlanjut ke:
#       1. hitung kemiringan garis dengan m = (y2 - y1) / (x2 - x1) 
#       2. iterasi diulang sebanyak N kali
#       3. menentukan nilai i dengan persamaan y = m ( x - x1 ) + y1
#       4. lakukan pembulatan pada  nilai y
#       5. gambar titik (x, y(pembulatan))
#       6. nilai x didapatkan dari persamaan x = x + 1

else:
    koor_x = []
    koor_y = []
    gradient = (y2 - y1) / (x2 - x1)
    # N adalah banyaknya iterasi yang didapatkan dari persamaan dibawah ini apabila  x1 != x2 atau y1 != y2
    N = x2 - x1 + 1
    for i in range (0,N,1):
        bulat_y = gradient * (x - x1) + y1
        koord_Y = round(bulat_y)
        print('Garis yang di lewati oleh titik A da titik B yaitu ', x,',', koord_Y)
        koor_x.append(x)
        koor_y.append(koord_Y)
        x+=1
# syntaks apppend digunakan untuk menambah item ke dalam array atau list
# plt.plot digunakan agar mathplotlib dapat membuat titik pertemuan di masing-masing koordinat x,y
# plt.show digunakan agar mathplotlib dapat menampilkan garis dari titik titik kordinat yang telah di dapat 

    graphic.plot(koor_x,koor_y)
    graphic.show()
