# TUGAS BESAR PENGENALAN KOMPUTASI K-39
# "Automatic Parking Gate"

# Kelompok 9 K-39
#   Muhammad Abrar Adhyatama        (16924163)
#   Aldy Nahri Rafansyah            (16924165)
#   Aditya Rianda Subarkah          (16924168)
#   Julius Kevin Saputra            (16924169)
#   Akmal Nizam Aminudin            (16924177)
#   Reynaldi Putra Langit           (16924178)


#Errors, errors and errors
#Can't seem to solve it 
#Will continue tommorrow

# Deskripsi : Program sistem parkir otomatis dengan metode pembayaran non tunai

# KAMUS
# a, JK               : string
# JP, JKEL, saldo, IS : integer
# i, j                : integer
# bayar               : array of integer

# ALGORITMA

# Menampilkan layar utama
print("-------------------------------------------------------")
print("                                                       ")
print("                    Selamat Datang!                    ")
print(" Silahkan Tempel Kartu Member atau Tekan Tombol Tiiket ")
print("                                                       ")
print("-------------------------------------------------------")


# Menampilkan daftar harga parkir
print("   Jam Parkir   |  Motor  |  Mobil  | Box/Truk/Pickup |")
print("  2 Jam Pertama |  1500   |  3000   |      5000       |")
print(" Jam Berikutnya |  1500   |  3000   |      5000       |")
print("-------------------------------------------------------")
print("                                                       ")
print("                                                       ")
print("                                                       ")

