print ();
print ('Masukkan Batas Awal:');awal = input();
print ('Masukkan Batas Akhir:'); akhir = input();
a = int (awal);
b = int (akhir);
for ganjil in range (a,b,1):
    if ganjil % 2 == 1 : print (ganjil);
