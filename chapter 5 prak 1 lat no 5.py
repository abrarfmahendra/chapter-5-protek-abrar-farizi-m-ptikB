lagi='y'

while lagi=='y':

    print ("\t \t Aplikasi Perhitungan Gaji Karyawan")

    print ("===============================================================================")

    kode=input("Masukan kode karyawan \t: ")

    nama=input("Masukan Nama karyawan/Staff \t: ")

    print ("rincian gaji karyawan A,B,C,D")

    golongan=input("Masukan golongan \t\t: ")
    status =input("masukan status:")
    if (status=='menikah'):
        jumlah=input("masukan jumlah anak:")
   
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

    if ( status == 'menikah' ):
        tunjanganIstriSuami= gajipokok * (10/100)
        tunjanganAnak= gajipokok *(5/100)* jumlahanak
        gajikotor= gajipokok + tunjanganIstriSuami + tunjanganAnak
        gajibersih= gajikotor - potongan

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

    print ("status \t\t: ", status)
    print ("jumlah anak \t\t:Rp",jumlahanak)

    print ("===============================================================================")
    print ("gaji pokok \t\t:Rp",gajipokok)
    print ("tunjangan istri/suami:Rp",tunjanganIstriSuami)
    print ("tunjangan anak:Rp",tunjanganAnak)

    print ("===============================================================================")

    print ("gaji kotor:Rp",gajikotor)
    print ("potongan:Rp",potongan)

    print ("===============================================================================")

    print ("gaji bersih:Rp",gajibersih)
