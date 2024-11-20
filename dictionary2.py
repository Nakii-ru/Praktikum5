nilai_data = {}

def lihat_data():
    if not nilai_data:
        print("=" * 64)
        print("No | Nama\t|    NIM    | Tugas | UTS | UAS |  Nilai Akhir |")
        print("=" * 64)
        print("   |                      Belum ada data                       |")
        print("=" * 64)
        return
    print("No | Nama\t|    NIM    | Tugas | UTS | UAS |  Nilai Akhir |")
    print("=" * 64)
    for i, (nim, data) in enumerate(nilai_data.items(), start=1):
        print(f"{i}  | {data['nama']}\t| {nim} | {data['tugas']}  | {data['uts']}| {data['uas']}| {data['nilai_akhir']:.2f}        |")
    print("=" * 64)

def tambah_data():
    print("\nMasukkan Data Mahasiswa")
    nim = input("NIM: ")
    nama = input("Nama: ")
    tugas = float(input("Nilai Tugas: "))
    uts = float(input("Nilai UTS: "))
    uas = float(input("Nilai UAS: "))
    nilai_akhir = (tugas * 0.3) + (uts * 0.35) + (uas * 0.35)
    nilai_data[nim] = {
        "nama": nama,
        "tugas": tugas,
        "uts": uts,
        "uas": uas,
        "nilai_akhir": nilai_akhir
    }
    print("Data berhasil ditambahkan!")

def ubah_data():
    lihat_data()
    if not nilai_data:
        return
    nim = input("Masukkan NIM data yang ingin diubah: ")
    if nim in nilai_data:
        print("Masukkan data baru:")
        nama = input("Nama: ")  
        tugas = float(input("Nilai Tugas: "))
        uts = float(input("Nilai UTS: "))
        uas = float(input("Nilai UAS: "))
        nilai_akhir = (tugas * 0.3) + (uts * 0.35) + (uas * 0.35)
        nilai_data[nim] = {
            "nama": nama,
            "tugas": tugas,
            "uts": uts,
            "uas": uas,
            "nilai_akhir": nilai_akhir
        }
        print("Data berhasil diubah!")
        lihat_data()
    else:
        print("Data dengan NIM tersebut tidak ditemukan.")

def hapus_data():
    lihat_data()
    if not nilai_data:
        return
    nim = input("Masukkan NIM data yang ingin dihapus: ")
    if nim in nilai_data:
        del nilai_data[nim]
        print("Data berhasil dihapus!")
    lihat_data()

def cari_data():
    if not nilai_data:
        print("Belum ada data.")
        return
    keyword = input("Masukkan nama atau NIM yang dicari: ").lower()
    hasil = {nim: data for nim, data in nilai_data.items() if keyword in nim.lower() or keyword in data['nama'].lower()}
    if hasil:
        print("Hasil pencarian:")
        print("No | Nama\t|    NIM    | Tugas | UTS | UAS |  Nilai Akhir |")
        print("=" * 64)
        for i, (nim, data) in enumerate(hasil.items(), start=1):
            print(f"{i}  | {data['nama']}\t| {nim} | {data['tugas']}  | {data['uts']}| {data['uas']}| {data['nilai_akhir']:.2f}        |")
        print("=" * 64)
    else:
        print("Data tidak ditemukan.")

while True:
    print("\n|Program Input Nilai|")
    print("[(L)Lihat, (T)Tambah, (U)Ubah, (H)Hapus, (C)Cari, (K)Keluar]")
    pilihan = input("Menu: ").lower()
    
    if pilihan == 'l':
        lihat_data()
    elif pilihan == 't':
        tambah_data()
    elif pilihan == 'u':
        ubah_data()
    elif pilihan == 'h':
        hapus_data()
    elif pilihan == 'c':
        cari_data()
    elif pilihan == 'k':
        print("Keluar Dari Program.")
        break
    else:
        print("Pilihan tidak valid, silakan coba lagi.")