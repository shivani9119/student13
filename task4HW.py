#1 By using Class and providing commands directly
'''from netmiko import ConnectHandler
class CiscoDevice: #class is defined
    def __init__(self1, device_type, ip, username, password):#init Method is defined
        self1.device_info = {
            "device_type": device_type,
            "ip": ip,
            "username": username,
            "password": password
        }
        self1.connection = ConnectHandler(**self1.device_info)
    def send_command(self1, command): #send_command method is defined
        output = self1.connection.send_command(command)
        print(output)
device1 = CiscoDevice("cisco_ios", "sandbox-iosxe-recomm-1.cisco.com", "developer", "lastorangerestoreball8876")
#define object
device1.send_command("show ip int br") #.send_command() is a method to call the object
device1.send_command("show clock")
device1.send_command("show run | i hostname")
device1.send_command("show ver")'''

#2 By using Class and iterating commands from list
'''from netmiko import ConnectHandler
class CiscoDevice:
    def __init__(self, device_type, ip, username, password):
        self.device_info = {
            "device_type": device_type,
            "ip": ip,
            "username": username,
            "password": password
}
        self.connection = ConnectHandler(**self.device_info)
    def send_commands(self, commands):
        for command in commands:
            output = self.connection.send_command(command)
            print(output)
device1 = CiscoDevice("cisco_ios", "sandbox-iosxe-recomm-1.cisco.com", "developer", "lastorangerestoreball8876")
commands = ["show run | i hostname", "show ip int br", "show clock","show ver"]
device1.send_commands(commands)
print("job is success")'''

#3 Using 'if' condition
'''from netmiko import ConnectHandler
deviceinfo123 = {
    "device_type": "cisco_ios",
    "ip": "sandbox-iosxe-recomm-1.cisco.com",
    "username": "developer",
    "password": "lastorangerestoreball8876"
}
ssh123 = ConnectHandler(**deviceinfo123)
mycommands = input('enter the interface id:')
checkinter123 = ssh123.send_command("show ip int " + mycommands)
if "up" and "up" in checkinter123:
    print(mycommands + " is already up")
    #y = ssh123.send_config_set(["interface " + mycommands, "shutdown", "desc **reserved for CR12345*"])
    #print(y)
else:
    print(mycommands + " is down")'''

#4.
'''from netmiko import ConnectHandler, NetmikoAuthenticationException, NetmikoTimeoutException
multidevice = ["sandbox-iosxe-recomm-1.cisco.com", "172.16.24.205"]
for singledevice in multidevice:
    deviceinfo123 = {
        "device_type": "cisco_ios",
        "ip": singledevice,
        "username": "developer",
        "password": "lastorangerestoreball8876"
}
    try:
        ssh123 = ConnectHandler(**deviceinfo123)
        print("taking connection to " + singledevice + "#" * 10)
        out123 = ssh123.send_command("show ip int br")
        print(out123)
    except NetmikoAuthenticationException:
        print(singledevice + " failing due to cred issue")
        takingerrodev = open("authenticationfailed.txt", "a")
        takingerrodev.write(singledevice + "\n")
        takingerrodev.close()
        pass
    except NetmikoTimeoutException:
        print(singledevice + " failing due to TIMEOUT issue")
        takingerrodev = open("Timeoutfailed.txt", "a")
        takingerrodev.write(singledevice + "\n")
        takingerrodev.close()
        pass
print("job completed")'''

