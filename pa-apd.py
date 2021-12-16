# PROJECT AKHIR ALGORITMA & PEMROGRAMAN DASAR
# DOSEN PEMBIMBING: Pak Edy Budiman

# ANGGOTA: 1. RISKY KURNIAWAN, 2. AHMAD RIADI, 3. SEVINA AVI AMALIA, 4. MIRA SARTIKA LENGKONG, 5. OLIVIA OKTAVI UTAMI

import math
import turtle
import os
import platform
import sys
from time import sleep

riwayat = []
iniLuas = iniKeliling = False

def clear():
    os.system('cls'if os.name=='nt' else 'clear')
clear()


def gambarPersegi():
    # Persegi
    turtle.bgcolor("#393e46")

    # sisi 1
    turtle.color("#393e46")
    turtle.begin_fill()    
    turtle.forward(100)
    turtle.left(90)
    turtle.end_fill() 
    turtle.color("#ffd369", "#222831")
    turtle.begin_fill()
    turtle.write(' sisi', move=False, align = "left", font=("Arial", 13, "italic"))    
    turtle.forward(100)
    turtle.left(90)

    # sisi 2 
    turtle.forward(100)
    turtle.write('sisi', move=False, align = "center", font=("Arial", 13, "italic"))    
    turtle.forward(100)
    turtle.left(90)
    
    # sisi 3 
    turtle.forward(100)
    turtle.write(' sisi', move=False, align = "left", font=("Arial", 13, "italic"))    
    turtle.forward(100)
    turtle.left(90)

    # sisi 4
    turtle.forward(100)
    turtle.write("\n\nsisi", move=False, align = "center", font=("Arial", 13, "italic"))    
    turtle.forward(100)
    turtle.left(90)   
    turtle.forward(100)
    turtle.left(90)
    turtle.end_fill()

    turtle.color("#222831")
    turtle.begin_fill()    
    turtle.forward(15)
    turtle.end_fill() 

    kerjakan = True
    while (kerjakan):
        try:
            turtle.done()
            kerjakan = False
            turtle.TurtleScreen._RUNNING = True
        except turtle.Terminator:
            turtle.TurtleScreen._RUNNING = True
            print("JANGAN DI CLOSE SEBELUM GAMBAR SELESAI!!!")
            continue



def gambarPersegiPanjang():
    # Persegi Panjang
    turtle.bgcolor("#393e46")

    # sisi 1
    turtle.color("#393e46")
    turtle.begin_fill()    
    turtle.forward(150)
    turtle.left(90)
    turtle.end_fill() 
    turtle.color("#ffd369", "#222831")
    turtle.begin_fill()    
    turtle.write(" Lebar", move=False, align = "left", font=("Arial", 13, "italic"))    
    turtle.forward(100)
    turtle.left(90)

    # sisi 2 
    turtle.forward(150)
    turtle.write("Panjang", move=False, align = "center", font=("Arial", 13, "italic"))    
    turtle.forward(150)
    turtle.left(90)
    
    # sisi 3 
    turtle.forward(100)
    turtle.write(" Lebar", move=False, align = "left", font=("Arial", 13, "italic"))    
    turtle.forward(100)
    turtle.left(90)

    # sisi 4
    turtle.forward(150)
    turtle.write("Panjang", move=False, align = "center", font=("Arial", 13, "italic"))    
    turtle.forward(150)
    turtle.left(90)   
    turtle.forward(100)
    turtle.left(90)
    turtle.end_fill()

    turtle.color("#222831")
    turtle.begin_fill()    
    turtle.forward(15)
    turtle.end_fill() 

    kerjakan = True
    while (kerjakan):
        try:
            turtle.done()
            kerjakan = False
            turtle.TurtleScreen._RUNNING = True
        except turtle.Terminator:
            turtle.TurtleScreen._RUNNING = True
            print("JANGAN DI CLOSE SEBELUM GAMBAR SELESAI!!!")
            continue


def gambarJajarGenjang():
    # JAJAR GENJANG

    turtle.bgcolor("#393e46")

    turtle.color("#393e46")
    turtle.begin_fill()    
    turtle.goto(0, -50)
    turtle.end_fill()
    turtle.color("#ffd369", "#222831")
    turtle.begin_fill()
    turtle.write("Sisi Alas", move=False, align = "center", font=("Arial", 13, "italic"))        
    turtle.goto(105, -50)
    turtle.goto(-195, -50)
    turtle.goto(-150, 0)
    turtle.write("Sisi Miring  ", move=False, align = "right", font=("Arial", 13, "italic"))    
    turtle.goto(-105, 50)
    turtle.goto(195, 50)
    turtle.goto(105, -50)
    turtle.goto(-105, -50)
    turtle.goto(-105, 0)
    turtle.write(" Tinggi", move=False, align = "left", font=("Arial", 13, "italic"))    
    turtle.goto(-105, 50)
    turtle.end_fill()

    kerjakan = True
    while (kerjakan):
        try:
            turtle.done()
            kerjakan = False
            turtle.TurtleScreen._RUNNING = True
        except turtle.Terminator:
            turtle.TurtleScreen._RUNNING = True
            print("JANGAN DI CLOSE SEBELUM GAMBAR SELESAI!!!")
            continue



