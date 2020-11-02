nilai = int(input("masukan nilai indonesia = "))
nilai = int(input("masukan nilai ipa = "))
nilai = int(input("masukan nilai matematika = "))
lulus = "Selamat anda Lulus"
gagal = "maaf, Anda tidak lulus"
validasi = "input benar"
tidakvalidasi = "Maaf, input ada yang tidak valid"
if nilai>=60 :
    print(lulus)
elif nilai<=60 :
    print(gagal)
else :
    print(gagal)

print("sebab ketidaklulusan:")
if nilai<60:
    print("-Nilai bhs indonesia kurang dari 60")
if nilai<60:
    print("-Nilai ipa kurang dari 60")
if nilai<70:
    print("-Nilai matematika kurang dari 70")
