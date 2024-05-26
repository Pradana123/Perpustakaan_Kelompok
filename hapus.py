class Perpustakaan:
    def __init__(self):
        self.list_sementara = []
        self.list_hapus = []

    def tambah_item(self, item):
        self.list_sementara.append(item)

    def hapus_item(self, item):
        if item in self.list_sementara:
            self.list_sementara.remove(item)
            self.list_hapus.append(item)
            print("Item '{}' telah dihapus sementara.".format(item))
        else:
            print("Item '{}' tidak ditemukan dalam daftar sementara.".format(item))

    def kembalikan_item(self, item):
        if item in self.list_hapus:
            self.list_hapus.remove(item)
            self.list_sementara.append(item)
            print("Item '{}' telah dikembalikan ke daftar sementara.".format(item))
        else:
            print("Item '{}' tidak ditemukan dalam daftar yang telah dihapus.".format(item))

    def tampilkan_daftar_sementara(self):
        print("Daftar sementara:", self.list_sementara)

    def tampilkan_daftar_hapus(self):
        print("Daftar yang telah dihapus:", self.list_hapus)


# Contoh penggunaan
perpustakaan = Perpustakaan()

while True:
    print("\nPilihan Menu:")
    print("1. Tambah Item")
    print("2. Hapus Item Sementara")
    print("3. Kembalikan Item yang Telah Dihapus")
    print("4. Tampilkan Daftar Sementara")
    print("5. Tampilkan Daftar yang Telah Dihapus")
    print("6. Keluar")

    pilihan = input("Masukkan pilihan Anda: ")

    if pilihan == "1":
        item = input("Masukkan item yang ingin ditambahkan: ")
        perpustakaan.tambah_item(item)
    elif pilihan == "2":
        item = input("Masukkan item yang ingin dihapus sementara: ")
        perpustakaan.hapus_item(item)
    elif pilihan == "3":
        item = input("Masukkan item yang ingin dikembalikan: ")
        perpustakaan.kembalikan_item(item)
    elif pilihan == "4":
        perpustakaan.tampilkan_daftar_sementara()
    elif pilihan == "5":
        perpustakaan.tampilkan_daftar_hapus()
    elif pilihan == "6":
        print("Terima kasih!")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih lagi.")
