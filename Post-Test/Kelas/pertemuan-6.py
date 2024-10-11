data_mhs = {
    "nama" : "ucup",
    "nim" : 1,
    "matkul" : "APD",
    "dosen" :  {
        "nama" : "Awang",
        "matkul" : "APD"
    }
}

print(data_mhs['nama'])
print(data_mhs['nim'])

print(data_mhs.get('mapel'))

for data in data_mhs:
    print(data)

for key_data, value_data in data_mhs.items():
    print(f"Key: {key_data}\nValue: {value_data}")

data_mhs['alamat'] = 'samarinda'
data_mhs['alamat'] = 'palaran'

print(data_mhs)

#del data_mhs('nim')
cache = data_mhs.pop('nim')

print(data_mhs, "dictionary")
print(cache, 'cache')

print(data_mhs)
biodata = {
    
}

key = "apel", "mangga", "semangka", "nangka"
value = 1, 4, 2, 6
buah = dict.fromkeys(key, value)
print(buah)

print(data_mhs["dosen"]["nama"])