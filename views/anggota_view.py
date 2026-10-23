import customtkinter as ctk
from tkinter import ttk, messagebox

class AnggotaView(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Sistem Manajemen Perpustakaan - Data Anggota")
        self.geometry("800x500")

        # Variabel counter untuk ID Otomatis
        self.id_counter = 1

        # Konfigurasi Grid Utama
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.grid_rowconfigure(0, weight=1)

        # FRAME KIRI: FORMULIR INPUT ANGGOTA
        self.frame_kiri = ctk.CTkFrame(self)
        self.frame_kiri.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        ctk.CTkLabel(self.frame_kiri, text="Form Data Anggota 084", font=("Arial", 16, "bold")).pack(pady=15)

        # Komponen Input
        self.entry_nama = ctk.CTkEntry(self.frame_kiri, placeholder_text="Masukkan Nama Anggota")
        self.entry_nama.pack(pady=10, padx=15, fill="x")

        self.entry_alamat = ctk.CTkEntry(self.frame_kiri, placeholder_text="Masukkan Alamat")
        self.entry_alamat.pack(pady=10, padx=15, fill="x")

        # Tombol Aksi (Dihubungkan ke method simpan_data)
        self.btn_simpan = ctk.CTkButton(self.frame_kiri, text="Simpan Data", fg_color="green", command=self.simpan_data)
        self.btn_simpan.pack(pady=10, padx=15, fill="x")

        self.btn_update = ctk.CTkButton(self.frame_kiri, text="Perbarui Data (Update)", fg_color="blue")
        self.btn_update.pack(pady=5, padx=15, fill="x")

        self.btn_delete = ctk.CTkButton(self.frame_kiri, text="Hapus Data (Delete)", fg_color="red")
        self.btn_delete.pack(pady=5, padx=15, fill="x")

        # FRAME KANAN: TABEL DAFTAR ANGGOTA
        self.frame_kanan = ctk.CTkFrame(self)
        self.frame_kanan.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        ctk.CTkLabel(self.frame_kanan, text="Daftar Anggota Perpustakaan 084", font=("Arial", 16, "bold")).pack(pady=15)

        # Komponen Tabel
        kolom = ("id", "nama", "alamat")
        self.tabel = ttk.Treeview(self.frame_kanan, columns=kolom, show="headings", height=15)

        self.tabel.heading("id", text="ID")
        self.tabel.heading("nama", text="Nama Anggota")
        self.tabel.heading("alamat", text="Alamat")

        self.tabel.column("id", width=40, anchor="center")
        self.tabel.column("nama", width=150)
        self.tabel.column("alamat", width=200)

        self.tabel.pack(fill="both", expand=True, padx=15, pady=10)

    def simpan_data(self):
        # Ambil nilai dari input entry
        nama = self.entry_nama.get().strip()
        alamat = self.entry_alamat.get().strip()

        # Validasi jika inputan kosong
        if not nama or not alamat:
            messagebox.showwarning("Peringatan", "Nama dan Alamat tidak boleh kosong!")
            return

        # Masukkan data ke dalam tabel visual Treeview
        self.tabel.insert("", "end", values=(self.id_counter, nama, alamat))
        self.id_counter += 1

        # Bersihkan kolom isian setelah disimpan
        self.entry_nama.delete(0, "end")
        self.entry_alamat.delete(0, "end")

if __name__ == "__main__":
    app = AnggotaView()
    app.mainloop()