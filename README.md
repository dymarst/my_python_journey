# My Python Journey

Proyek ini adalah aplikasi CLI sederhana untuk belajar Python dan manajemen pengguna dengan MySQL/MariaDB.

## Fitur

- Register akun baru
- Login pengguna
- Menu pengguna untuk:
  - melihat profil
  - menambahkan nomor HP
  - menambahkan hobi
  - mengganti password
  - menghapus akun
  - mengirim pertanyaan ke admin
- Menu admin untuk:
  - melihat semua pengguna
  - menghapus user berdasarkan ID
  - mengakses menu user sebagai admin
  - melihat dan menjawab pertanyaan pengguna

## Struktur proyek

- `run.py` — entry point aplikasi
- `database/db.py` — koneksi MySQL ke database `test`
- `author/login.py` — proses login dan pemilihan menu admin/user
- `author/register.py` — pendaftaran akun baru
- `user/menu.py` — navigasi menu user
- `user/profile.py` — fungsi profil user (lihat, update telepon/hobi, ganti password, hapus akun)
- `user/user_questions.py` — kirim pertanyaan ke admin
- `adm/menu.py` — navigasi menu admin
- `adm/show_data.py` — tampilkan semua user
- `adm/del_user.py` — hapus user berdasarkan ID
- `adm/admin_questions.py` — tampilkan dan jawab pertanyaan pengguna
- `test.sql` — dump database contoh untuk tabel `users`

## Persyaratan

- Python 3.x
- MySQL atau MariaDB
- Paket Python: `mysql-connector-python`

## Setup

1. Install dependensi:
   ```bash
   pip install mysql-connector-python
   ```
2. Jalankan MySQL/MariaDB dan buat database `test`.
3. Eksekusi `test.sql` untuk membuat tabel `users` dan data awal:
   - tabel `users` dengan kolom: `id`, `username`, `password`, `telepon`, `hobi`
   - pengguna admin default: `dymarr`
4. Jika belum ada, buat juga tabel `ask` untuk menyimpan pertanyaan pengguna:
   ```sql
   CREATE TABLE ask (
     id INT AUTO_INCREMENT PRIMARY KEY,
     username VARCHAR(54) NOT NULL,
     pertanyaan TEXT NOT NULL,
     jawaban TEXT
   );
   ```
5. Sesuaikan koneksi database di `database/db.py` jika username, password, host, atau nama database berbeda.

## Menjalankan aplikasi

```bash
python run.py
```

## Catatan

- Admin dikenali saat login dengan username `dymarr`.
- Data pengguna tersimpan di MySQL/MariaDB.
- Aplikasi ini bertujuan sebagai latihan Python dengan operasi database sederhana.