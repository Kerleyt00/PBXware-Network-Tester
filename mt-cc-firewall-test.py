import PySimpleGUI as sg
import socket
#
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

# UI Design
sg.theme('BlueMono')

gui_title = sg.Text('Welcome to the TelcoSwitch CC / MT server firewall tester'),
gui_host = sg.Text('What server do you want to test?'), sg.InputText(key="gui_input"),
gui_output = sg.Output(size=(80, 30)),
gui_button = sg.Button('Ok'), sg.Button('Close')
			
layout = [
    [gui_title],
    [gui_host],
    [gui_output],
    [gui_button]
    ]

# Create the Window
window = sg.Window('TelcoSwitch Callswitch Firewall Tester', layout)

# Event Loop to process "events" and get the "values" of the inputs

while True:
    
    event, values = window.read()
    host = str(values["gui_input"])
    
    if event == sg.WIN_CLOSED or event == 'Close': # if user closes window or clicks the close button
        break
        exit()
        
# Port tester if the user continues
    
    ip_addr = socket.gethostbyname(host)
    
    print(f"The server you are testing is: {host}\n")
    print (f"This server is hosted on IP address: {ip_addr}\n")

    for port in range(len(ports)):

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host,int(ports[port])))
    
        print (f"Testing port {ports[port]} - on server {host}")

        if result == 0:
            print("Host: {}, Port: {} - Enabled and working\n".format(host, ports[port]))
        else:
            print("Host: {}, - Firewall Issue on port: {} \nYou will need to address this".format(host, ports[port]))
        sock.close()

    print ("\nPlease visit: https://support.telcoswitch.com/hc/en-us/articles/207279309-Network-ports-used-by-CallSwitch-Firewall-Guide- for more info\n")

window.close()
