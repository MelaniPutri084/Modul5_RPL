from models.buku_model import BukuModel

model = BukuModel()

# 1. Fungsi Create: Menambah data jika belum ada di database
daftar_buku = model.get_all_buku()
if not any(buku['judul'] == "Pemrograman Python MVC" for buku in daftar_buku):
    model.create_buku("Pemrograman Python MVC", "Guido van Rossum", 2023)

# 2. Fungsi Update: Mengubah data buku ID 1
model.update_buku(1, "Laskar Pelangi (Edisi Revisi)", "Andrea Hirata", 2008)

# 3. Fungsi Delete: Menghapus data buku ID 2 (Bumi Manusia)
model.delete_buku(2)

# 4. Fungsi Read: Menampilkan daftar buku terbaru
print("=== Daftar Buku Setelah Update & Delete ===")
daftar_buku_terbaru = model.get_all_buku()
for buku in daftar_buku_terbaru:
    print(f"[{buku['id_buku']}] {buku['judul']} - {buku['penulis']} ({buku['tahun_terbit']})")