#5.
'''from netmiko import ConnectHandler, NetmikoAuthenticationException, NetmikoTimeoutException
pointingexternalfile = open(r"C:\Users\Student13\Documents\deviceip.txt", "r")
ab = pointingexternalfile.readlines()
print(ab)
pointingexternalfile1 = open(r"C:\Users\Student13\Documents\cred.txt", "r")
ab1 = pointingexternalfile1.readlines()
print(ab1)
user = ab1[0]
pass1 = ab1[1]
for singledevice in ab:
    start = 1
    while start < 5:
        try:
            deviceinfo123 = {
            "device_type": "cisco_ios",
            "ip": singledevice,
            "username": user,
            "password": pass1
            }
            ssh123 = ConnectHandler(**deviceinfo123)
            hostname123 = ssh123.find_prompt()
            print(hostname123)
            if ">" or "#" in hostname123:
                print("login to " + singledevice + " is successfully")
                print("taking connection to " + singledevice + "#" * 10)
                out123 = ssh123.send_command("show ip int br")
                print(out123)
                break
            else:
                pass
        except NetmikoAuthenticationException:
            print(singledevice + " failing due to cred issue")
            takingerrodev = open("authenticationfailed.txt", "a")
            takingerrodev.write(singledevice + "\n")
            takingerrodev.close()
            pass
        except NetmikoTimeoutException:
            print(singledevice + " failing due to TIMEOUT issue")
            takingerrodev = open("Timeoutfailed.txt", "a")
            takingerrodev.write(singledevice + "\n")
            takingerrodev.close()
            pass
        print(start)
        start = start + 1
print("job completed")
'''
#6.
'''from netmiko import ConnectHandler, file_transfer
from netmiko.ssh_autodetect import SSHDetect
iplist = ["sandbox-iosxe-recomm-1.cisco.com", "sandbox-iosxe-recomm-1.cisco.com"]
for ip in iplist:
    device123 = {
        "device_type": "autodetect",
        "ip": ip,
        "username": "developer",
        "password": "lastorangerestoreball8876"
    }
    guesseer123 = SSHDetect(**device123)
    device_type = guesseer123.autodetect()
    print(device_type)
    if device_type == "cisco_ios":
        device123 = {
            "device_type": device_type,
            "ip": ip,
            "username": "developer",
            "password": "lastorangerestoreball8876"
    }
        ssh123 = ConnectHandler(**device123)
        o123 = ssh123.send_command("show ip int br")
        print(o123)
    elif device_type == "juniper":
        device123 = {
            "device_type": device_type,
            "ip": ip,
            "username": "developer",
            "password": "lastorangerestoreball8876"
        }
        ssh123 = ConnectHandler(**device123)
        o123 = ssh123.send_command("set xxxxxx")
        print(o123)
    elif device_type == "cisco_asa":
        device123 = {
            "device_type": device_type,
            "ip": ip,
            "username": "developer",
            "password": "lastorangerestoreball8876"
            }
        ssh123 = ConnectHandler(**device123)
        o123 = ssh123.send_command("show int ip br")
        print(o123)
    elif device_type == "panos":
        device123 = {
            "device_type": device_type,
            "ip": ip,
            "username": "developer",
            "password": "lastorangerestoreball8876"
        }
        ssh123 = ConnectHandler(**device123)
        o123 = ssh123.send_command("show int ip br")
        print(o123)
    else:
        print("this is non-ssh based device, excluding" + ip)'''

#8.
'''write a python netmiko script for multiple device (more than 1)
and store the device list externally and execute (show ip int br, show run, show clock) and store the backup in external
notepad'''
from netmiko import ConnectHandler, NetmikoAuthenticationException, NetmikoTimeoutException
multidevice = ["sandbox-iosxe-recomm-1.cisco.com", "sandbox-iosxe-recomm-1.cisco.com"]
pointingexternalfile = open(r"C:\Users\Student13\Documents\deviceip.txt", "r")
ab = pointingexternalfile.readlines()
print(ab)
#
pointingexternalfile1 = open(r"C:\Users\Student13\Documents\cred.txt", "r")
ab1 = pointingexternalfile1.readlines()
print(ab1)
user = ab1[0]
pass1 = ab1[1]
for singledevice in multidevice:
    deviceinfo123 = {
        "device_type": "cisco_ios",
        "ip": singledevice,
        "username": "developer",
        "password": "lastorangerestoreball8876"
    }
    try:
        ssh123 = ConnectHandler(**deviceinfo123)
        print("taking connection to " + singledevice + "#" * 10)
        mycommands = ["show run | i hostname", "show ip int br", "show clock", "show ver"]
        for singleclicommands in mycommands:
            output123 = ssh123.send_command(singleclicommands)
            # print(output123)
            takingerrodev = open("commands_data.txt", "a")
            takingerrodev.write(output123 + "\n")
            takingerrodev.close()
    except NetmikoAuthenticationException:
        print(singledevice + " failing due to cred issue")
        takingerrodev = open("authenticationfailed.txt", "a")
        takingerrodev.write(singledevice + "\n")
        takingerrodev.close()
        pass
    except NetmikoTimeoutException:
        print(singledevice + " failing due to TIMEOUT issue")
        takingerrodev = open("Timeoutfailed.txt", "a")
        takingerrodev.write(singledevice + "\n")
        takingerrodev.close()
        pass
print("job completed")