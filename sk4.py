brg = {
        "p": "Lip Glaze Wardah",
        "h": "90000",
        "s": "15"
}

while True:
    print("=" * 57)
    print("\n                   DATA STOCK                    ")
    print("=" * 57)
    print("1. Lihat Data Barang")
    print("2. Tambah Data")
    print("3. Ubah Data Barang")
    print("4. Hapus Data")
    print("5. Menu")

    pilih = input("Pilihan Menu :")
# melihat data
    if pilih == "1":
        print("\n                   Data Produk                  ")
        print("Produk: ", brg["p"])
        print("Harga :", brg["h"])
        print("stok :", brg["s"])
        if "k_n" in brg:
            print("Kategori: ", brg["k_n"])

#Tambah Data
    elif pilih == "2":
        tambah = input("Masukkan Kategori Produk : ")
        brg["k_n"] = tambah
        print("\nData Berhasil ditambahkan")
#Ubah harga
    elif pilih == "3":
        ubah_harga = input("Tambahkan harga baru : ")
        brg["h"] = ubah_harga
        print("\nHarga Berhasil ditambahkan")
#Hapus Data
    elif pilih == "4":
        if "k_n" in brg:
            brg.pop("k_n")
            print("\nData Berhasil Dihapus")
        else:
            print("\nData tidak ditemukan")
#menu
    elif pilih == "5":
        print("\nTerima kasih, selamat tinggal :)")
        break
    else:
        print("Pilihan tidak ada di menu, silahkan coba lagi.")