def gambarTrapesium():
    # TRAPESIUM
    turtle.bgcolor("#393e46")
    turtle.color("#ffd369", "#222831")
    turtle.begin_fill()
    turtle.write(" Sisi Alas", move=False, align = "center", font=("Arial", 13, "italic"))    
    # turtle.goto(0, 0)
    turtle.goto(120, 0)
    turtle.goto(120, 60)
    turtle.write("Tinggi ", move=False, align = "right", font=("Arial", 13, "italic"))    
    turtle.goto(120, 150)
    turtle.goto(0, 150)
    turtle.write(" Sisi Atas", move=False, align = "center", font=("Arial", 13, "italic"))
    turtle.goto(-120, 150)
    turtle.goto(-120, 75)
    # turtle.write(" Tinggi", move=False, align = "left", font=("Arial", 13, "italic"))    
    turtle.goto(-120, 0)
    turtle.goto(210, 0)
    turtle.goto(165, 75)
    turtle.write(" Sisi Miring", move=False, align = "left", font=("Arial", 13, "italic"))    
    turtle.goto(120, 150)
    turtle.goto(-120, 150)
    turtle.goto(-165, 75)
    turtle.write("Sisi Miring ", move=False, align = "right", font=("Arial", 13, "italic"))    
    turtle.goto(-210, 0)

    turtle.goto(120, 0)
    turtle.end_fill()

    kerjakan = True
    while (kerjakan):
        try:
            turtle.done()
            kerjakan = False
            turtle.TurtleScreen._RUNNING = True
        except turtle.Terminator:
            turtle.TurtleScreen._RUNNING = True
            print("JANGAN DI CLOSE SEBELUM GAMBAR SELESAI!!!")
            continue


def gambarBelahKetupat():
    #BELAH KETUPAT
    turtle.bgcolor("#393e46")
    turtle.color("#ffd369", "#222831")
    turtle.begin_fill()
    turtle.write("      Diagonal 1", move=False, align = "left", font=("Arial", 13, "italic"))    
    turtle.goto(150, 0)
    turtle.goto(-150, 0)
    turtle.goto(-75, 100)
    turtle.write("Sisi 1 ", move=False, align = "right", font=("Arial", 13, "italic"))    
    turtle.goto(0, 200)
    turtle.goto(0, -85)
    turtle.write("Diagonal 2 ", move=False, align = "right", font=("Arial", 13, "italic"))    
    turtle.goto(0, -200)
    turtle.goto(75, -100)
    turtle.write("     Sisi 2 ", move=False, align = "left", font=("Arial", 13, "italic"))
    turtle.goto(150, 0)
    turtle.goto(75, 100)
    turtle.write(" Sisi 3", move=False, align = "left", font=("Arial", 13, "italic"))
    turtle.goto(0, 200)
    turtle.goto(0, -200)
    turtle.goto(-75, -100)
    turtle.write("Sisi 4    ", move=False, align = "right", font=("Arial", 13, "italic"))
    turtle.goto(-150, 0)
    turtle.end_fill()

    kerjakan = True
    while (kerjakan):
        try:
            turtle.done()
            kerjakan = False
            turtle.TurtleScreen._RUNNING = True
        except turtle.Terminator:
            turtle.TurtleScreen._RUNNING = True
            print("JANGAN DI CLOSE SEBELUM GAMBAR SELESAI!!!")
            continue



def gambarLayangLayang():
    turtle.bgcolor("#393e46")
    turtle.color("#393e46")
    turtle.begin_fill()
    turtle.goto(50, 0)
    turtle.end_fill()
    turtle.color("#ffd369", "#222831")
    turtle.begin_fill()
    turtle.goto(50, 120)
    turtle.goto(50, -120)
    turtle.goto(50, -50)
    turtle.write("Diagonal 1 ", move=False, align = "right", font=("Arial", 13, "italic"))    
    turtle.goto(50, 0)
    turtle.goto(155, 0)
    turtle.goto(0, 0)
    turtle.write("Diagonal 2 ", move=False, align = "right", font=("Arial", 13, "italic"))    
    turtle.goto(-155, 0)
    turtle.goto(-52.5, -60)
    turtle.write("Sisi 1      ", move=False, align = "right", font=("Arial", 13, "italic"))    
    turtle.goto(50, -120)
    turtle.goto(102.5, -60)
    turtle.write("      Sisi 2", move=False, align = "left", font=("Arial", 13, "italic"))    
    turtle.goto(155, 0)
    turtle.goto(50, 120)
    turtle.goto(-155, 0)
    turtle.end_fill()

    kerjakan = True
    while (kerjakan):
        try:
            turtle.done()
            kerjakan = False
            turtle.TurtleScreen._RUNNING = True
        except turtle.Terminator:
            turtle.TurtleScreen._RUNNING = True
            print("JANGAN DI CLOSE SEBELUM GAMBAR SELESAI!!!")
            continue



def gambarSegitiga():
    turtle.bgcolor("#393e46")
    turtle.color("#393e46", "white")
    turtle.begin_fill()
    turtle.goto(0, -50)
    turtle.end_fill()
    turtle.color("#ffd369", "#222831")
    turtle.begin_fill()
    turtle.write("Sisi 1 (Alas) ", move=False, align = "right", font=("Arial", 13, "italic"))
    turtle.goto(120, -50)
    turtle.goto(-120, -50)
    turtle.goto(-60, 55)
    turtle.write("Sisi 2 ", move=False, align = "right", font=("Arial", 13, "italic"))
    turtle.goto(0, 160)
    turtle.goto(60, 55)
    turtle.write(" Sisi 3", move=False, align = "left", font=("Arial", 13, "italic"))
    turtle.goto(120, -50)
    turtle.goto(0, -50)
    turtle.goto(0, 50)
    turtle.write(" Tinggi", move=False, align = "left", font=("Arial", 13, "italic"))
    turtle.goto(0, 160)
    turtle.end_fill()

    kerjakan = True
    while (kerjakan):
        try:
            turtle.done()
            kerjakan = False
            turtle.TurtleScreen._RUNNING = True
        except turtle.Terminator:
            turtle.TurtleScreen._RUNNING = True
            print("JANGAN DI CLOSE SEBELUM GAMBAR SELESAI!!!")
            continue