# Input Jenis Pembayaran (Tiket/Member)
Opt_one = str(input("             (T)iket atau (K)artu Member?               ")
    if Opt_one == T or Opt_one == ("Tiket");
        print("                    Mencetak Tiket,                    ")
        print("                   .................                   ")
        print("                    Silahkan Masuk!                    ")
    elif Opt_one == ("K") or Opt_one == ("Kartu Member");
        NM = str(input("Nama: ")
        print("          Selamat Datang, " + (NM) " !")
        print("                   .................                   ")
        print("                    Silahkan Masuk!                    ")
    else;
        print(Opt_one)

# Input jam saat ingin parkir
JP = int(input("Jam masuk: "))
print(JP)
if JP>24 or JP<0:
    while JP>24 or JP<0:
        print("harap masukkan jam parkir dengan benar!")
        JP = int(input("Harap masukkan jam berapa anda parkir: "))
    print(JP)
    
# Input metode pembayaran
print("Apakah anda ingin cetak karcis atau tap e-money?")
a = input("karcis atau emoney? ")
if (a=="karcis" or a=="emoney")==False:
    while a!="karcis" and a!="emoney" :
        print("Harap masukkan cara bayar dengan benar!")
        a = input("karcis atau emoney? ")
print("Gate terbuka!")
print()

# Input jam saat ingin keluar
JKEL = int(input("Jam berapa anda keluar: "))
if JKEL<0 or JKEL>24:
    while JKEL>24 or JKEL<0:
        print("Harap masukkan jam keluar dengan benar!")
        JKEL = int(input("Jam berapa anda keluar: "))
if JKEL<=JP:
    JKEL = JKEL + 24
TJP = JKEL - JP
print("Anda parkir selama",TJP," jam")
print()

# Input nomimal saldo
saldo = int(input("Masukkan saldo anda: "))

# Input jenis kendaraan yang diparkirkan
JK = input("Apa jenis kendaraan anda? ")
if (JK=="motor" or JK=="mobil")==False:
    while JK!="motor" and JK!="mobil":
        print("Harap masukkan jenis kendaraan anda dengan benar!")
        JK = input("Apa jenis kendaraan anda? ")
print()

# Pengulangan untuk menentukan harga
# Kondisi saat memarkir motor dan membayar dengan karcis
if JK=="motor" and a=="karcis":
    if TJP == 1:
        harga = 4000
    elif TJP == 2:
        harga = 6000
    else:
        harga = 2000*TJP
    print("Scan karcis berhasil")
    print("harga yang harus dibayar adalah sebesar Rp.",harga)
    print()
    if saldo<harga:
    # Kondisi saat saldo tidak cukup
        while saldo<harga:
            print("Saldo anda tidak cukup, harap lakukan pengisian saldo")
            IS = int(input("Berapa banyak akan isi saldo? "))
            saldo = saldo + IS
            SSAL = saldo - harga
        print("Saldo anda sekarang sebesar Rp",saldo)
        print()
        print("Scan karcis berhasil")
        print("Pembayaran berhasil dan saldo anda berkurang sebesar Rp",harga)
        print("Sisa saldo anda Rp.",SSAL)
        print()
        print("Gate terbuka!")
        print("Selamat berkendara, terima kasih telah menggunakan jasa parkir otomatis kelompok 7")
    elif saldo>=harga:
    # Kondisi saat saldo cukup
        SSAL = saldo - harga
    print("Pembayaran berhasil dan saldo anda berkurang sebesar Rp",harga)
    print("Sisa saldo anda Rp.",SSAL)
    print()
    print("Gate terbuka!")
    print("Selamat berkendara, terima kasih")
  
# Kondisi saat memarkir motor dan membayar dengan emoney
elif JK=="motor" and a=="emoney":
    if TJP == 1:
        harga = 4000
    elif TJP == 2:
        harga = 6000
    else:
        harga = 2000*TJP
    print("Tap kartu berhasil")
    print("harga yang harus dibayar adalah sebesar Rp.",harga)
    print()
    if saldo<harga:
    # Kondisi saat saldo tidak cukup
        while saldo<harga:
            print("Saldo anda tidak cukup, harap lakukan pengisian saldo")
            IS = int(input("Berapa banyak akan isi saldo? "))
            saldo = saldo + IS
            SSAL = saldo - harga
            print("Saldo anda sekarang sebesar Rp",saldo)
            print()
        print("pembayaran berhasil dan saldo anda berkurang sebesar Rp",harga)
        print("Sisa saldo anda Rp.",SSAL)
        print()
        print("Gate terbuka!")
        print("Selamat berkendara, terima kasih")
    elif saldo>=harga:
    # Kondisi saat saldo cukup
        SSAL = saldo - harga
    print("Pembayaran berhasil dan saldo anda berkurang sebesar Rp",harga)
    print("Sisa saldo anda Rp.",SSAL)
    print()
    print("Gate terbuka!")
    print("Selamat berkendara, terima kasih")
  
# Kondisi saat memarkir mobil dan membayar dengan karcis
elif JK=="mobil" and a=="karcis":
    if TJP == 1:
        harga = 6000
    elif TJP == 2:
        harga = 9000
    else:
        harga = 4000*TJP
    print("Scan karcis berhasil")
    print("harga yang harus dibayar adalah sebesar Rp.",harga)
    print()
    if saldo<harga:
        # Kondisi saat saldo tidak cukup
        while saldo<harga:
            print("Saldo anda tidak cukup, harap lakukan pengisian saldo")
            IS = int(input("Berapa banyak akan isi saldo? "))
            saldo = saldo + IS
            SSAL = saldo - harga
        print("Saldo anda sekarang sebesar Rp",saldo)
        print()
        print("Pembayaran berhasil dan saldo anda berkurang sebesar Rp",harga)
        print("Sisa saldo anda Rp.",SSAL)
        print()
        print("Gate terbuka!")
        print("Selamat berkendara, terima kasih")
    elif saldo>=harga:
        # Kondisi saat saldo cukup
        SSAL = saldo - harga
        print("Pembayaran berhasil dan saldo anda berkurang sebesar Rp",harga)
        print("Sisa saldo anda Rp.",SSAL)
        print()
        print("Gate terbuka!")
        print("Selamat berkendara, terima kasih")
        
# Kondisi saat memarkir mobil dan membayar dengan emoney
elif JK=="mobil" and a=="emoney":
    if TJP == 1:
        harga = 6000
    elif TJP == 2:
        harga = 9000
    else:
        harga = 4000*TJP
    print("Tap kartu berhasil")
    print("harga yang harus dibayar adalah sebesar Rp.",harga)
    print()
    if saldo<harga:
        # Kondisi saat saldo tidak cukup
        while saldo<harga:
            print("Saldo anda tidak cukup, harap lakukan pengisian saldo")
            IS = int(input("Berapa banyak akan isi saldo? "))
            saldo = saldo + IS
            SSAL = saldo - harga
        print("Saldo anda sekarang sebesar Rp",saldo)
        print()
        print("Pembayaran berhasil dan saldo anda berkurang sebesar Rp",harga)
        print("Sisa saldo anda Rp.",SSAL)
        print()
        print("Gate terbuka!")
        print("Selamat berkendara, terima kasih")
    elif saldo>=harga:
        # Kondisi saat saldo cukup
        SSAL = saldo - harga
        print("Pembayaran berhasil dan saldo anda berkurang sebesar Rp",harga)
        print("Sisa saldo anda Rp.",SSAL)
        print()
        print("Gate terbuka!")
        print("Selamat berkendara, terima kasih")
