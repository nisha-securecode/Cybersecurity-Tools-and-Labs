import socket 
target_ip = "scanme.nmap.org"
target_port = 22

def grab_banner(ip,port):
    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.settimeout(2)

        s.connect((ip,port))
    
        banner = s.recv(1024)
        print(f"[+] banner: {banner.decode().strip()}")

        s.close()
    
    except socket.timeout:
        print("[-] connection timed out. port closed or filtered")
    except socket.ConnectionRefusedError:
        print("[-] connection refused. no service running on device")
    except Exception as e:
        print("[-] error occured:{e}")

grab_banner(target_ip, target_port)
