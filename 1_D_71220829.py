afsno=int(input("Masukkan jumlah uang: Rp"))
isan=(input("Ketik 'START' untuk memulai: "))
def count_upper_lower(asdfg):
    kkkk = 0
    hgf = 0
    for ffaf in asdfg:
        if ffaf.isupper():
            kkkk += 1
        elif ffaf.islower():
            hgf += 1
    print("Upper Case Count is %d Lower Case Count is %d " %(kkkk, hgf))

count_upper_lower(isan)

jiad=(input("Apa barang yang akan Anda beli? "))
if jiad == ("susu"):
    print ("Sisa uang Anda ",afsno-20000)
elif jiad == ("permen"):
    print ("Sisa uang Anda ",afsno-500)
elif jiad == ("roti"):
    print ("Sisa uang Anda ",afsno-15000)
elif jiad == ("roti"):
    print ("Sisa uang Anda ",afsno-15000)
elif jiad == ("indomie"):
    print ("Sisa uang Anda ",afsno-3000)
elif jiad == ("vitamin"):
    print ("Sisa uang Anda ",afsno-50000)
else: 
    (print(jiad))