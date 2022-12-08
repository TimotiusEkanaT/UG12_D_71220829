print ("~~~~~ Table Matematika Nich ~~~~~")
print ("Pilihan Model Matematika")
print ("1. Perkalian")
print ("2. Pembagian")

juhh=int(input("Masukkan model matematika yang diinginkan 1/2 : "))
ijji=int(input("Menampilkan tabel matematika dengan angka:"))

if juhh == 1:
    for kl in range (1,11):
        print (ijji, "x", kl, "=",ijji*kl)

elif juhh == 2:
    for ad in range (49,66):
        print (ad, ":", ijji, "=",ad/ijji)

else:
    print ("Pilihan tidak tersedia, jangan ngasal!")