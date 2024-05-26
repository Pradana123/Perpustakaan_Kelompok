class Buku:
    def __init__(self, judul, pengarang, tahun_terbit, kode):
        self.judul = judul
        self.pengarang = pengarang
        self.tahun_terbit = tahun_terbit
        self.kode = kode
        self.dipinjam = False

class Anggota:
    def __init__(self, nama, id_anggota):
        self.nama = nama
        self.id_anggota = id_anggota

class Perpustakaan:
    def __init__(self):
        self.daftar_buku = []
        self.list_sementara = []
        self.list_hapus = []
        self.daftar_anggota = []

    def tambah_buku(self, judul, pengarang, tahun_terbit, kode):
        buku_baru = Buku(judul, pengarang, tahun_terbit, kode)
        self.daftar_buku.append(buku_baru)
        print(f"Buku '{judul}' berhasil ditambahkan.")

    def daftar_anggota(self):
        print("Daftar Anggota:")
        for anggota in self.daftar_anggota:
            print(f"Nama: {anggota.nama}, ID: {anggota.id_anggota}")

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

    def hapus_buku(self, judul):
        for buku in self.daftar_buku:
            if buku.judul == judul and not buku.dipinjam:
                self.daftar_buku.remove(buku)
                return f"Buku {judul} berhasil dihapus."
        return f"Buku {judul} tidak ditemukan atau sedang dipinjam."


# Contoh penggunaan
perpustakaan = Perpustakaan()

while True:
    print("\nPilihan Menu:")
    print("1. Tambah Buku")
    print("2. Tambah Anggota")
    print("3. Tambah Item")
    print("4. Pinjam Buku")
    print("5. Kembalikan Buku")
    print("6. Tampilkan Daftar Buku")
    print("7. Daftar Buku Dipinjam")
    print("8. Daftar Anggota")
    print("9. Keluar")

    pilihan = input("Masukkan pilihan Anda: ")

    if pilihan == "1":
        judul = input("Masukkan judul buku: ")
        pengarang = input("Masukkan nama pengarang: ")
        tahun_terbit = input("Masukkan tahun terbit: ")
        kode = input("Masukkan kode buku: ")
        perpustakaan.tambah_buku(judul, pengarang, tahun_terbit, kode)
    elif pilihan == "2":
        nama = input("Masukkan nama anggota: ")
        id_anggota = input("Masukkan ID anggota: ")
        perpustakaan.daftar_anggota.append(Anggota(nama, id_anggota))
        print(f"Anggota {nama} berhasil ditambahkan.")
    elif pilihan == "3":
        item = input("Masukkan item yang ingin ditambahkan: ")
        perpustakaan.tambah_item(item)
    elif pilihan == "4":
        item = input("Masukkan item yang ingin dihapus sementara: ")
        perpustakaan.hapus_item(item)
    elif pilihan == "5":
        item = input("Masukkan item yang ingin dikembalikan: ")
        perpustakaan.kembalikan_item(item)
    elif pilihan == "6":
        perpustakaan.tampilkan_daftar_sementara()
    elif pilihan == "7":
        perpustakaan.tampilkan_daftar_hapus()
    elif pilihan == "8":
        perpustakaan.daftar_anggota()
    elif pilihan == "9":
        print("Terima kasih!")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih lagi.")
