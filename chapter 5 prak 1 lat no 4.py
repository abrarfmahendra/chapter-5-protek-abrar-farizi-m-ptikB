lagi='y'

while lagi=='y':

    print ("\t \t Aplikasi Perhitungan Gaji Karyawan")

    print ("===============================================================================")

    kode=input("Masukan kode karyawan \t: ")

    nama=input("Masukan Nama karyawan/Staff \t: ")

    print ("rincian gaji karyawan A,B,C,D")

    golongan=input("Masukan golongan \t\t: ")

    if (golongan=='A'):

        gajipokok = 10000000
        potongan = 2.5

    elif(golongan=='B'):

        gajipokok = 8500000
        potongan = 2


    elif(golongan=='C'):

        gajipokok = 7000000
        potongan = 1.5


    elif(golongan=='D'):

        gajipokok = 5500000
        potongan = 1

    potongan = gajipokok * (potongan/100)
    gajibersih= gajipokok - potongan

    print ("")

    print ("\n")

    print ("===============================================================================")

    print ("\t\t\t struck gaji bulanan")

    print ("")

    print ("kode \t\t: ",kode)

    print ("Nama \t\t: ",nama)

    print ("golongan \t: ",golongan)

    print ("potongan \t\t: ",potongan)
    print ("gaji pokok \t\t:Rp",gajipokok)
    print ("gaji bersih \t\t:Rp",gajibersih)
    print ("")

    print ("===============================================================================")

    print ("")

    lagi=input("Ambil Data Lagi [y/n]? : ")
