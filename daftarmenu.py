# list makanan dan minuman
menu_makanan = ["Ayam Goreng", "Ayam Bakar","Ayam Tulang Lunak"]
menu_minuman = ["Es Teh","Teh Hangat","Teh GreenTea"]

# cetak daftar makanan dan minuman
print("Daftar Makanan")
for daftar_makanan in menu_makanan:
    print(daftar_makanan)
print("\n")
print("Daftar Minuman")
for daftar_minuman in menu_minuman:
    print(daftar_minuman)

# memesan makanan dan minuman
print("\n")
pesan_makanan = input("Pesan Makanan: ")
porsi_makanan = int(input("Berapa Porsi: "))
pesan_minuman = input("Pesan Minuman: ")
porsi_minuman = int(input("Berapa Porsi: "))

#cek yang di pesan ada dalam menu atau tidak
if pesan_makanan in menu_makanan and pesan_minuman in menu_minuman:
    print(pesan_makanan ,"dan",pesan_minuman,"tersedia")
    print("Saya Memesan",pesan_makanan,"Sebanyak",porsi_makanan,"porsi dan",pesan_minuman,"Sebanyak",porsi_minuman,"porsi")
elif pesan_makanan in menu_makanan or pesan_minuman in menu_minuman:
    print(pesan_minuman,"atau",pesan_minuman,"tidak tersedia")
else:
    print("Silahkan Pesan Kembali")
