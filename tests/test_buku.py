from unittest.mock import MagicMock
from models.buku_model import BukuModel

# Test 1: Pengujian bawaan modul untuk create_buku (JANGAN DIHAPUS)
def test_create_buku_berhasil():
    # Menginisialisasi Model
    model = BukuModel()

    # Memanipulasi (Mock) koneksi database agar tidak mengotori data asli
    model.conn = MagicMock()
    mock_cursor = MagicMock()
    model.conn.cursor.return_value = mock_cursor

    # Melakukan eksekusi fungsi
    hasil = model.create_buku("Buku Testing", "Penulis QA", 2026)

    # Memverifikasi apakah fungsi mengembalikan nilai True
    assert hasil is True

    # Memverifikasi apakah cursor.execute benar-benar dipanggil
    mock_cursor.execute.assert_called_once()

    # Memverifikasi apakah perintah commit (simpan) dipanggil
    model.conn.commit.assert_called_once()


# Test 2: Tambahan untuk Tugas 3 (Menguji fungsi get_all_buku)
def test_get_all_buku():
    model = BukuModel()
    
    # Mock koneksi dan kursor database
    model.conn = MagicMock()
    mock_cursor = MagicMock()
    model.conn.cursor.return_value = mock_cursor
    
    # Simulasi data kembalian (fetchall) dari database
    dummy_data = [
        (1, "Pemrograman Python", "Budi", 2023),
        (2, "Belajar MVC", "Ani", 2024)
    ]
    mock_cursor.fetchall.return_value = dummy_data
    
    # Eksekusi fungsi
    hasil = model.get_all_buku()
    
    # Verifikasi apakah kueri SELECT dijalankan
    mock_cursor.execute.assert_called_once()
    
    # Verifikasi apakah hasil pengembalian sesuai dengan data dummy
    assert len(hasil) == 2
    assert hasil[0][1] == "Pemrograman Python"