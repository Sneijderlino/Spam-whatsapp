from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import urllib.parse
import time
import sys
import os

#================== CONFIGURATION ==================
CHROMEDRIVER_PATH = None 

NOMOR = "6282292964110"
PESAN = "Halo Bro, Saya Sneijderlino"
JUMLAH_PESAN = 10
JEDA_SELANJUT = 1.2

WA_USER_DATA = os.path.join(os.getcwd(), "wa-session")

# Timeouts

TIMEOUT_LOGIN = 90
TIMEOUT_CHAT_LOAD = 25

#================ END CONFIGURATION =================

def create_driver(path_to_driver=None):
    options = Options()
    options.add_argument(f"--user-data-dir={WA_USER_DATA}")
    options.add_argument("--profile-directory=Default")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-gpu")
    options.add_argument("--start-maximized")

    if path_to_driver and os.path.isfile(path_to_driver):
        service = Service(path_to_driver)
        driver = webdriver.Chrome(service=service, options=options)
    else:
        try:
            print("menginstal Chromedriver.")
            from webdriver_manager.chrome import ChromeDriverManager
            service = Service(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=options)
        except Exception as e:
            raise RuntimeError("Chromedriver tidak ditemukan dan webdriver-manager gagal. "
                            "Set CHROMEDRIVER_PATH ke chromedriver.exe atau install webdriver-manager.") from e
    return driver

def wait_for_login(driver, timeout=TIMEOUT_LOGIN):
    print("Menunggu WhatsApp Web terbuka dan login (scan QR jika perlu)...")
    try:
        WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true" and @data-tab]'))
        )
        time.sleep(1)
        print("Login terdeteksi. WhatsApp Web siap.")
        return True
    except Exception as e:
        print("Timeout menunggu login / WhatsApp Web belum siap. Pastikan sudah scan QR.")
        return False

def find_message_input(driver):
    xpaths = [
        '//footer//div[@contenteditable="true" and @data-tab]', 
        '//footer//div[@contenteditable="true" and @aria-label="Ketik pesan"]',
        '//footer//div[@aria-label="Type a message"]',
        '//div[@contenteditable="true" and @role="textbox"]',
    ]
    for xp in xpaths:
        try:
            el = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, xp)))
            if el.is_displayed():
                return el
        except:
            continue
    raise RuntimeError("Input pesan target (di chat) tidak ditemukan. WhatsApp Web mungkin belum memuat chat target sepenuhnya.")


def open_chat(driver, nomor, pesan_prefix=""):
    encoded = urllib.parse.quote(pesan_prefix)
    url = f"https://web.whatsapp.com/send?phone={nomor}&text={encoded}"
    driver.get(url)

    try: 
        find_message_input(driver) 
        time.sleep(2) 
        print(f"Chat dengan {nomor} berhasil dibuka dan kotak pesan siap.")
        return True
    except Exception as e:
        print("Gagal membuka chat atau chat belum siap (nomor mungkin tidak valid atau loading lambat):", e)
        return False 

def send_messages_in_one_chat(driver, pesan, jumlah, jeda):
    try:
        input_box = find_message_input(driver)
    except Exception as e:
        print("Gagal menemukan kotak pesan:", e)
        return 0, jumlah

    sukses = 0 
    gagal = 0 
    try:
        input_box.click()
        input_box.send_keys(Keys.CONTROL, "a") 
        input_box.send_keys(Keys.DELETE)      
        print("Kotak pesan target dibersihkan dari sisa teks (jika ada).")
    except:
        pass
    
    for i in range(1, jumlah + 1):
        try:
            driver.execute_script("arguments[0].focus();", input_box)
            input_box.click()
            
            message_to_send = f"{pesan} ({i})" 
            
            input_box.send_keys(message_to_send)
            time.sleep(0.08) 
            input_box.send_keys(Keys.ENTER)
            
            sukses += 1
            print(f"✅ [{i}/{jumlah}] Terkirim ke target.")
            time.sleep(jeda)
        except Exception as e:
            gagal += 1
            print(f"⚠️ [{i}/{jumlah}] Gagal kirim: {e}")
            try:
                input_box = find_message_input(driver)
            except: 
                pass
            time.sleep(1) 
            
    return sukses, gagal 

def main():
    print("=== Spam WA by Sneijderlino")
    if not NOMOR or not NOMOR.isdigit():
        print("Format nomor salah. Gunakan format: 628xx... tanpa + atau 0 di depan.")
        return

    os.makedirs(WA_USER_DATA, exist_ok=True)
    try:
        driver = create_driver(CHROMEDRIVER_PATH)
    except Exception as e:
        print("Gagal membuat driver:", e)
        return

    try:
        driver.get("https://web.whatsapp.com")
    except Exception as e:
        print("Gagal membuka WhatsApp Web di Chrome:", e)
        driver.quit()
        return
    if not wait_for_login(driver):
        print("Pastikan kamu sudah scan QR dan WhatsApp Web aktif.")
        driver.quit()
        return
    print(f"Membuka chat nomor {NOMOR} ...")
    if not open_chat(driver, NOMOR, ""):
        print("Gagal membuka chat target. Hentikan.")
        driver.quit()
        return
    print(f"\nMemulai pengiriman {JUMLAH_PESAN} pesan...")
    sukses, gagal = send_messages_in_one_chat(driver, PESAN, JUMLAH_PESAN, JEDA_SELANJUT)

    print("\n=== Ringkasan ===")
    print(f"Total sukses: {sukses}")
    print(f"Total gagal : {gagal}")
    print("Browser akan tetap terbuka (session disimpan). Tutup manual bila sudah selesai.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nDihentikan oleh user.")
        sys.exit(0)