kesempatan = 3
username = "richo"
password = 62

while kesempatan >= 1:
    print("=" * 30)
    user = input("Masukkan username anda: ")
    pw = int(input("Masukkan password anda: "))

    if user == username and pw == password:
        print("Login berhasil :)")

        # Interface menu program
        print("=" * 30)
        print("Menu Program Menghitung")
        print("Luas dan Volume Bangun Ruang")
        print("=" * 30)
        print("Pilih yang ingin Anda hitung")
        print("=" * 30)
        print("1. Kubus")
        print("2. Balok")
        print("3. Tabung")
        print("4. Kerucut")
        print("0. Keluar")
        print("=" * 30)
        
        # Pilihan awal
        ulang = "ya"
        while ulang == "ya":
            pilihan1 = int(input("Masukkan pilihan: "))

        # Percabangan pilihan user
        # Kubus
            if pilihan1 == 1:
                print("=" * 30)
                print("Apa yang ingin Anda cari? ")
                print("1. Luas Kubus")
                print("2. Volume Kubus")
                print("=" * 30)
                pilihan2 = int(input("Masukkan pilihan: "))
                if pilihan2 == 1:
                    print("Luas Kubus")
                    print("3 x sisi x sisi")
                    sisi = int(input("Masukkan sisi kubus (dalam cm): "))
                    luas = 3 * sisi * sisi
                    print(f"Luas Kubus\t: {luas} cm")
                else:
                    print("Volume Kubus")
                    print("sisi x sisi x sisi")
                    sisi = int(input("Masukkan sisi kubus (dalam cm): "))
                    volume = sisi * sisi * sisi
                    print(f"Volume Kubus\t: {volume} cm")

            # Balok
            elif pilihan1 == 2:
                print("=" * 30)
                print("Apa yang ingin Anda cari? ")
                print("1. Luas Balok")
                print("2. Volume Balok")
                print("=" * 30)
                pilihan2 = int(input("Masukkan pilihan: "))
                if pilihan2 == 1:
                    print("Luas Balok")
                    print("2 x (panjang x lebar + panjang x tinggi + lebar x tinggi)")
                    panjang = int(input("Masukkan panjang kubus (dalam cm): "))
                    lebar = int(input("Masukkan lebar kubus (dalam cm): "))
                    tinggi = int(input("Masukkan tinggi kubus (dalam cm): "))
                    luas = 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)
                    print(f"Luas Balok\t: {luas} cm")
                else:
                    print("Volume Balok")
                    print("panjang x lebar x tinggi")
                    panjang = int(input("Masukkan panjang kubus (dalam cm): "))
                    lebar = int(input("Masukkan lebar kubus (dalam cm): "))
                    tinggi = int(input("Masukkan tinggi kubus (dalam cm): "))
                    volume = panjang * lebar * tinggi
                    print(f"Volume Balok\t: {volume} cm")

            # Tabung
            elif pilihan1 == 3:
                print("=" * 30)
                print("Apa yang ingin Anda cari? ")
                print("1. Luas Tabung")
                print("2. Volume Tabung")
                print("=" * 30)
                pilihan2 = int(input("Masukkan pilihan: "))
                if pilihan2 == 1:
                    print("Luas Tabung")
                    print("2 x π x r (t + r)")
                    jari1 = (input("Apakah jari-jari diketahui? (Ya/Tidak) "))
                    if jari1 == "Ya":
                        jari2 = int(input("Masukkan jari-jari (dalam cm): "))
                    else:
                        diameter = int(input("Masukkan diameter (dalam cm): "))
                        jari2 = diameter / 2
                    if jari2 % 7 == 0:
                        π = int(22 / 7)
                    else:
                        π = float(3.14)
                    tinggi = int(input("Masukkan tinggi (dalam cm): "))
                    luas = 2 * π * jari2 * (tinggi + jari2)
                    print(f"Luas Tabung\t: {luas} cm")

                else:
                    print("Volume Tabung")
                    print("π x r x r x t")
                    jari1 = (input("Apakah jari-jari diketahui? (Ya/Tidak) "))
                    if jari1 == "Ya":
                        jari2 = int(input("Masukkan jari-jari (dalam cm): "))
                    else:
                        diameter = int(input("Masukkan diameter (dalam cm): "))
                        jari2 = diameter / 2
                    if jari2 % 7 == 0:
                        π = int(22 / 7)
                    else:
                        π = float(3.14)
                    tinggi = int(input("Masukkan tinggi (dalam cm): "))
                    volume = π * jari2 * jari2 * tinggi
                    print(f"Volume Tabung\t: {volume} cm")

            # kerucut
            elif pilihan1 == 4:
                print("=" * 30)
                print("Apa yang ingin Anda cari? ")
                print("1. Luas Kerucut")
                print("2. Volume Kerucut")
                print("=" * 30)
                pilihan2 = int(input("Masukkan pilihan: "))
                if pilihan2 == 1:
                    print("Luas Kerucut")
                    print("π x r (r + s)")
                    jari1 = (input("Apakah jari-jari diketahui? (Ya/Tidak) "))
                    if jari1 == "Ya":
                        jari2 = int(input("Masukkan jari-jari (dalam cm): "))
                    else:
                        diameter = int(input("Masukkan diameter (dalam cm): "))
                        jari2 = diameter / 2
                    if jari2 % 7 == 0:
                        π = int(22 / 7)
                    else:
                        π = float(3.14)
                    pelukis = int(input("Masukkan garis pelukis (dalam cm): "))
                    luas = π * jari2 * (jari2 + pelukis)
                    print(f"Luas Tabung\t: {luas} cm")

                else:
                    print("Volume Kerucut")
                    print("1/2 x π x r x r x t")
                    jari1 = (input("Apakah jari-jari diketahui? (Ya/Tidak) "))
                    if jari1 == "Ya":
                        jari2 = int(input("Masukkan jari-jari (dalam cm): "))
                    else:
                        diameter = int(input("Masukkan diameter (dalam cm): "))
                        jari2 = diameter / 2
                    if jari2 % 7 == 0:
                        π = int(22 / 7)
                    else:
                        π = float(3.14)
                    tinggi = int(input("Masukkan tinggi (dalam cm): "))
                    volume = 1 / 2 * π * jari2 * jari2 * tinggi
                    print(f"Luas Tabung\t: {volume} cm")
            

            # Pilihan  untuk membersihkan layar dan pilihan selain yang ada di menu   
            elif pilihan1 == 0:
                import os
                
                # Membersihkan layar terminal
                os.system("cls")

                exit("Keluar dari Program")

            else:
                print("Masukkan nomor yang benar dong :( ")
            ulang = input("Ingin menghitung lagi? ")

            if ulang == "tidak":
                exit("Keluar Program")

    else:
        print("Username atau Password anda salah!")
        kesempatan -= 1
        if kesempatan == 0:
            print("Keluar dari program")