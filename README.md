# CallSwitch Firewall Application Tester 

Test your internet connecton to a callswitch server using the following tools. The tools are built in python and bundled into an applicaion using PyInstaller. Currently the tools are CLI and GUI tools only for Linux and Windows. 

The applicaion will test TCP ports using sockets and ICMP ping packets to deturmine the quality of the connection as well as any TCP ports that are required for the CallSwitch applicaion by TelcoSwitch. The tool can also test for latancy and packet loss seen between your network and your MT/CC server. 

### Future plans
* Support for ICMP ping testing providing ICMP TTL and RTT stats ✔
* Apple Mac support 
* SIP ALG testing
* Reporting to a simple text file that is saved to the user's directory

### How to use
1. Download the release for your device. 
2. Using your CLI (bash or cmd) navigate to the exe or binary file.
  - If you are a linux user you will need to run the binary as root
3. Run the file from the command line or windows UI
4. Enter in any infomation, that is prompted for. 
5. Confirm if you need to make any changes to the firewall

#### Windows CLI
![Screenshot of a tool working in Windows CMD](https://github.com/Kerleyt00/callswitch-firewall-tester/blob/main/image%20(6).png)

#### Windows GUI
![Screenshot of the tool working in Windows as a GUI](https://github.com/Kerleyt00/callswitch-firewall-tester/blob/main/gui_screenshot.png)

### Other infomation 

Please visit: https://support.telcoswitch.com/hc/en-us/articles/207279309-Network-ports-used-by-CallSwitch-Firewall-Guide-
