# server.py
import socket
import time

# sunucu soketini yarat

soket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Sunucu soketi yaratildi.'

# lokal makine ismini al ve baglan
server_adres = ('localhost', 9992)
soket.bind(server_adres)
soket.listen(1)


while True:
    # baglanti kurulu oldugu surece
    print "Baglanti icin bekleniyor..."
    conn, addr = soket.accept()
    try:
        print "Baglanti adresi: ", addr
        print "Istemciden veri bekleniyor..."
        data = conn.recv(4096)
        print 'Istemciden alinan bilgi: "%s"' % data
        print "Verinin alindigi anki zaman bilgisi istemciye gonderiliyor..."
        currentTime = time.ctime(time.time()) + "\r\n"
        conn.sendall(currentTime.encode('ascii'))

    finally:
        conn.close()