def gambarLingkaran():
    #Lingkaran
    turtle.bgcolor("#393e46")

    turtle.color("#ffd369", "#222831")
    turtle.begin_fill()
    turtle.circle(100)
    turtle.left(90)   
    turtle.goto(0, 50)
    turtle.write(" Jari-Jari", move=False, align = "left", font=("Arial", 13, "italic"))
    turtle.goto(0, 100)
    turtle.left(180)
    turtle.forward(100)
    turtle.end_fill()

    kerjakan = True
    while (kerjakan):
        try:
            turtle.done()
            kerjakan = False
            turtle.TurtleScreen._RUNNING = True
        except turtle.Terminator:
            turtle.TurtleScreen._RUNNING = True
            print("JANGAN DI CLOSE SEBELUM GAMBAR SELESAI!!!")
            continue


    


def persegi(pil, pilBangun):
    EROR = True
    while (EROR): 
        try:
            if (str.upper(pil) == "LUAS"):
                print("Luas Persegi")
                salah = True
                while(salah):
                    s = int(input("Masukkan panjang sisinya (cm):   "))
                    if (s == 0):
                        print("Ups, Panjang sisi tidak boleh 0!!")
                    elif (s < 0):
                        print("Tidak boleh Negatif!!!!")
                    else:
                        L = s * s 
                        print("L = sisi * sisi")
                        print("L =", s, "*", s)
                        print("Luas = {} cm^2\n".format(L))
                        salah = False           
                gambarPersegi()                 
                return L
                EROR = False

            elif (str.upper(pil) == "KELILING"):
                print("Keliling Persegi")
                salah = True
                while (salah):
                    s = int(input("Masukkan panjang sisinya (cm):   "))
                    if (s == 0):
                        print("Ups, Panjang sisi tidak boleh 0!!")
                    elif (s < 0):
                        print("Tidak boleh Negatif!!!!")
                    else:
                        K = 4 * s
                        print("K = sisi + sisi + sisi + sisi")
                        print("K =", s, "+", s, "+", s, "+", s)
                        print("Keliling = {} cm\n".format(K))
                        salah = False    
                gambarPersegi()
                return K
                EROR = False
        except ValueError:
            print("Input anda salah, Masukkan angka!!")





def persegiPanjang(pil, pilBangun):
    EROR = True
    while (EROR): 
        try:
            if (str.upper(pil) == "LUAS"):
                print("Luas Persegi panjang")
                salah = True
                while (salah):
                    p = int(input("Masukkan panjangnya (cm):    "))
                    l = int(input("Masukkan lebarnya   (cm):    "))
                    if (p == 0 and l == 0):
                        print("Ups, Panjang dan Lebar tidak boleh 0!!")
                    elif (p == 0):
                        print("Ups, Panjang tidak boleh 0!!")
                    elif (l == 0):
                        print("Ups, Lebar tidak boleh 0!!")
                    elif (p < 0 or l < 0):
                        print("Tidak boleh Negatif!!!!")
                    else:
                        L = p * l
                        print("L = panjang * lebar")
                        print("L =", p, "*", l)
                        print("Luas = {} cm^2\n".format(L))
                        salah = False
                gambarPersegiPanjang()
                return L   
                EROR = False

            elif (str.upper(pil) == "KELILING"):
                print("Keliling Persegi panjang")
                salah = True
                while (salah):
                    p = int(input("Masukkan panjangnya (cm):    "))
                    l = int(input("Masukkan lebarnya   (cm):    "))
                    if (p == 0 and l == 0):
                        print("Ups, Panjang dan Lebar tidak boleh 0!!")
                    elif (p == 0):
                        print("Ups, Panjang tidak boleh 0!!")
                    elif (l == 0):
                        print("Ups, Lebar tidak boleh 0!!")
                    elif (p < 0 or l < 0):
                        print("Tidak boleh Negatif!!!!")
                    else:
                        K = 2 * (p + l)
                        print("K = 2 * (panjang + lebar)")
                        print("K = 2 *", "(", p, "+", l, ")")  
                        print("Keliling = {} cm\n".format(K))    
                        salah = False
                gambarPersegiPanjang()
                return K
                EROR = False
        except ValueError:
            print("Input anda salah, Masukkan angka!!")





