import getpass

while True :
    login =print("-------Login-------")

    name_1 =input("Buat username baru anda: ")
    pass_1 =input("Buat NIM anda : ")
    print("\n---------------TERKONFIRMASI---------------")
    name_2 =input("Masukkan username anda: ")
    pass_2 =getpass.getpass("Masukkan NIM anda : ")

    if name_2==name_1 and pass_2==pass_1 :
        print("-----------------------------------------")
        print("Login anda berhasil, selamat datang " + name_1 + "!!")
        print("-----------------------------------------")
        Harga_barang =int(input("Masukkan harga barang :Rp "))
        Jumlah_pembelian =int(input("Jumlah pembelian : "))
        bayar =Harga_barang*Jumlah_pembelian
        print()
        if bayar > 250000 :
            diskon =bayar*25/100
            total =bayar - diskon
            print("SELAMAT!, anda mendapatkan diskon 25%")
            print()
        elif Harga_barang < 250000 :
            total =bayar
            print("Anda tidak mendapatkan diskon")
            print()
        else :
            total = bayar

        print("Total Biaya :",bayar)
        print("Total yang harus kamu bayar :",total)

        while True:
            print("-----------------------------------------------------")
            lanjut = input("Apakah anda ingin menghitung total harga lagi?\nTekan (iya/tidak):")
            if lanjut == 'iya':
                Harga_barang =int(input("Masukkan harga barang :Rp "))
                Jumlah_pembelian =int(input("Jumlah pembelian : "))
                bayar =Harga_barang*Jumlah_pembelian
                print() 
                if bayar > 250000 :
                    diskon =bayar*25/100
                    total =bayar - diskon
                    print("Selamat!, anda mendapatkan diskon 25%")
                    print()
                elif Harga_barang < 250000 :
                    total =bayar
                    print("Anda tidak mendapatkan diskon")
                    print()
                else :
                    total = bayar

                print("Total Biaya :",bayar)
                print("Total yang harus kamu bayar :",total)
            elif lanjut == 'tidak':
                break #Program selesai
        print("Penghitungan selesai. Thankyouu!!!")
        print("----------------------------------------------------")
        break

    else :
        print("-----------------------------------------")
        print("Login ditolak, coba lagi!                ")
        print("-----------------------------------------")
        break