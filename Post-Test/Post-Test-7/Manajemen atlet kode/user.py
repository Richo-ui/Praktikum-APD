import os
from utility import clear_screen, validasi_input
from atlet import tambah_atlet, lihat_atlet, edit_atlet, hapus_atlet

users = [{
    "user" : "admin", 
    "pw" : "admin123", 
    "role" : "admin"
}]

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

# Fungsi untuk membatasi login
def coba_login(coba=1):
    role = login()
    if role:
        return role
    elif coba < 3:
        print(f"Percobaan login ke-{coba}. Coba lagi.")
        return coba_login(coba + 1)
    else:
        print("Batas percobaan login habis!")
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

# Fungsi utama untuk menampilkan menu utama
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
            pilihan = validasi_input("Pilih opsi: ", int)
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

# Fungsi untuk menampilkan menu awal (login/register)
def menu_awal():
    while True:
        clear_screen()
        print("=== Menu Awal ===")
        print("1. Login")
        print("2. Register")
        print("3. Keluar")
        
        pilihan = validasi_input("Pilih opsi: ", int)
        if pilihan == 1:
            role = coba_login()
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