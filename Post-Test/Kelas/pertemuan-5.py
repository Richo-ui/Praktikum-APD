data_mahasiswa = ["Ifnu", "Adi", "Richo", "Andi"]

print("="*10)
print("Menu")
print("="*10)
print("""
1. Lihat data
2. Tambah data
3. Cari data
4. Hapus data
5. Exit""")

kesempatan = 1
while kesempatan == 1:
    menu = input("Masukan pilihan : ")
    if menu == "1":
        for index, item in enumerate(data_mahasiswa):
            print(item)
            
    if menu == "2":
        print("Mau ditambah diawal atau akhir? (1/2)")
        butuh = input("Masukan kebutuhan : ")
        if butuh == "1":
            item = input("Masukan nama : ")
            data_mahasiswa.insert(0, item)
            print(data_mahasiswa)
        if butuh == "2":
            item = input("Masukan nama : ")
            data_mahasiswa.append(item)
            print(data_mahasiswa)
    if menu == "3":
        print("Apa data yang ingin dicari : ")
        cari = input("Masukan nama : ")
        if cari in data_mahasiswa:
            print(f"Data {cari.lower} ditemukan")
        else:
            print(f"Data {cari.lower} tidak ditemukan")
    if menu == "4":
        print("Ingin menghapus data yang mana? ")
        hapus = input("Masukan nama : ")
        if hapus in data_mahasiswa:
            data_mahasiswa.remove(hapus)
            print(f"Data {hapus} telah dihapus")
            print(data_mahasiswa)
        else: 
            print(f"Data {hapus} tidak ditemukan")
    if menu == "5":
        kesempatan = 0
else:
    print("Terima kasih")