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
        enscp = ssh123.send_config_set("ip scp server enable")
        trnsfer123 = file_transfer(ssh123, source_file="netmiko_global.log", dest_file="ciscoiosimage15.6.log", direction="put", file_system="disk0:")
        print(trnsfer123)
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

from netmiko import ConnectHandler, NetmikoAuthenticationException, NetmikoTimeoutException


deviceinfo123 = {
    "device_type": "cisco_ios",
    "ip": "sandbox-iosxe-recomm-1.cisco.com",
    "username": "developer",
    "password": "lastorangerestoreball8876"
}
ssh123 = ConnectHandler(**deviceinfo123)
# output123 = ssh123.send_command("show ip int br")
output123 = ssh123.send_command("sh ip ospf neighbor")
print(output123)
