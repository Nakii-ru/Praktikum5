# Praktikum 5 - Dictionary'2

NAMA : RIDHO FHADLY HAMZAH

NIM : 312410486

KELAS : TI.24.A5

# Hasil Eksekusi Program
![prak.pict](https://github.com/Nakii-ru/prak.pict/blob/main/Screenshot%202024-11-20%20172111.png?raw=true)
![prak.pict](https://github.com/Nakii-ru/prak.pict/blob/main/Screenshot%202024-11-20%20172311.png?raw=true)
![prak.pict](https://github.com/Nakii-ru/prak.pict/blob/main/Screenshot%202024-11-20%20172335.png?raw=true)

# Flowchart Program
![prak.pict](https://github.com/Nakii-ru/prak.pict/blob/main/Praktikum5(1).png?raw=true)
# Penjelasan Program
```python
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
```
Program diawali deangan inisialisasi dictionary `nilai_data` untuk menyimpan data mahasiswa seperti `Nama`, `NIM`, `Nilai Tugas`, `UTS`, `UAS`, dan `Nilai Akhir`.

## Fungsi `lihat_data`

Fungsi ini menampilkan semua data mahasiswa yang telah dimasukkan. Jika tidak ada data, maka program akan menampilkan pesan `"Belum ada data`.
```python
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
```
##  Fungsi `tambah_data()`

Baris ini menyimpan data mahasiswa baru yang dimasukkan oleh pengguna ketika memasukkan pilihan `"T"` , termasuk `NIM`, `Nama`, `Nilai Tugas`, `UTS`, dan `UAS`. Program kemudian menghitung `nilai akhir`(`Nilai Tugas*0.3` + `UAS*0.35` + `UAS*0.35`) dan menyimpan data mahasiswa ke dalam dictionary `nilai_data.`
```python
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
```
## Fungsi `ubah_data()`

Baris ini Menampilkan semua data mahasiswa ketika pengguna memilih input `"U"`, lalu Pengguna akan memilih mana `NIM` yang ingin diubah. Jika `NIM` ditemukan, data mahasiswa diperbarui dengan data baru yang dimasukkan oleh pengguna.
```python
def hapus_data():
    lihat_data()
    if not nilai_data:
        return
    nim = input("Masukkan NIM data yang ingin dihapus: ")
    if nim in nilai_data:
        del nilai_data[nim]
        print("Data berhasil dihapus!")
    lihat_data()
```
## Fungsi `hapus_data()`

Baris Menampilkan semua data mahasiswa ketika pengguna memasukkan pilihan `"H"`, lalu Pengguna memilih `NIM` yang ingin dihapus. Data yang sesuai dengan `NIM` akan dihapus dari `nilai_data`.
```python
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
```
## Fungsi `cari_data()`

Baris ini untuk memasukkan keyword pencarian (`NIM`). Program mencari data yang sesuai dan menampilkan hasil pencarian ketika pengguna memilih pilihan `"C"`. Jika tidak ditemukan, program akan menampilkan pesan bahwa data tidak ditemukan.

```python
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
```
Program akan menampilkan menu utama berulang kali dengan pilihan sebagai berikut:

Lihat Data `(L)`: Menampilkan semua data mahasiswa yang telah dimasukkan.

Tambah Data `(T)`: Menambahkan data mahasiswa baru, termasuk NIM, nama, nilai tugas, UTS, dan UAS, serta menghitung nilai akhir.

Ubah Data `(U)`: Mengubah data mahasiswa berdasarkan NIM yang dipilih.

Hapus Data `(H)`: Menghapus data mahasiswa berdasarkan NIM yang dipilih.

Cari Data `(C)`: Mencari data mahasiswa berdasarkan nama atau NIM.

Keluar `(K)`: Mengakhiri program.
