#Program menghitung waktu tempuh

#deklarasi
waktutempuh=0.0
jarak=0.0
kecepatan=0.0

while True:
  print("+=====================================================================+")
  print("|                      SELAMAT DATANG DI PROGRAM                      |")
  print("|                 PENGHITUNG ESTIMASI WAKTU PERJALANAN                |")
  print("|                              (Via Tol)                              |")
  print("|_____________________________________________________________________|")
  print("|                     By : Kinanthi Putri Ariyani                     |")
  print("+=====================================================================+")
  print("+=====================================================================+")
  print("|                                Fitur                                |")
  print("+=====================================================================+")
  print("|   1. Jogjakarta - Malang*                                           |")
  print("|   2. Surabaya - Mojokerto*                                          |")
  print("|   3. Kediri - Jakarta*                                              |")
  print("|   4. Custom                                                         |")
  print("|   5. Keluar program                                                 |")
  print("|   *sering dicari                                                    |")
  print("+=====================================================================+")
  print(" ")
  user = int(input("Pilih fitur yang ingin anda pakai [1-5] :"))

  if user==1:
    print("+=====================================================================+")
    print("|                     ESTIMASI WAKTU PERJALANAN                       |")
    print("|                       Jogjakarta - Malang                           |")
    print("|                           (Via Tol)                                 |")
    print("+=====================================================================+")
    jarakantarkota = 394
    kecepatan = input("Kecepatan kendaraan (km/h) :")
    kecepatan = float(kecepatan) #casting string to float
    kecepatan = round(kecepatan)
    waktutempuh = jarakantarkota/kecepatan #menghitung waktu tempuh 
    waktutempuh = round(waktutempuh) #membulatkan nilai hasil dari waktu tempuh
    kota = print("Jogjakarta - Malang")
    print("Dengan kecepatan", kecepatan, "(km/h) anda akan mendapatkan estimasi waktu perjalanan dari Jogjakarta - Malang selama", waktutempuh, "jam")
    print(" ")
    lanjut_fitur = input("Apakah anda ingin mencoba fitur lain ?(y/n) : ")
    if lanjut_fitur=='y':
      print(" ")
    elif lanjut_fitur=='n':
      print("+=====================================================================+")
      print("|             Terima Kasih telah menggunakan program ini              |")
      print("|                        Sampai jumpa lagi...                         |")
      print("+=====================================================================+")
      break

  elif user==2:
    print("+=====================================================================+")
    print("|                     ESTIMASI WAKTU PERJALANAN                       |")
    print("|                       Surabaya - Mojokerto                          |")
    print("|                           (Via Tol)                                 |")
    print("+=====================================================================+")
    jarakantarkota = 64
    kecepatan = input("Kecepatan kendaraan (km/h) :")
    kecepatan = float(kecepatan) #casting string to float
    kecepatan = round(kecepatan)
    waktutempuh = jarakantarkota/kecepatan #menghitung waktu tempuh 
    waktutempuh = round(waktutempuh) #membulatkan nilai hasil dari waktu tempuh
    kota = print("Surabaya - Mojokerto")
    print("Dengan kecepatan", kecepatan, "(km/h) anda akan mendapatkan estimasi waktu perjalanan dari Surabaya - Mojokerto selama", waktutempuh, "jam")
    print(" ")
    lanjut_fitur = input("Apakah anda ingin mencoba fitur lain ?(y/n) : ")
    if lanjut_fitur=='y':
      print(" ")
    elif lanjut_fitur=='n':
      print("+=====================================================================+")
      print("|             Terima Kasih telah menggunakan program ini              |")
      print("|                        Sampai jumpa lagi...                         |")
      print("+=====================================================================+")
      break

  elif user==3:
    print("+=====================================================================+")
    print("|                     ESTIMASI WAKTU PERJALANAN                       |")
    print("|                         Kediri - Jakarta                            |")
    print("|                            (Via Tol)                                |")
    print("+=====================================================================+")
    arakantarkota = 709
    kecepatan = input("Kecepatan kendaraan (km/h) :")
    kecepatan = float(kecepatan) #casting string to float
    kecepatan = round(kecepatan)
    waktutempuh = jarakantarkota/kecepatan #menghitung waktu tempuh 
    waktutempuh = round(waktutempuh) #membulatkan nilai hasil dari waktu tempuh
    kota = print("Kediri - Jakarta")
    print("Dengan kecepatan", kecepatan, "(km/h) anda akan mendapatkan estimasi waktu perjalanan dari Kediri - Jakarta selama", waktutempuh, "jam")
    print(" ")
    lanjut_fitur = input("Apakah anda ingin mencoba fitur lain ?(y/n) : ")
    if lanjut_fitur=='y':
      print(" ")
    elif lanjut_fitur=='n':
      print("+=====================================================================+")
      print("|             Terima Kasih telah menggunakan program ini              |")
      print("|                        Sampai jumpa lagi...                         |")
      print("+=====================================================================+")
      break

  elif user==4:
    print("+=====================================================================+")
    print("|                     ESTIMASI WAKTU PERJALANAN                       |")
    print("|                              CUSTOM                                 |")
    print("+=====================================================================+")
    a = input("Masukkan kota asal :")
    b = input("Masukkan kota tujuan :")
    jarak = input("Jarak antarkota (km) :")
    jarak = float(jarak) #casting string to float
    kecepatan = input("Kecepatan kendaraan (km/h) :")
    kecepatan = float(kecepatan) #casting string to float
    kecepatan = round(kecepatan)
    waktutempuh = jarak/kecepatan #menghitung waktu tempuh 
    waktutempuh = round(waktutempuh) #membulatkan nilai hasil dari waktu tempuh
    kota = print(a, "-", b)
    print("Dengan kecepatan", kecepatan, "(km/h) anda akan mendapatkan estimasi waktu perjalanan dari", a, "-", b, "selama", waktutempuh, "jam")
    print(" ")
    lanjut_fitur = input("Apakah anda ingin mencoba fitur lain ?(y/n) : ")
    if lanjut_fitur=='y':
      print(" ")
    elif lanjut_fitur=='n':
      print("+=====================================================================+")
      print("|             Terima Kasih telah menggunakan program ini              |")
      print("|                        Sampai jumpa lagi...                         |")
      print("+=====================================================================+")
      break
      
  elif user==5:
    print("+=====================================================================+")
    print("|             Terima Kasih telah menggunakan program ini              |")
    print("|                        Sampai jumpa lagi...                         |")
    print("+=====================================================================+")
    break
