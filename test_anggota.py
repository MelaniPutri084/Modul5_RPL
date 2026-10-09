from models.anggota_model import AnggotaModel

model_anggota = AnggotaModel()

# Tambahkan dua baris print ini di awal
print("Menambahkan data anggota...")
print("Data anggota berhasil disimpan!\n")

# Tampilan daftar anggota perpustakaan
print("=== Daftar Anggota Perpustakaan ===")
daftar_anggota = model_anggota.get_all_anggota()
for anggota in daftar_anggota:
    print(f"[{anggota['id_anggota']}] {anggota['nama']} - {anggota['alamat']}")