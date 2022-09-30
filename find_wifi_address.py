import socket
import netifaces

# flash ip 192.168.1.1
# code ip 192.168.100.1

my_system_name = socket.gethostname()
my_system_address = socket.gethostbyname(my_system_name)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.connect(('8.8.8.8', 1))

gateway_ip = netifaces.gateways()
my_wifi_address = s.getsockname()[0]

router_ip = gateway_ip['default'][netifaces.AF_INET][0]

print(f"Router ip address is : {router_ip}")
print(f"host name is : {my_system_name} and address is : {my_system_address} and wifi address is : {my_wifi_address}")