def jajarGenjang(pil, pilBangun):
    EROR = True
    while (EROR): 
        try:
            if (str.upper(pil) == "LUAS"):
                print("Luas Jajar genjang")
                salah = True
                while (salah):
                    sBawah = int(input("Masukkan panjang alasnya (cm):    "))
                    t = int(input("Masukkan tingginya       (cm):    "))
                    if (sBawah == 0 and t == 0):
                        print("Ups, Panjang alas dan Tinggi tidak boleh 0!!")
                    elif (sBawah == 0):
                        print("Ups, Panjang alas tidak boleh 0!!")
                    elif (t == 0):
                        print("Ups, Tinggi tidak boleh 0!!")
                    elif (sBawah < 0 or t < 0):
                        print("Tidak boleh Negatif!!!!")
                    else:                        
                        L = sBawah * t
                        print("L = alas * tinggi")
                        print("L =", sBawah, "*", t)
                        print("Luas = {} cm^2\n".format(L))
                        salah = False
                gambarJajarGenjang()
                return L  
                EROR = False

            elif (str.upper(pil) == "KELILING"):
                print("Keliling Jajar genjang")
                salah = True
                while (salah):
                    sBawah = int(input("Masukkan panjang alasnya        (cm):    "))
                    sMiring = int(input("Masukkan panjang sisi miringnya (cm):    "))
                    if (sBawah == 0 and sMiring == 0):
                        print("Ups, Panjang alas dan Sisi miring tidak boleh 0!!")
                    elif (sBawah == 0):
                        print("Ups, Panjang alas tidak boleh 0!!")
                    elif (sMiring == 0):
                        print("Ups, Sisi Miring tidak boleh 0!!")
                    elif (sBawah < 0 or sMiring < 0):
                        print("Tidak boleh Negatif!!!!")
                    else:
                        K = 2 * (sBawah + sMiring)
                        print("K = 2 * (sisiAlas + sisiMiring)")
                        print("K = 2 * (", sBawah, "+", sMiring, ")")
                        print("Keliling = {} cm".format(K))
                        salah = False 
                gambarJajarGenjang()
                return K
                EROR = False
        except ValueError:
            print("Input anda salah, Masukkan angka!!")
    

    


def trapesium(pil, pilBangun):
    EROR = True
    while (EROR): 
        try:
            if (str.upper(pil) == "LUAS"):
                print("Luas Trapesium")
                salah = True
                while(salah):
                    sBawah = int(input("Masukkan panjang alasnya      (cm):    "))
                    sAtas = int(input("Masukkan panjang sisi atasnya (cm):    "))
                    t = int(input("Masukkan tingginya            (cm):    "))
                    if (sBawah == 0 and sAtas == 0 and t == 0):
                        print("Ups, Panjang alas, Sisi atas, dan Tinggi tidak boleh 0!!")
                    elif(sBawah == 0 and sAtas == 0):
                        print("Ups, Panjang alas, Sisi atas, tidak boleh 0!!")
                    elif (sAtas == 0 and t == 0):
                        print("Ups, Panjang Sisi atas, dan Tinggi tidak boleh 0!!")
                    elif (sAtas == 0):
                        print("Ups, Panjang Sisi Atas tidak boleh 0!!")
                    elif (sBawah == 0):
                        print("Ups, Panjang Sisi Alas tidak boleh 0!!")
                    elif (t == 0):
                        print("Ups, Tinggi tidak boleh 0!!")
                    elif (sBawah < 0 or t < 0 or sAtas < 0):
                        print("Tidak boleh Negatif!!!!")
                    else:
                        L = .5 * (sBawah + sAtas) * t
                        print("L = 1/2 * (alas + sisiAtas) * tinggi")
                        print("L = 1/2 * (", sBawah, "+", sAtas, ")", "*", t)
                        print("Luas = {} cm^2".format(L)) 
                        salah = False 
                gambarTrapesium()
                return L
                EROR = False
            elif (str.upper(pil) == "KELILING"):
                print("Keliling Trapesium")
                salah = True
                while(salah):
                    sBawah = int(input("Masukkan panjang sisi alasnya (cm):\t"))
                    sAtas = int(input("Masukkan panjang sisi atasnya (cm):\t"))
                    sKanan = int(input("Masukkan panjang sisi kanannya (cm):\t"))
                    sKiri = int(input("Masukkan panjang sisi Kirinya (cm):\t")) 
                    if (sBawah == 0 and sAtas == 0 and sKanan == 0 and sKiri == 0):
                        print("Ups, Panjang Alas, sisi Atas, sisi Kanan, sisi Kiri tidak boleh 0!!" )
                    elif (sBawah == 0 and sAtas == 0 and sKanan == 0):
                        print("Ups, Panjang Alas, sisi Atas, sisi Kanan, tidak boleh 0!!" )
                    elif (sBawah == 0 and sAtas == 0 and sKiri == 0):
                        print("Ups, Panjang Alas, sisi Atas, sisi Kiri tidak boleh 0!!" )
                    elif (sBawah == 0 and sKanan == 0 and sKiri == 0):
                        print("Ups, Panjang Alas, sisi Kanan, sisi Kiri tidak boleh 0!!" )
                    elif (sAtas == 0 and sKanan == 0 and sKiri == 0):
                        print("Ups, Panjang sisi Atas, sisi Kanan, sisi Kiri tidak boleh 0!!" )
                    elif (sBawah == 0 and sAtas == 0):
                        print("Ups, Panjang Alas, sisi Atas tidak boleh 0!!" )
                    elif (sBawah == 0 and sKanan == 0):
                        print("Ups, Panjang Alas, sisi Kanan tidak boleh 0!!" )
                    elif (sBawah == 0 and sKiri == 0):
                        print("Ups, Panjang Alas, sisi Kiri tidak boleh 0!!" )
                    elif (sAtas == 0 and sKanan):
                        print("Ups, Panjang sisi Atas, sisi Kanan tidak boleh 0!!" )
                    elif (sAtas == 0 and sKiri == 0):
                        print("Ups, Panjang sisi Atas, sisi Kiri tidak boleh 0!!" )
                    elif (sKanan == 0 and sKiri == 0):
                        print("Ups, Panjang sisi Kanan, sisi Kiri tidak boleh 0!!" )
                    elif (sBawah == 0):
                        print("Ups, Panjang alas tidak boleh 0!!")
                    elif (sAtas == 0):
                        print("Ups, Panjang Sisi Atas tidak boleh 0!!")
                    elif (sKanan == 0):
                        print("Ups, Panjang Sisi Kanan tidak boleh 0!!")
                    elif (sKiri == 0):
                        print("Ups, Panjang Sisi Kiri tidak boleh 0!!")
                    elif (sBawah < 0 or sAtas < 0 or sKanan < 0 or sKiri < 0):
                        print("Tidak boleh Negatif!!!!")
                    else:
                        K = sAtas + sKiri + sKanan + sBawah
                        print("K = sAtas+sKiri+sKanan+sBawah")
                        print("K =", sAtas, "+", sKiri, "+", sKanan, "+", sBawah)
                        print("Keliling = {} cm".format(K))
                        salah = False
                gambarTrapesium()
                return K
                EROR = False
        except ValueError:
            print("Input anda salah, Masukkan angka!!")




