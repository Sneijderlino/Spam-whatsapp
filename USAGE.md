# USAGE

Panduan singkat menjalankan `SpamWA.py` pada Windows (bash) dan hal-hal yang sering diperlukan.

1) Virtualenv (opsional namun direkomendasikan):

```bash
python -m venv .venv
source .venv/Scripts/activate
pip install -r requirements.txt
```

2) Chromedriver:
- Jika tidak ingin menginstall chromedriver manual, skrip sudah mencoba menginstall menggunakan `webdriver-manager`.
- Jika menggunakan chromedriver manual, set `CHROMEDRIVER_PATH` di `SpamWA.py` ke path `chromedriver.exe`.

3) Menjaga session:
- Folder `wa-session/` akan dibuat otomotis dan menyimpan profile Chrome agar QR tidak perlu discan berulang.

4) Run:

```bash
python SpamWA.py
```

5) Troubleshooting singkat:
- Jika chat tidak terbuka, pastikan nomor benar (format internasional tanpa +) dan akun WhatsApp aktif.
- Jika element input tidak ditemukan, tunggu sampai WhatsApp Web selesai load atau perbesar timeout di file.
