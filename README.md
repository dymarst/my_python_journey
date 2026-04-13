# My Python Journey

Proyek ini adalah aplikasi CLI sederhana untuk belajar Python dan manajemen pengguna dengan MySQL/MariaDB.

## Fitur

### Fitur Umum
- Register akun baru dengan password di-hash menggunakan bcrypt
- Login dengan verifikasi password dan pencatatan last_login
- Max 3 attempt login sebelum ditolak

### Menu Pengguna
- Melihat profil (username, telepon, hobi)
- Menambahkan nomor HP
- Menambahkan hobi
- Mengganti password dengan verifikasi password lama
- Menghapus akun dengan konfirmasi
- Mengirim pertanyaan ke admin (disimpan di database)

### Menu Admin
- Melihat semua pengguna dengan informasi lengkap (ID, username, telepon, hobi, last login)
- Menghapus user berdasarkan ID
- Mengakses menu user sebagai admin (lihat profil, tambah HP/hobi, ganti password)
- Melihat semua pertanyaan dari pengguna
- Menjawab pertanyaan pengguna

## Struktur proyek

### File Utama
- `run.py` — entry point aplikasi, menampilkan menu login/register dan routing ke menu yang sesuai

### Database Module (`database/`)
- `db.py` — koneksi MySQL ke database `test` (host: 127.0.0.1, user: root, password: kosong)
- `test.sql` — dump database dengan tabel `users` dan `ask` beserta data awal

### Authentication Module (`author/`)
- `login.py` — proses login dengan bcrypt verification, max 3 attempt, update last_login, routing ke menu admin/user
- `register.py` — pendaftaran akun baru dengan bcrypt hashing password, cek duplikasi username

### User Module (`user/`)
- `menu.py` — navigasi menu user dengan 6 opsi (lihat profil, tambah HP, tambah hobi, ganti password, hapus akun, kirim pertanyaan)
- `profile.py` — fungsi profil user:
  - `lihat_data()` — tampilkan profil (username, telepon, hobi)
  - `isi_telepon()` — tambah/update nomor HP
  - `isi_hobi()` — tambah/update hobi
  - `ganti_password()` — ubah password dengan verifikasi password lama menggunakan bcrypt
  - `del_akun()` — hapus akun dengan konfirmasi
- `user_questions.py` — kirim pertanyaan ke admin dan simpan ke tabel `ask`

### Admin Module (`adm/`)
- `menu.py` — navigasi menu admin dengan 5 opsi (tampilkan semua user, hapus user, login sebagai user, lihat pertanyaan, jawab pertanyaan)
- `show_data.py` — tampilkan semua user dari database dengan info ID, username, telepon, hobi, last_login
- `del_user.py` — hapus user berdasarkan ID dengan validasi
- `admin_questions.py` — tampilkan semua pertanyaan user dan fitur untuk admin menjawab pertanyaan

## Persyaratan

- Python 3.x
- MySQL atau MariaDB
- Paket Python: `mysql-connector-python`

## Database Schema

### Tabel `users`
- `id` (INT, Primary Key, Auto Increment)
- `username` (VARCHAR 54, Unique)
- `password` (VARCHAR 255) — disimpan dalam format hash bcrypt
- `telepon` (VARCHAR 12)
- `hobi` (VARCHAR 54)
- `last_login` (DATETIME)

### Tabel `ask`
- `id` (INT, Primary Key, Auto Increment)
- `username` (VARCHAR 12) — username penanya
- `pertanyaan` (TEXT) — isi pertanyaan
- `jawaban` (TEXT) — jawaban dari admin (boleh kosong jika belum dijawab)

## Setup

1. Install dependensi:
   ```bash
   pip install mysql-connector-python
   ```
2. Jalankan MySQL/MariaDB dan buat database `test`.
3. Eksekusi `test.sql` untuk membuat tabel `users`, `ask` dan data awal:
   - tabel `users` dengan kolom: `id`, `username`, `password`, `telepon`, `hobi`, `last_login`
   - tabel `ask` dengan kolom: `id`, `username`, `pertanyaan`, `jawaban`
   - pengguna admin default: `dymarr`
4. Sesuaikan koneksi database di `database/db.py` jika username, password, host, atau nama database berbeda.

## Menjalankan aplikasi

```bash
python run.py
```

## Catatan

- Data pengguna tersimpan di MySQL/MariaDB dengan tabel `users` dan `ask`.
- Password dienkripsi menggunakan bcrypt dengan salt generation untuk keamanan.
- Setiap login yang berhasil mencatat waktu terakhir login (`last_login`).
- Aplikasi ini bertujuan sebagai latihan Python dengan operasi database sederhana.

## Data Awal (Default)

Setelah menjalankan `test.sql`, tersedia:
- **Admin user:** username `dymarr` (dapat mengelola semua user)
- **Test user:** username `loke` (user biasa untuk testing)

## Keamanan

- Password disimpan dalam format hash bcrypt, bukan plaintext
- Setiap password baru di-hash dengan `bcrypt.gensalt()` sebelum disimpan
- Verifikasi password menggunakan `bcrypt.checkpw()` saat login dan ganti password