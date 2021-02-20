
from vidstream import StreamingServer
import threading

# host here (IPv4)
IPv4 = ''
receiver = StreamingServer(IPv4, 9999)
t = threading.Thread(target=receiver.start_server())
t.start()

while input("") != 'STOP':
    continue

receiver.stop_server()
