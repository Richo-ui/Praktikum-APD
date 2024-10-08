import os

# membersihkan layar
def clear_screen():
    os.system('cls')

# list untuk menyimpan data user (username, password, role)
users = [["admin", "admin123", "admin"]]
atlet_list = [] 

# Fungsi untuk login
def login():
    clear_screen()
    print("--- Login ---")
    username = input("Username: ")
    password = input("Password: ")
    
    # Cek user di dalam database users
    for user in users:
        if user[0] == username and user[1] == password:
            print(f"\nSelamat datang, {username}!")
            return user[2]
    
    print("\nUsername atau password salah!")
    input("Tekan Enter untuk kembali ke login...")
    return None

# Fungsi untuk register
def register():
    clear_screen()
    print("--- Register ---")
    username = input("Masukkan username baru: ")
    password = input("Masukkan password baru: ")
    
    # Cek apakah username sudah ada
    for user in users:
        if user[0] == username:
            print("\nUsername sudah ada!")
            input("Tekan Enter untuk kembali ke menu...")
            return
    
    users.append([username, password, "user"])
    print(f"\nPengguna {username} berhasil didaftarkan!")
    input("Tekan Enter untuk kembali ke menu...")

# Fungsi untuk menambahkan atlet (hanya admin)
def tambah_atlet():
    clear_screen()
    print("\n--- Tambah Atlet Baru ---")
    try:
        nama = input("Masukkan Nama Atlet: ")
        usia = int(input("Masukkan Usia Atlet: "))
        cabang = input("Masukkan Cabang Olahraga: ")
        posisi = input("Masukkan Posisi Atlet: ")
        statistik = input("Masukkan Statistik: ")
        prestasi = input("Masukkan Prestasi: ")
        
        # Data atlet sebagai list 
        atlet = [nama, usia, cabang, posisi, statistik, prestasi]
        
        # Menambahkan atlet ke dalam list
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
            print(f"{index + 1}. {atlet[0]} - {atlet[1]} - {atlet[2]} - {atlet[3]} - {atlet[4]} - {atlet[5]}")
    input("\nTekan Enter untuk kembali ke menu...")

# Fungsi untuk mengedit informasi atlet (hanya admin)
def edit_atlet():
    clear_screen()
    lihat_atlet()
    if len(atlet_list) > 0:
        try:
            pilihan = int(input("Pilih nomor atlet yang ingin diedit: "))
            if 1 <= pilihan <= len(atlet_list):
                atlet = atlet_list[pilihan - 1]
                print(f"\n--- Edit Informasi Atlet {atlet[0]} ---")
                atlet[0] = input(f"Nama ({atlet[0]}): ") or atlet[0]
                atlet[1] = input(f"Usia ({atlet[1]}): ") or atlet[1]
                atlet[2] = input(f"Cabang ({atlet[2]}): ") or atlet[2]
                atlet[3] = input(f"Posisi ({atlet[3]}): ") or atlet[3]
                atlet[4] = input(f"Statistik ({atlet[4]}): ") or atlet[4]
                atlet[5] = input(f"Prestasi ({atlet[5]}): ") or atlet[5]
                print(f"\nAtlet {atlet[0]} berhasil diupdate!\n")
            else:
                print("\nPilihan tidak valid!")
        except ValueError:
            print("\nInput tidak valid. Harap masukkan nomor yang benar.")
        input("\nTekan Enter untuk kembali ke menu...")

# Fungsi untuk menghapus atlet (hanya admin)
def hapus_atlet():
    clear_screen()
    lihat_atlet()
    
    if len(atlet_list) > 0:
        try:
            pilihan = int(input("Pilih nomor atlet yang ingin dihapus: "))
            if 1 <= pilihan <= len(atlet_list):
                atlet = atlet_list.pop(pilihan - 1)
                print(f"\nAtlet {atlet[0]} berhasil dihapus!\n")
            else:
                print("\nPilihan tidak valid!")
        except ValueError:
            print("\nInput tidak valid. Harap masukkan nomor yang benar.")
    input("\nTekan Enter untuk kembali ke menu...")

# Fungsi utama untuk menampilkan menu
def menu_utama(role):
    while True:
        clear_screen()
        print("=== Menu Manajemen Atlet ===")
        print("1. Tambah Atlet") if role == 'admin' else None
        print("2. Lihat Daftar Atlet")
        print("3. Edit Informasi Atlet") if role == 'admin' else None
        print("4. Hapus Atlet") if role == 'admin' else None
        print("5. Keluar")
        
        try:
            pilihan = int(input("Pilih opsi: "))
            if role == "admin":
                if pilihan == 1:
                    tambah_atlet()
                elif pilihan == 2:
                    lihat_atlet()
                elif pilihan == 3:
                    edit_atlet()
                elif pilihan == 4:
                    hapus_atlet()
                elif pilihan == 5:
                    clear_screen()
                    print("Terima kasih telah menggunakan aplikasi!")
                    break
                else:
                    print("\nPilihan tidak valid.")
            else:  # Jika pengguna adalah 'user'
                if pilihan == 2:
                    lihat_atlet()
                elif pilihan == 5:
                    clear_screen()
                    print("Terima kasih telah menggunakan aplikasi!")
                    break
                else:
                    print("\nPilihan tidak valid.")
        except ValueError:
            print("\nInput tidak valid. Harap masukkan angka.")
        input("\nTekan Enter untuk melanjutkan...")

# Fungsi untuk menampilkan menu awal (login/register)
def menu_awal():
    while True:
        clear_screen()
        print("=== Menu Awal ===")
        print("1. Login")
        print("2. Register")
        print("3. Keluar")
        
        try:
            pilihan = int(input("Pilih opsi: "))
            if pilihan == 1:
                role = login()
                if role:
                    menu_utama(role)
            elif pilihan == 2:
                register()
            elif pilihan == 3:
                clear_screen()
                print("Terima kasih telah menggunakan aplikasi!")
                break
            else:
                print("\nPilihan tidak valid.")
        except ValueError:
            print("\nInput tidak valid. Harap masukkan angka.")
        input("\nTekan Enter untuk melanjutkan...")

# Menjalankan menu awal
menu_awal()
