nilai = int(input("masukan nilai bhs indonesia = "))
nilai = int(input("masukan nilai ipa = "))
nilai = int(input("masukan nilai matematika = "))
lulus = "Selamat anda Lulus"
gagal = "maaf, Anda tidak lulus"
validasi = "input benar"
tidakvalidasi = "Maaf, input ada yang tidak valid"
if nilai>=60 :
    print(validasi)
elif nilai<=60 :
    print(tidakvalidasi)
else :
    print(tidakvalidasi)