def belahKetupat(pil, pilBangun):
    EROR = True
    while (EROR): 
        try:
            if (str.upper(pil) == "LUAS"):
                print("Luas Belah Ketupat")
                salah = True
                while(salah):
                    d1 = int(input("Masukkan panjang diagonal1 (cm):     "))
                    d2 = int(input("Masukkan panjang diagonal2 (cm):     "))
                    if(d1 == 0 and d2 == 0):
                        print("Ups, Diagonal 1 dan Diagonal 2 tidak boleh 0!!")
                    elif(d1 == 0):
                        print("Ups, Diagonal 1 tidak boleh 0!!")
                    elif(d2 == 0):
                        print("Ups, Diagonal 2 tidak boleh 0!!")
                    elif (d1 < 0 or d2 < 0):
                        print("Tidak boleh Negatif!!!!")
                    else:
                        L = .5 * d1 * d2
                        print("L = 1/2 * diagonal1 * diagonal2")
                        print("L = 1/2 *", d1, "*", d2)
                        print("Luas = {} cm^2".format(L))
                        salah = False 
                gambarBelahKetupat()
                return L
                EROR = False

            elif (str.upper(pil) == "KELILING"):
                print("Keliling Belah Ketupat")
                salah = True
                while (salah):
                    s = int(input("Masukkan panjang sisinya (cm):   "))
                    if (s == 0):
                        print("Ups, Panjang sisi tidak boleh 0!!")
                    elif (s < 0):
                        print("Tidak boleh Negatif!!!!")
                    else:
                        K = 4 * s
                        print("K = sisi + sisi + sisi + sisi")
                        print("K = ", s, "+", s, "+", s, "+", s)
                        print("Keliling = {} cm".format(K))
                        salah = False
                gambarBelahKetupat()
                return K
                EROR = False
        except ValueError:
            print("Input anda salah, Masukkan angka!!")
    

    


def layangLayang(pil, pilBangun):
    EROR = True
    while (EROR): 
        try:
            if (str.upper(pil) == "LUAS"):
                print("Luas Layang-layang")
                salah = True
                while(salah):
                    d1 = int(input("Masukkan panjang diagonal1 (cm):    "))
                    d2 = int(input("Masukkan panjang diagonal2 (cm):    "))
                    if(d1 == 0 and d2 == 0):
                        print("Ups, Diagonal 1 dan Diagonal 2 tidak boleh 0!!")
                    elif(d1 == 0):
                        print("Ups, Diagonal 1 tidak boleh 0!!")
                    elif(d2 == 0):
                        print("Ups, Diagonal 2 tidak boleh 0!!")
                    elif (d1 < 0 or d2 < 0):
                        print("Tidak boleh Negatif!!!!")
                    else:     
                        L =  .5 * d1 * d2
                        print("L = 1/2 * diagonal1 * diagonal2")
                        print("L = 1/2 *", d1, "*", d2)
                        print("Luas = {} cm^2".format(L))
                        salah = False  
                gambarLayangLayang()
                return L
                EROR = False

            elif (str.upper(pil) == "KELILING"):
                print("Keliling Layang-layang")
                salah = True
                while(salah):
                    s1 = int(input("Masukkan panjang sisi1 (cm):     "))
                    s2 = int(input("Masukkan panjang sisi2 (cm):     "))
                    if (s1 == 0 and s2 == 0):
                        print("Panjang Sisi 1 & Sisi 2 tidak boleh nol")
                    elif (s1 == 0):
                        print("Panjang Sisi 1 tidak boleh nol")
                    elif (s2 == 0):
                        print("Panjang Sisi 2 tidak boleh nol")    
                    elif (s1 < 0 or s2 < 0):
                        print("Tidak boleh Negatif!!!!")
                    else:
                        K = 2 * (s1 + s2)
                        print("K = 2 * (sisi1 + sisi2)")
                        print("K = 2 * (", s1, "+", s2, ")")
                        print("Keliling = {} cm".format(K))
                        salah = False
                gambarLayangLayang()
                return K
                EROR = False
        except ValueError:
            print("Input anda salah, Masukkan angka!!")
   

    


