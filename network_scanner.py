import socket 
import threading

network = "10.25.2."
live_host = []

def scan_ip(ip):
    try:
        s =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.settimeout(0.5)

        result = s.connect_ex((ip,135))

        if result == 0:
            live_host.append(ip)
            print("[+] live: {ip}")
        s.close()
    except:
        pass

thread = []
for ip in range(1,255):
    ip = network + str(ip)
    t = threading.Thread(target=scan_ip,args=(ip,))
    thread.append(t)
    t.start()

for t in thread:
    t.join()

print(f"\nscan complete! found {len(live_host)} live host: ")

for host in live_host:
    print(host)
