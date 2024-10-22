import os
from utility import clear_screen, validasi_input

atlet_list = [
    {
        "nama": "Erling Haaland",
        "usia": 24,
        "cabor": "Sepak Bola",
        "posisi": "Penyerang",
        "statistik": "27 Gol, 5 Assist",
        "prestasi": "Golden Boy 2020"
    },
    {
        "nama": "Stephen Curry",
        "usia": 36,
        "cabor": "Basket",
        "posisi": "Point Guard",
        "statistik": "26.4 Poin, 4.5 Rebound",
        "prestasi": "MVP NBA 2022"
    }
] 

# Fungsi untuk menambahkan atlet (hanya admin)
def tambah_atlet():
    clear_screen()
    print("\n--- Tambah Atlet Baru ---")
    try:
        nama = input("Masukkan Nama Atlet: ")
        usia = validasi_input("Masukkan Usia Atlet: ", int)
        cabang = input("Masukkan Cabang Olahraga: ")
        posisi = input("Masukkan Posisi Atlet: ")
        statistik = input("Masukkan Statistik: ")
        prestasi = input("Masukkan Prestasi: ")
        
        # Data atlet sebagai dictionary 
        atlet = {
            "nama" : nama, 
            "usia" : usia, 
            "cabor" : cabang, 
            "posisi" : posisi, 
            "statistik" : statistik, 
            "prestasi" : prestasi
        }
        
        # Menambahkan atlet ke dalam dictionary
        atlet_list.append(atlet)
        print(f"\nAtlet {nama} berhasil ditambahkan!\n")
    except ValueError:
        print("\nInput usia harus berupa angka!")
    
    input("Tekan Enter untuk kembali ke menu...")

# Fungsi untuk melihat daftar atlet (nama - usia - cabor - posisi - statistik - prestasi)
def lihat_atlet():
    clear_screen()
    if len(atlet_list) == 0:
        print("\nTidak ada atlet yang terdaftar.")
    else:
        print("\n--- Daftar Atlet ---")
        for index, atlet in enumerate(atlet_list):
            print(f"Atlet {index + 1}")
            print(f"  Nama    \t:{atlet['nama']}") 
            print(f"  Usia    \t:{atlet['usia']}") 
            print(f"  Cabang  \t:{atlet['cabor']}") 
            print(f"  Posisi  \t:{atlet['posisi']}")
            print(f"  Statistik\t:{atlet['statistik']}")
            print(f"  Prestasi \t:{atlet['prestasi']}")
            print("-" * 30)
    input("\nTekan Enter untuk kembali ke menu...")

# Fungsi untuk mengedit informasi atlet (hanya admin)
def edit_atlet():
    clear_screen()
    lihat_atlet()
    if len(atlet_list) > 0:
        try:
            pilihan = validasi_input("Pilih nomor atlet yang ingin diedit: ", int)
            if 1 <= pilihan <= len(atlet_list):
                atlet = atlet_list[pilihan - 1]
                print(f"\n--- Edit Informasi Atlet {atlet['nama']} ---")
                atlet["nama"] = input(f"Nama ({atlet['nama']}): ") or atlet["nama"]
                atlet["usia"] = validasi_input(f"Usia ({atlet['usia']}): ", int) or atlet["usia"]
                atlet["cabor"] = input(f"Cabang ({atlet['cabor']}): ") or atlet["cabor"]
                atlet["posisi"] = input(f"Posisi ({atlet['posisi']}): ") or atlet["posisi"]
                atlet["statistik"] = input(f"Statistik ({atlet['statistik']}): ") or atlet["statistik"]
                atlet["prestasi"] = input(f"Prestasi ({atlet['prestasi']}): ") or atlet["prestasi"]
                print(f"\nAtlet {atlet['nama']} berhasil diupdate!\n")
            else:
                print("\nPilihan tidak valid!")
        except ValueError:
            print("\nInput tidak valid. Harap masukkan nomor yang benar.")

# Fungsi untuk menghapus atlet (hanya admin)
def hapus_atlet():
    clear_screen()
    lihat_atlet()
    
    if len(atlet_list) > 0:
        try:
            pilihan = validasi_input("Pilih nomor atlet yang ingin dihapus: ", int)
            if 1 <= pilihan <= len(atlet_list):
                atlet = atlet_list.pop(pilihan - 1)
                print(f"\nAtlet {atlet['nama']} berhasil dihapus!\n")
            else:
                print("\nPilihan tidak valid!")
        except ValueError:
            print("\nInput tidak valid. Harap masukkan nomor yang benar.")