def segitiga(pil, pilBangun):
    EROR = True
    while (EROR): 
        try:
            if (str.upper(pil) == "LUAS"):
                print("Luas Segitiga")
                salah = True
                while (salah):
                    sBawah = int(input("Masukkan panjang alasnya (cm):\t"))
                    t = int(input("Masukkan tingginya (cm):\t"))
                    if (sBawah == 0 and t == 0):
                        print("Ups, Panjang alas dan Tinggi tidak boleh 0!!")
                    elif (sBawah == 0):
                        print("Ups, Panjang alas tidak boleh 0!!")
                    elif (t == 0):
                        print("Ups, Tinggi tidak boleh 0!!")
                    elif (sBawah < 0 or t < 0):
                        print("Tidak boleh Negatif!!!!")
                    else:
                        L = .5 * sBawah * t
                        print("L = 1/2 * alas * tinggi")
                        print("L = 1/2 *", sBawah, "*", t)
                        print("Luas = {} cm^2".format(L)) 
                        salah = False
                gambarSegitiga()
                return L
                EROR = False

            elif (str.upper(pil) == "KELILING"):
                print("Keliling Segitiga")
                salah = True
                while (salah):
                    s1 = int(input("Masukkan panjang sisi1 (cm):     "))
                    s2 = int(input("Masukkan panjang sisi2 (cm):     "))
                    s3 = int(input("Masukkan panjang sisi3 (cm):     "))
                    if (s1 == 0 and s2 == 0 and s3 == 0):
                        print("Panjang Sisi 1, Sisi 2, dan Sisi 3 tidak boleh nol")
                    elif (s1 == 0 and s2 == 0):
                        print("Panjang Sisi 1 & Sisi 2 tidak boleh nol")
                    elif (s1 == 0 and s3 == 0):
                        print("Panjang Sisi 1 & Sisi 3 tidak boleh nol")
                    elif (s2 == 0 and s3 == 0):
                        print("Panjang Sisi 2 & Sisi 3 tidak boleh nol")
                    elif (s1 == 0):
                        print("Panjang Sisi 1 tidak boleh nol")
                    elif (s2 == 0):
                        print("Panjang Sisi 2 tidak boleh nol")
                    elif (s3 == 0):
                        print("Panjang Sisi 3 tidak boleh nol")
                    elif (s1 < 0 or s2 < 0 or s3 < 0):
                        print("Tidak boleh Negatif!!!!")
                    else:
                        K = s1 + s2 +s3
                        print("K = s1 + s2 + s3")
                        print("K =", s1, "+", s2, "+", s3)
                        print("Keliling = {} cm".format(K))
                        salah = False
                gambarSegitiga()
                return K
                EROR = False
        except ValueError:
            print("Input anda salah, Masukkan angka!!")
    

   


def lingkaran(pil, pilBangun):
    EROR = True
    while (EROR): 
        try:
            if (str.upper(pil) == "LUAS"):
                print("Luas Lingkaran")
                salah = True
                while(salah):
                    r = int(input("Masukkan panjang jari-jarinya (cm):   "))
                    if r == 0:
                        print("Ups, Panjang Jari-jari tidak boleh 0!!")
                    elif (r < 0):
                        print("Tidak boleh Negatif!!!!")
                    else:
                        L = math.pi * r**2
                        print("L = π * jari-jari^2")
                        print("L = 3.141592 *", r**2)
                        print("Luas = {} cm^2".format(L)) 
                        salah = False
                gambarLingkaran()
                return L
                EROR = False
                
            elif (str.upper(pil) == "KELILING"):
                print("Keliling Lingkaran")
                salah = True
                while(salah):
                    r = int(input("Masukkan panjang jari-jarinya (cm):   "))
                    if (r == 0):
                        print("Ups, Panjang Jari-jari tidak boleh 0!!")
                    elif (r < 0):
                        print("Tidak boleh Negatif!!!!")
                    else:
                        K = 2 * math.pi * r
                        print("K = 2 * π * jari-jari")
                        print("K = 2 * 3.141592 *", r)
                        print("Keliling = {} cm".format(K))
                        salah = False
                gambarLingkaran()
                return K    
                EROR = False
        except ValueError:
            print("Input anda salah, Masukkan angka!!")
    



