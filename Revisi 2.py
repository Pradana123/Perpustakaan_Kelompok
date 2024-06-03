class Buku:
    def __init__(self, judul, pengarang, tahun_terbit, codebuku):
        self.judul = judul
        self.pengarang = pengarang
        self.tahun_terbit = tahun_terbit
        self.codebuku = codebuku
        self.dipinjam = False

    def __str__(self):
        return f"{self.judul} oleh {self.pengarang}, {self.tahun_terbit}, {self.codebuku}"

class Anggota:
    def __init__(self, nama, id_anggota):
        self.nama = nama
        self.id_anggota = id_anggota
        self.buku_dipinjam = []

    def pinjam_buku(self, buku):
        if not buku.dipinjam:
            buku.dipinjam = True
            self.buku_dipinjam.append(buku)
            return True
        return False

    def kembalikan_buku(self, buku):
        if buku in self.buku_dipinjam:
            buku.dipinjam = False
            self.buku_dipinjam.remove(buku)
            return True
        return False

    def daftar_buku_dipinjam(self):
        return self.buku_dipinjam

class Perpustakaan:
    def __init__(self):
        self.daftar_buku = []
        self.anggota_perpustakaan = []

    def tambah_buku(self, buku):
        self.daftar_buku.append(buku)

    def hapus_buku(self, judul):
        for buku in self.daftar_buku:
            if buku.judul == judul and not buku.dipinjam:
                self.daftar_buku.remove(buku)
                return f"Buku {judul} berhasil dihapus."
        return f"Buku {judul} tidak ditemukan atau sedang dipinjam."

    def cari_buku(self, judul):
        found_books = [buku for buku in self.daftar_buku if judul.lower() in buku.judul.lower()]
        return found_books

    def tampilkan_buku(self):
        buku_tersedia = [buku for buku in self.daftar_buku if not buku.dipinjam]
        if buku_tersedia:
            return "\n".join(str(buku) for buku in sorted(buku_tersedia, key=lambda x: x.judul))
        return "Tidak ada buku di perpustakaan."

    def jumlah_buku_tersedia(self):
        buku_tersedia = len([buku for buku in self.daftar_buku if not buku.dipinjam])
        return f"Jumlah buku yang tersedia: {buku_tersedia}"

    def tambah_anggota(self, anggota):
        self.anggota_perpustakaan.append(anggota)

    def cari_anggota(self, id_anggota):
        for anggota in self.anggota_perpustakaan:
            if anggota.id_anggota == id_anggota:
                return anggota
        return None

def main():
    perpustakaan = Perpustakaan()
    perpustakaan.tambah_buku(Buku("The Hobbit", "J.R.R. Tolkien", 1937, "BKPS01"))
    perpustakaan.tambah_buku(Buku("1984", "George Orwell", 1949, "BKPS02"))

    print("Selamat datang di Sistem Manajemen Perpustakaan!")
    while True:
        print("\nMenu:")
        print("1. Tambah Buku")
        print("2. Hapus Buku")
        print("3. Cari Buku")
        print("4. Tampilkan Semua Buku")
        print("5. Tambah Anggota")
        print("6. Pinjam Buku")
        print("7. Kembalikan Buku")
        print("8. Keluar")
        pilihan = input("Masukkan pilihan Anda: ")

        if pilihan == '1':
            judul = input("Masukkan judul buku: ")
            pengarang = input("Masukkan pengarang buku: ")
            tahun_terbit = input("Masukkan tahun terbit buku: ")
            codebuku = input("Masukkan code buku: ")
            perpustakaan.tambah_buku(Buku(judul, pengarang, tahun_terbit, codebuku))
            print("Buku berhasil ditambahkan.")
        elif pilihan == '2':
            judul = input("Masukkan judul buku yang ingin dihapus: ")
            print(perpustakaan.hapus_buku(judul))
        elif pilihan == '3':
            judul = input("Masukkan judul buku yang ingin dicari: ")
            found_books = perpustakaan.cari_buku(judul)
            if found_books:
                for buku in found_books:
                    print(buku)
            else:
                print("Buku tidak ditemukan.")
        elif pilihan == '4':
            print(perpustakaan.jumlah_buku_tersedia())
            print(perpustakaan.tampilkan_buku())
        elif pilihan == '5':
            nama = input("Masukkan nama anggota: ")
            id_anggota = input("Masukkan ID anggota: ")
            perpustakaan.tambah_anggota(Anggota(nama, id_anggota))
            print("Anggota berhasil ditambahkan.")
        elif pilihan == '6':
            id_anggota = input("Masukkan ID anggota: ")
            anggota = perpustakaan.cari_anggota(id_anggota)
            if anggota:
                jumlah_buku = int(input("Masukkan jumlah buku yang ingin dipinjam: "))
                for _ in range(jumlah_buku):
                    judul = input("Masukkan judul buku yang ingin dipinjam: ")
                    buku = next((b for b in perpustakaan.daftar_buku if b.judul == judul and not b.dipinjam), None)
                    if buku and anggota.pinjam_buku(buku):
                        print(f"Buku '{judul}' berhasil dipinjam.")
                    else:
                        print(f"Buku '{judul}' tidak tersedia atau sudah dipinjam.")
            else:
                print("Anggota tidak ditemukan. Silakan daftar sebagai anggota terlebih dahulu.")
                nama = input("Masukkan nama anggota: ")
                id_anggota = input("Masukkan ID anggota: ")
                anggota_baru = Anggota(nama, id_anggota)
                perpustakaan.tambah_anggota(anggota_baru)
                print("Anggota berhasil ditambahkan. Silakan coba pinjam buku kembali.")
        elif pilihan == '7':
            id_anggota = input("Masukkan ID anggota: ")
            anggota = perpustakaan.cari_anggota(id_anggota)
            if anggota:
                jumlah_buku = int(input("Masukkan jumlah buku yang ingin dikembalikan: "))
                for _ in range(jumlah_buku):
                    judul = input("Masukkan judul buku yang ingin dikembalikan: ")
                    buku = next((b for b in anggota.buku_dipinjam if b.judul == judul), None)
                    if buku and anggota.kembalikan_buku(buku):
                        print(f"Buku '{judul}' berhasil dikembalikan.")
                    else:
                        print(f"Buku '{judul}' tidak ditemukan di daftar peminjaman.")
            else:
                print("Anggota tidak ditemukan.")
        elif pilihan == '8':
            print("Terima kasih telah menggunakan sistem perpustakaan kami.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()

