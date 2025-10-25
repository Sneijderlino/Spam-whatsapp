# Spam-whatsapp

Spam-whatsapp adalah skrip Python sederhana untuk mengirim pesan berulang ke satu kontak WhatsApp Web menggunakan Selenium.

Disclaimer singkat: proyek ini menggunakan otomatisasi WhatsApp Web. Penggunaan untuk spam, pelecehan, atau aktivitas ilegal tidak didukung. Gunakan hanya untuk keperluan testing atau komunikasi yang sah sesuai aturan WhatsApp.

## Ringkasan
- Penulis: Sneijderlino
- Bahasa: Python 3.8+
- Dependencies: `selenium`, `webdriver-manager`

## Fitur utama
- Menggunakan Chrome dan profil user-data agar sesi tetap tersimpan (tidak perlu scan QR tiap kali).
- Mengirim pesan berulang ke nomor tujuan.

## Quick start (Windows / bash)

1. Clone repo:

```bash
git clone https://github.com/Sneijderlino/Spam-whatsapp.git
cd "Spam WA"
```

2. Buat virtualenv dan install dependency:

```bash
python -m venv .venv
source .venv/Scripts/activate  # jika menggunakan bash di Windows
pip install --upgrade pip
pip install -r requirements.txt
```

3. Konfigurasi (opsional): buka `SpamWA.py` dan sesuaikan variabel konfigurasi di bagian atas:
- `NOMOR` — format: 628... (tanpa + atau 0 di depan)
- `PESAN` — teks pesan
- `JUMLAH_PESAN` — banyak pesan yang ingin dikirim
- `JEDA_SELANJUT` — jeda antar pesan (detik)
- `CHROMEDRIVER_PATH` — jika Anda ingin menggunakan chromedriver lokal, set path-nya.

4. Jalankan skrip:

```bash
python SpamWA.py
```

Saat pertama kali dijalankan, browser akan membuka WhatsApp Web. Scan QR jika diminta. Profil session akan disimpan di folder `wa-session/` sehingga tidak perlu scan ulang pada run berikutnya.

## Cara kerja singkat
Skrip membuka `https://web.whatsapp.com/send?phone=...&text=...` lalu menunggu hingga box input chat terdeteksi, kemudian mengirim pesan sebanyak konfigurasi.

## Keamanan & Privasi
- Jangan commit folder `wa-session/` yang berisi session Chrome — sudah ditambahkan ke `.gitignore`.
- Repo tidak menyimpan nomor tujuan secara publik kecuali Anda memasukkannya ke file dan meng-commitnya.

## Contributing
Lihat `CONTRIBUTING.md` untuk panduan kontribusi. Tersedia template Issue dan Pull Request di `.github/`.

## License
Lihat file `LICENSE` di repo.

## Catatan pengembang
- Tambahkan `CHROMEDRIVER_PATH` jika anda tidak ingin mengandalkan `webdriver-manager`.
- Untuk CI, ada workflow dasar di `.github/workflows/ci.yml` yang menjalankan lint dan pengecekan sintaks.
<p align="center">
  <img src="/img/spamwa.png" alt="Header Image" width="900"/>
</p>

<h1 align="center">💣 Spam-whatsapp</h1>

<p align="center">

  <a href="LICENSE">
    <img src="https://img.shields.io/github/license/Sneijderlino/Spam-whatsapp?style=for-the-badge&color=2ecc71" alt="License"/>
  </a>
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/Python-3.8+-3776AB.svg?style=for-the-badge&logo=python" alt="Python"/>
  </a>
  <img src="https://img.shields.io/badge/OS-Windows%20%7C%20Linux%20%7C%20macOS-informational?style=for-the-badge" alt="OS Support"/>
  <img src="https://img.shields.io/badge/Status-Active%20Development-success?style=for-the-badge" alt="Status"/>
</p>

---

## 🛑 Disclaimer Penting (Wajib Dibaca!)

Proyek ini bertujuan *HANYA untuk tujuan edukasi, riset keamanan, dan pembelajaran otomasi.*  
⚠ *Segala bentuk penyalahgunaan adalah tanggung jawab penuh pengguna.*  
Penulis *tidak bertanggung jawab atas kerugian, pelanggaran hukum, atau pemblokiran akun WhatsApp* yang disebabkan oleh penggunaan skrip ini.

---

## 🧠 Tentang Proyek

*WA-Spammer-Selenium* adalah automation script berbasis *Python* dan *Selenium* untuk mengirim pesan otomatis melalui WhatsApp Web.  
Skrip ini dirancang untuk *menguji kemampuan otomasi browser* dan *simulasi sistem pengiriman pesan massal* menggunakan deep link WhatsApp.

---

## 🚀 Mengapa Proyek Ini Menarik?

💡 *WA-Spammer-Selenium* bukan hanya untuk spam. Ini contoh nyata bagaimana automation tools bekerja:  

- 🔁 *Selenium Session Handling* → belajar cara menyimpan & melanjutkan sesi login WhatsApp Web.  
- ⚙ *WebDriver Management* → tidak perlu repot mengunduh chromedriver secara manual.  
- 🔗 *Dynamic URL Invocation* → membuka chat lewat link wa.me/send langsung ke target.

---

## ✨ Fitur Utama

| Fitur | Deskripsi |
|:--|:--|
| ✅ *Sesi Persisten* | Login cukup sekali, QR disimpan di folder wa-session/ |
| ⚙ *Driver Otomatis* | webdriver-manager otomatis menyesuaikan versi Chrome |
| ⏱ *Jeda Terkontrol* | Atur jeda antar pesan agar mirip perilaku manusia |
| 🔒 *Konfigurasi Aman* | Semua pengaturan terpisah di SpamWA.py atau .env |
| 💬 *Pesan Kustom* | Dapat mengatur isi pesan dan jumlah pengiriman |

---

## 🧩 Persyaratan Sistem

| Komponen | Keterangan |
|:--|:--|
| *Python* | Versi *3.8 atau lebih baru* |
| *Google Chrome* | Harus sudah terinstal & up to date |
| *Paket Python* | selenium, webdriver-manager |

### 📦 Install Dependencies

```bash
pip install -r requirements.txt
``