def mulaiMenghitung(user):
    global riwayat, iniLuas, iniKeliling
    print("==========================")
    print("[1] Persegi\t\t||")
    print("[2] Persegi panjang\t||")
    print("[3] Jajar Genjang\t||")
    print("[4] Trapesium\t\t||")
    print("[5] Belah Ketupat\t||")
    print("[6] Layang-Layang\t||")
    print("[7] Segitiga\t\t||")
    print("[8] Lingkaran\t\t||")
    print("==========================")
    bangun = ["Persegi",#=============> 0
              "Persegi Panjang",#=====> 1
              "Jajar Genjang",#=======> 2
              "Trapesium",#===========> 3
              "Belah Ketupat",#=======> 4   
              "Layang-Layang",#=======> 5
              "Segitiga",#============> 6
              "Lingkaran"]#===========> 7 
    kerjakan = True
    while (kerjakan): 
        try:
            pilBangun = int(input("\nBangun apa yang ingin anda pilih? (Nomornya saja):     "))
            if (pilBangun >= 1 and pilBangun <= 8):
                kerjakan = False
                print("Anda Memilih bangun {}\n".format(bangun[pilBangun-1]))   
            else:
                print("Masukkan angka diantara 1 - 8")
        except ValueError:
            print("Input anda salah, Masukkan angka diantara 1 - 8")
    
    kerjakan = True
    while (kerjakan): 
        pil = input("LUAS / KELILING? :    ")
        if (str.upper(pil) == "LUAS"):
            iniLuas = True
            kerjakan = False
            print("Anda Memilih {} {}\n\n".format(str.capitalize(pil), bangun[pilBangun-1]))
        elif (str.upper(pil) == "KELILING"):
            iniKeliling = True
            kerjakan = False
            print("Anda Memilih {} {}\n\n".format(str.capitalize(pil), bangun[pilBangun-1]))
        else:
            print("Input anda salah!")
            


    if (pilBangun == 1):
        hasil = persegi(pil, pilBangun)

    elif (pilBangun == 2):
        hasil = persegiPanjang(pil, pilBangun)
    
    elif (pilBangun == 3):
        hasil = jajarGenjang(pil, pilBangun)
    
    elif (pilBangun == 4):
        hasil = trapesium(pil, pilBangun)
    
    elif (pilBangun == 5):
        hasil = belahKetupat(pil, pilBangun)
    
    elif (pilBangun == 6):
        hasil = layangLayang(pil, pilBangun)
    
    elif (pilBangun == 7):
        hasil = segitiga(pil, pilBangun)
    
    elif (pilBangun == 8):
        hasil = lingkaran(pil, pilBangun)


    if (iniLuas):
        riwayat.append("Nama: {}, \nBangun yang dipilih: {},  \n{},  \nHasil = {}cm^2\n\n".format(str.title(user), bangun[pilBangun-1], str.capitalize(pil), hasil))  
        iniLuas = False
    if (iniKeliling):
        riwayat.append("Nama: {}, \nBangun yang dipilih: {},  \n{},  \nHasil = {}cm\n\n".format(str.title(user), bangun[pilBangun-1], str.capitalize(pil), hasil))
        iniKeliling = False
    showMenu1()



def editHistory():
    clear()
    global iniLuas, iniKeliling
    print("\n\n")
    print("==========================================================================")
    for j in range(len(riwayat)):
        print("["+ str(j+1)+ "]")
        print(str(riwayat[j]))
    print("==========================================================================")
    EROR = True
    while(EROR):
        try: 
            ubah = int(input("Nomor ke berapa yang ingin anda ubah?:    "))
            if (ubah == 0):
                showMenu1()
            elif (ubah >= 1):
                del riwayat[ubah-1]
                EROR = False
            else:
                print("Input anda salah!!")        
        except IndexError:
                print("Mohon maaf, anda salah memasukkan Index!!")
        except ValueError:
            print("Input anda salah, Masukkan angka!!")

    print("\n\n\n==========================================================================")
    print("Silahkan Ubah")
    print("==========================================================================\n")
    print("[1] Persegi\t\t||")
    print("[2] Persegi panjang\t||")
    print("[3] Jajar Genjang\t||")
    print("[4] Trapesium\t\t||")
    print("[5] Belah Ketupat\t||")
    print("[6] Layang-Layang\t||")
    print("[7] Segitiga\t\t||")
    print("[8] Lingkaran\t\t||")
    bangun = ["Persegi",#=============> 0
              "Persegi Panjang",#=====> 1
              "Jajar Genjang",#=======> 2
              "Trapesium",#===========> 3
              "Belah Ketupat",#=======> 4
              "Layang-Layang",#=======> 5
              "Segitiga",#============> 6
              "Lingkaran"]#===========> 7 
              
    kerjakan = True
    while (kerjakan): 
        try:
            pilBangun = int(input("\nBangun apa yang ingin anda pilih? (Nomornya saja):     "))
            if (pilBangun >= 1 and pilBangun <= 8):
                kerjakan = False
                print("Anda Memilih bangun {}\n".format(bangun[pilBangun-1]))   
            elif(pilBangun == 0):
                showMenu1()
            else:
                print("Masukkan angka diantara 1 - 8")
        except ValueError:
            print("Input anda salah, Masukkan angka diantara 1 - 8")

    kerjakan = True
    while (kerjakan): 
        pil = input("LUAS / KELILING? :    ")
        if (str.upper(pil) == "LUAS"):
            iniLuas = True
            kerjakan = False
            print("Anda Memilih {} {}\n\n".format(str.capitalize(pil), bangun[pilBangun-1]))
        elif (str.upper(pil) == "KELILING"):
            iniKeliling = True
            kerjakan = False
            print("Anda Memilih {} {}\n\n".format(str.capitalize(pil), bangun[pilBangun-1]))
        else:
            print("Input anda salah!")
            


    if (pilBangun == 1):
        hasil = persegi(pil, pilBangun)

    elif (pilBangun == 2):
        hasil = persegiPanjang(pil, pilBangun)
    
    elif (pilBangun == 3):
        hasil = jajarGenjang(pil, pilBangun)
    
    elif (pilBangun == 4):
        hasil = trapesium(pil, pilBangun)
    
    elif (pilBangun == 5):
        hasil = belahKetupat(pil, pilBangun)
    
    elif (pilBangun == 6):
        hasil = layangLayang(pil, pilBangun)
    
    elif (pilBangun == 7):
        hasil = segitiga(pil, pilBangun)
    
    elif (pilBangun == 8):
        hasil = lingkaran(pil, pilBangun)

    if (iniLuas):
        riwayat.insert(ubah-1,"Nama: {}, \nBangun yang dipilih: {},  \n{},  \nHasil = {}cm^2\n\n".format(str.title(user), bangun[pilBangun-1], str.capitalize(pil), hasil))  
        iniLuas = False
        
    if (iniKeliling):
        riwayat.insert(ubah-1,"Nama: {}, \nBangun yang dipilih: {},  \n{},  \nHasil = {}cm\n\n".format(str.title(user), bangun[pilBangun-1], str.capitalize(pil), hasil))  
        iniKeliling = False
        
    print("Data Berhasil diubah!")
    showMenu1()



