import socket
from pythonping import ping
#
host = input("What server do you want to test? " )
ip_addr = socket.gethostbyname(host)

# ports used for testing callswitch
port_80=80
port_443=443
port_5060=5060
port_5061=5061
port_10001=10001
port_10005=10005
port_10007=10007
port_10009=10009
port_11389=11389
# turn ports into a list
ports = [
    port_80,
    port_443,
    port_5060,
    port_5061,
    port_10001,
    port_10005,
    port_10007,
    port_10009,
    port_11389
    ]

# Port tester if the user continues
    
ip_addr = socket.gethostbyname(host)

print(f"The server you are testing is: {host}\n")
print (f"This server is hosted on IP address: {ip_addr}\n")
#packet loss and latacny test
print ("\nWe are testing packet loss\n")

action = ping (host, count = 10, timeout =2)
if action.packet_loss == 0.0:
    print ("Your network is good\n")
else:
    print ("You have a packet loss issue\n")

print ("\nWe are testing for network latancy\n")
print ("Average Latancy (ms): ")
print (action.rtt_avg_ms)
print ("Max Latancy (ms): ")
print (action.rtt_max_ms)

if action.rtt_max_ms <= 150.0:
    print ("Your network is good\n")
else:
    print ("You have a latacny issue\n")

for port in range(len(ports)):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((host,int(ports[port])))
    
    print (f"Testing port {ports[port]} - on server {host}")

    if result == 0:
        print("Host: {}, Port: {} - Enabled and working".format(host, ports[port]))
    else:
        print("Host: {}, - Firewall Issue on port: {} \nYou will need to address this".format(host, ports[port]))
        break
    sock.close()

print ("\n\nPlease visit: https://support.telcoswitch.com/hc/en-us/articles/207279309-Network-ports-used-by-CallSwitch-Firewall-Guide- for more info\n")