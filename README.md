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