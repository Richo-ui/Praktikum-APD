import os

# Fungsi untuk membersihkan layar
def clear_screen():
    os.system('cls')


# Fungsi untuk validasi input tipe data
def validasi_input(input_prompt, input_type):
    while True:
        try:
            return input_type(input(input_prompt))
        except ValueError:
            print(f"Input harus berupa {input_type.__name__}. Coba lagi.")