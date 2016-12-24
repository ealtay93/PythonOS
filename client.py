# client.py
import socket
import platform
import time

try:
    # TCP/IP soketi olusturuluyor
    print 'Istemci Soketi yaratiliyor'
    soket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # lokal makine ismini al ve baglantiyi kur
    server_adres = ('localhost', 9992)
    print "9998 portu uzerinden sunucuya baglaniliyor..."
    soket.connect(server_adres)
    print "Baglanti basarili...!"
except socket.error, msg:
    print "Sunucuya Baglanti basarisiz oldu... Hata Kodu: " + str(msg[0]) + " , Hata mesaji: " + msg[1]
    exit()


OsInfo = platform.platform()

try:
    print "isletim sistemi bilgilerim sunucuya gonderiliyor..."
    soket.sendall(OsInfo)
    print "Isletim sistemi bilgisi basari ile sunucuya gonderildi..."
    time.sleep(2)

    data = soket.recv(4096)
    print("Sunucudan geri alinan bilgi: %s" % data.decode('ascii'))

finally:
    print "soket kapatiliyor..."
    soket.close()
