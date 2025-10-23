# 🤝 Panduan Kontribusi ke Spam-whatsapp

Terima kasih banyak atas minat Anda untuk berkontribusi pada proyek *Spam-whatsapp* oleh Sneijderlino! Kami menghargai setiap usaha, baik itu laporan bug, usulan fitur, atau perbaikan kode.

Sebelum memulai, pastikan Anda telah membaca dan menyetujui *[Kode Etik (CODE_OF_CONDUCT.md)](./.github/CODE_OF_CONDUCT.md)* kami.

## 🧐 Bagaimana Cara Berkontribusi?

Ada beberapa cara Anda dapat membantu proyek ini:

### 1. 🐞 Melaporkan Bug (Bug Reports)

Jika Anda menemukan kesalahan atau masalah dalam menjalankan skrip:

1.  Akses tab **[Issues](https://github.com/Sneijderlino/Spam-whatsapp/issues)** di repositori ini.
2.  Klik tombol *"New Issue"* dan pilih template *"Laporan Bug"*.
3.  Berikan judul yang jelas ([BUG] Deskripsi Singkat Masalah).
4.  Sertakan *langkah-langkah reproduksi* yang detail dan informasi tentang *lingkungan* Anda (OS, versi Python, versi Chrome).

### 2. 💡 Mengusulkan Fitur (Feature Requests)

Jika Anda memiliki ide untuk meningkatkan fungsionalitas skrip:

1.  Akses tab **[Issues](https://github.com/Sneijderlino/Spam-whatsapp/issues)**.
2.  Klik tombol *"New Issue"* dan pilih template *"Usulan Fitur"* (Jika template ini tersedia, atau gunakan template umum).
3.  Jelaskan fitur yang Anda usulkan dan mengapa fitur tersebut penting bagi proyek.

### 3. 💻 Mengirimkan Kode (Pull Requests)

Untuk berkontribusi dengan kode, ikuti alur kerja standar Git:

1.  *Fork* repositori Sneijderlino/Spam-whatsapp.
2.  *Clone* repositori hasil fork Anda ke komputer lokal.
3.  Buat *Branch Baru* untuk perubahan Anda. Gunakan nama branch yang deskriptif:
    bash
    git checkout -b fix/perbaikan-input-pesan
    # ATAU
    git checkout -b feat/tambah-mode-headless
    
4.  Lakukan perubahan kode dalam file **SpamWA.py**.
5.  Pastikan Anda telah menjalankan pip install -r requirements.txt untuk menguji perubahan Anda secara lokal.
6.  *Commit* perubahan Anda (lihat aturan Commit Message di bawah).
7.  *Push* branch baru Anda ke repositori fork Anda.
8.  Buka *Pull Request (PR)* ke branch main di repositori utama Sneijderlino/Spam-whatsapp.
9.  Isi template *"Pull Request"* dan jelaskan secara ringkas perubahan Anda.

## 💬 Aturan Commit Message

Kami mengikuti konvensi penamaan commit yang sederhana dan jelas.

* Gunakan prefiks untuk menunjukkan jenis perubahan:
    * fix: Untuk perbaikan bug.
    * feat: Untuk fitur baru.
    * docs: Untuk perubahan dokumentasi (README, CONTRIBUTING, dll.).
    * refactor: Untuk perubahan kode yang tidak mengubah fungsi eksternal.
    * chore: Untuk pembaruan build atau tool (misalnya requirements.txt).

* *Contoh Commit yang Baik:*
    
    fix: Mengatasi gagal kirim pesan karena loading lambat
    feat: Menambahkan opsi untuk mengaktifkan mode headless Chrome
    docs: Memperbarui cara instalasi di Termux pada README
    

## ✅ Standar Kode

* *Kesesuaian Python:* Pastikan kode Anda kompatibel dengan Python 3.
* *Komentar:* Gunakan komentar secukupnya, terutama untuk blok kode yang kompleks atau workaround khusus Selenium.
* *Struktur:* Pertahankan struktur folder src/ dan file konfigurasi (.gitignore, requirements.txt) agar tetap rapi.
* *Pengujian Lokal:* Pastikan perubahan Anda tidak memunculkan bug baru dan skrip masih dapat berjalan normal.

Kami akan meninjau PR Anda sesegera mungkin. Selamat berkontribusi!