#
import socket
#from pythonping import ping
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

print (f"\n\nThis server is hosted on IP address: {ip_addr}\n\n")

# ping_result = ping(host, verbose=True)

# print(f"Latancy in ms: {ping_result.rtt_avg_ms}")

# print ("\nTesting round trip time\n")
# if ping_result.rtt_avg_ms >= 100: 
#     print ("You have a non latant internet connction")
# else: 
#     print ("You may see connection issues")

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