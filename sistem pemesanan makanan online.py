from prettytable import PrettyTable

users = {
    "admin": {"password": "akuadmin", "role": "admin"},
    "pembeli": {"password": "akupembeli", "role": "pembeli"}
}

menu = [
    {"nama": "Ramen", "harga": 25000},
    {"nama": "Sushi", "harga": 20000},
    {"nama": "Takoyaki", "harga": 15000},
    {"nama": "Karaage", "harga": 15000}
]

pesanan = []

# Fungsi untuk menampilkan menu
def tampilkan_menu():
    tabel = PrettyTable()
    tabel.title = "Menu Makanan Online"
    tabel.field_names = ["Nama", "Harga"]
    for item in menu:
        tabel.add_row([item["nama"], f"Rp {item['harga']}"])
    print(tabel)
    
# Fungsi untuk menambahkan menu (Admin)
def tambah_menu():
    nama = input("Masukkan nama makanan: ")
    if any(item["nama"].lower() == nama.lower() for item in menu):
        print ("Maaf, Menu dengan nama tersebut sudah ada.")
        return
    harga = int(input("Masukkan harga makanan: "))
    menu.append({"nama": nama, "harga": harga})
    print("Menu berhasil ditambahkan!")
    
# Fungsi untuk mengubah menu (Admin)
def ubah_menu():
    tampilkan_menu()
    nama_ubah = input("Masukkan nama menu yang ingin diubah: ")
    for item in menu:
        if item["nama"].lower() == nama_ubah.lower():
            item["nama"] = input("Masukkan nama baru: ")
            item["harga"] = int(input("Masukkan harga baru: "))
            print ("Menu berhasil diubah!")
            return
    print("Menu tidak ditemukan!")
    
# Fungsi untuk menghapus makanan
def hapus_menu():
    tampilkan_menu()
    nama_hapus = input("Masukkan nama menu yang ingin dihapus: ")
    for item in menu: 
        if item["nama"].lower() == nama_hapus.lower():
            menu.remove(item)
            print("Menu berhasil dihapus!")
            return
    print("Menu tidak ditemukan!")
    
# Fungsi untuk melalukan pemesanan (Pembeli)
def pesan_makanan():
    pesanan_saat_ini = []
    while True:
        tampilkan_menu()
        pilihan = input("Masukkan nama menu yang ingin dipesan (atau 'selesai' untuk mengakhiri pesanan): ")
        if pilihan.lower() == 'selesai':
            break
        jumlah = int(input("Masukkan jumlah yang ingin dipesan: "))
        for item in menu:
            if item["nama"].lower() == pilihan.lower():
                pesanan_saat_ini.append({"nama": item["nama"], "harga": item["harga"], "jumlah": jumlah})
                print(f"{jumlah} {item['nama']} ditambahkan ke pesanan")
                break
        else:
            print("Menu tidak ditemukan!")
        
    if pesanan_saat_ini:
        pesanan.extend(pesanan_saat_ini)
        print("Pesanan berhasil dicatat!")
    else:
        print("Tidak ada pesanan yang dicatat.")
            
# Fungsi untuk menampilkan pesanan
def tampilkan_pesanan():
    if not pesanan:
        print("Belum ada pesanan.")
        return
    
    tabel = PrettyTable()
    tabel.title = "Pesanan"
    tabel.field_names = ["Nama", "Harga", "Jumlah", "Total"]
    total_keseluruhan = 0
    for item in pesanan:
        total = item["harga"] * item["jumlah"]
        total_keseluruhan += total
        tabel.add_row([item["nama"], f"Rp {item['harga']}", item["jumlah"], f"Rp {total}"])
    print(tabel)
    print(f"Total Keseluruhan: Rp {total_keseluruhan}")
    
# Fungsi Login
def login():
    print("==========================LOGIN==========================")
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    user = users.get(username)
    if user and user["password"] == password: 
        return user["role"]
    return None

# Main program
def main():
    while True:
        print("=== Selamat Datang di Sistem Pemesanan Makanan Online ===")
        role = login()
        if role == "admin":
            while True:
                print("Menu Admin:")
                print("1. Tampilkan Menu")
                print("2. Tambah Menu")
                print("3. Ubah Menu")
                print("4. Hapus Menu")
                print("5. Logout")
                pilihan = input("Pilih menu (1-6): ")
                
                if pilihan == "1":
                    tampilkan_menu()
                elif pilihan == "2":
                    tambah_menu()
                elif pilihan == "3":
                    ubah_menu()
                elif pilihan == "4":
                    hapus_menu()
                elif pilihan == "5":
                    print("Logout berhasil.")
                    break
                else:
                    print("Pilihan tidak valid!")
                    
        elif role == "pembeli":
            while True:
                print("Menu Pembeli: ")
                print("1. Lihat Menu")
                print("2. Pesan Makanan")
                print("3. Lihat Pesanan")
                print("4. Logout")
                pilihan = input("Pilih menu (1-4): ")
                
                if pilihan == "1":
                    tampilkan_menu()
                elif pilihan == "2":
                    pesan_makanan()
                elif pilihan == "3":
                    tampilkan_pesanan()
                elif pilihan == "4":
                    print("Logout berhasil.")
                    break
                else:
                    print("Pilihan tidak valid")
                
        else:
            print("Login gagal. Username atau password salah.")
            
        lanjut = input("Apakah Anda ingin melanjutkan program? (ya/tidak): ")
        if lanjut.lower() != 'ya':
            print("Terima kasih telah menggunakan sistem pemesanan makanan online!")
            break

if __name__ == "__main__":
    main()