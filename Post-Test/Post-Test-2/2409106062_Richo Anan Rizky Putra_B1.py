# Program Biodata dengan Fungsi Input
print("Bio Data Anda")

# Input data dari user
nama = input("Masukkan Nama: ")
umur = int(input("Masukkan Umur: "))
tinggi_badan = float(input("Masukkan Tinggi Badan (dalam meter): "))
status_mahasiswa = input("Apakah Anda seorang mahasiswa? (True/False): ")
status_mahasiswa = status_mahasiswa.lower() == 'true'

# Menjumlahkan total variabel tipe data int dan float
total = umur + tinggi_badan

# Menampilkan biodata
print("Nama                : ", nama)
print("Umur                : ", umur)
print("Tinggi Badan        : ", tinggi_badan, "meter")
print("Status Mahasiswa    : ", status_mahasiswa)

# Menampilkan total jumlah dari variabel tipe int dan float
print("Total dari variabel yang bertipe int dan float adalah:", total)