def lihatHistory():
    clear()
    print("\n\n")
    if (len(riwayat) < 1):
        print("==========================================================================")
        print("History Kosong!")
        print("==========================================================================")
    else:    
        print("History:")
        print("==========================================================================")
        for j in range(len(riwayat)):
            print("[" + str(j+1) + "]")
            print(str(riwayat[j]))
        print("==========================================================================")
    showMenu1()
    
def hapusHistory():
    clear()
    print("==========================================================================")
    for j in range(len(riwayat)):
        print("[" + str(j+1) + "]")
        print(str(riwayat[j]))
    print("==========================================================================")
    EROR = True
    while(EROR):
            buang = input("Anda ingin menghapus semuanya?:    ")
            if (str.upper(buang) == "TIDAK"):
                EROR = True
                while(EROR):
                    try:
                        hapus = int(input("Nomor ke berapa yang ingin anda hapus?:    "))
                        if (hapus == 0):
                            showMenu1()
                        elif (hapus < 0):
                            print("Mohon maaf, anda salah memasukkan Index!!")
                        else:    
                            del riwayat[hapus - 1]
                            print("History Berhasil dihapus!\n\n")
                            EROR = False
                            showMenu1()
                    except ValueError:
                        print("Input anda salah, Masukkan Angka!!!")        
                    except IndexError:
                        print("Mohon maaf, anda salah memasukkan Index!!")
            elif (str.upper(buang) == "YA"):
                riwayat.clear()
                print("History Berhasil dibersihkan!\n\n")
                EROR = False
                showMenu1()
            elif (str.upper(buang) == "0"):
                showMenu1()
            else:
                print("Input anda salah!!")    

def exitMenu():
    clear()
    save = True
    while(save):
        simpan = input("Apakah anda ingin Menyimpan History dalam file Text? (YA / TIDAK):    ")
        if (str.upper(simpan) == "YA"):
            file_history = open("History ("+ str.title(user) + ").txt", "a")
            for i in range(len(riwayat)):
                history = str(riwayat[i])
                file_history.write(history)
            file_history.close()
            sleep(1)
            print("History anda Tersimpan!")   
            print("\n\n\n\nTerima Kasih telah menggunakan Program Kami!\n\n\n\n")    
            save = False
        elif (str.upper(simpan) == "TIDAK"): 
            sleep(1)
            print("\n\n\n\nTerima Kasih telah menggunakan Program Kami!\n\n\n\n")       
            save = False
        elif (str.upper(simpan) == "0"):
            showMenu1()
        else:
            print("Input Anda Salah!!!")



def showMenu1():
    input("ketik [ENTER] untuk melanjutkan...")
    clear()
    print(5*"\n")
    print("[1] Lanjut Menghitung")
    print("[2] Edit History")
    print("[3] Lihat History")
    print("[4] Hapus History")
    print("[0] Exit")
    ulangi = True
    while(ulangi):
        selected_menu = str(input("Pilih menu yang ingin anda pilih >>>    "))
        if(selected_menu == "1"):
            print(43*"\n")
            print("([0] Untuk membatalkan pilihan)\n\n")
            mulaiMenghitung(user)
            ulangi = False
        elif(selected_menu == "2"):
            print("([0] Untuk membatalkan pilihan)\n\n")
            editHistory()
            ulangi = False
        elif(selected_menu == "3"):
            print("([0] Untuk membatalkan pilihan)\n\n")
            lihatHistory()
            ulangi = False
        elif(selected_menu == "4"):
            print("([0] Untuk membatalkan pilihan)\n\n")
            hapusHistory()
            ulangi = False
        elif (selected_menu == "0"):
            print("([0] Untuk membatalkan pilihan)\n\n")
            exitMenu()
            break
        else:
            print("Kamu memilih menu yang salah!")


user = ""
while (user == ""):
    user = input("\n\nMasukkan Nama anda :    ")
clear()
print("\n\t\t\tSelamat datang!,  {}".format(str.title(user)))
print("\t\t//====================================================\\\\")
print("\t\t|| \t\t\t\t\t\t  === ||")
print("\t\t||\t\t\t\t\t\t      ||")
print("\t\t|| Aplikasi Penghitung Luas dan Keliling Bangun datar ||")
print("\t\t||\t\t\t\t\t\t      ||")
print("\t\t||\t\t\t\t\t\t      ||")
print("\t\t\\\\=========================||=========================//\n\n")
mulaiMenghitung(user)   

print("___________ __            ___               __      ___      |||   ")
print("||||||||||| ||            |||    __  ____   ||      |||      |||   ")
print("    ||      ||  ____     || ||   || |||||   ||    |||        |||   ")
print("    ||      || |||||    ||   ||  ||||   ||| ||  |||          |||   ")
print("    ||      ||||   ||  ||||||||| ||      || |||||            |||   ")
print("    ||      ||      || ||     || ||      || ||  |||          |||   ")
print("    ||      ||      || ||     || ||      || ||    |||              ")
print("    __      __      __ __     __ __      __ __      __       |||   ") 
