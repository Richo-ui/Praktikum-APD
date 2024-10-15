import os

# Fungsi untuk membersihkan layar
def clear_screen():
    os.system('cls')

# dictionary untuk menyimpan data user (username, password, role)
users = [{
    "user" : "admin", 
    "pw" : "admin123", 
    "role" : "admin"
}]

atlet_list = [] 

# Fungsi untuk login
def login():
    clear_screen()
    print("--- Login ---")
    username = input("Username: ")
    password = input("Password: ")
    
    # Cek user di dalam database users
    for user in users:
        if user["user"] == username and user["pw"] == password:
            print(f"\nSelamat datang, {username}!")
            return user["role"]
    
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
        if user["user"] == username:
            print("\nUsername sudah ada!")
            input("Tekan Enter untuk kembali ke menu...")
            return
    
    users.append({"user": username, "pw": password, "role": "user"})
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
        
        # Data atlet sebagai dictionary 
        atlet = {
            "nama" : nama, 
            "usia" : usia, 
            "cabor" : cabang, 
            "posisi" : posisi, 
            "statistik" : statistik, 
            "prestasi" : prestasi
        }
        
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
            print(f"{index + 1}. {atlet['nama']} - {atlet['usia']} - {atlet['cabor']} - {atlet['posisi']} - {atlet['statistik']} - {atlet['prestasi']}")
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
                print(f"\n--- Edit Informasi Atlet {atlet['nama']} ---")
                atlet["nama"] = input(f"Nama ({atlet['nama']}): ") or atlet["nama"]
                atlet["usia"] = input(f"Usia ({atlet['usia']}): ") or atlet["usia"]
                atlet["cabor"] = input(f"Cabang ({atlet['cabor']}): ") or atlet["cabor"]
                atlet["posisi"] = input(f"Posisi ({atlet['posisi']}): ") or atlet["posisi"]
                atlet["statistik"] = input(f"Statistik ({atlet['statistik']}): ") or atlet["statistik"]
                atlet["prestasi"] = input(f"Prestasi ({atlet['prestasi']}): ") or atlet["prestasi"]
                print(f"\nAtlet {atlet['nama']} berhasil diupdate!\n")
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
                print(f"\nAtlet {atlet['nama']} berhasil dihapus!\n")
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
