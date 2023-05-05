#2
from netmiko import ConnectHandler
#def class
class CiscoDevice:
    def __init__(selfabc, device_type, ip, username, password):
        selfabc.deviceinfo123 = {
            "device_type": device_type,
            "ip": ip,
            "username": username,
            "password": password}
        selfabc.ssh123 = ConnectHandler(**selfabc.deviceinfo123)
    def send_command(selfabc, mycommands):
        for singleclicommands in mycommands:
            output123 = selfabc.ssh123.send_command(singleclicommands)
            print(output123)

device1 = CiscoDevice("cisco_ios", "172.16.24.177", "admin", "cisco")
mycommands = ["show run | i hostname", "show ip int br", "show clock", "show ver"]
device1.send_command(mycommands)
#
print("job is success")

''''#3
from netmiko import ConnectHandler, NetmikoAuthenticationException, NetmikoTimeoutException
multidevice = ["172.16.24.200", "172.16.24.205"]
for singledevice in multidevice:
    deviceinfo123 = {
        "device_type": "cisco_ios",
        "ip": singledevice,
        "username": "admin",
        "password": "cisco1"
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