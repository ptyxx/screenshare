from vidstream import ScreenShareClient
import threading

# clients ipv4
sender = ScreenShareClient('', 9999)
sender.stop_stream()


t = threading.Thread(target=sender.start_stream())
t.start()

while input("") != 'STOP':
    continue

sender.stop_stream()
