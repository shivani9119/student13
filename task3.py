#LIST
lst = [1, 2, 3, 4, 5]
lst.append(6)
print(lst)
lst.remove(3)
print(lst)
print(lst[1])
tup = (1,2,3,4,5)#TUPLE
print(tup[1])
st = {1,2,3,4,5}#SET
st.add(6)
print(st)
st.remove(3)
print(st)

#IOS Automation
#Send Commands
#1
from netmiko import ConnectHandler
deviceinfo123 = {
    "device_type": "cisco_ios",
    "ip": "172.16.24.150",
    "username": "admin",
    "password": "cisco"
}
ssh123 = ConnectHandler(**deviceinfo123)
output123 = ssh123.send_command("show ip int br")
print(output123)

#2
from netmiko import ConnectHandler
deviceinfo123 = {
    "device_type": "cisco_ios",
    "ip": "172.16.24.150",
    "username": "admin",
    "password": "cisco"
}
ssh123 = ConnectHandler(**deviceinfo123)
mycommands = ["show run | i hostname", "show ip int br", "show clock","show ver"]
for singleclicommands in mycommands:
    output123 = ssh123.send_command(singleclicommands)
    print(output123)
print("job is success")

#Send Configuration Command
#1
from netmiko import ConnectHandler
deviceinfo123 = {
    "device_type": "cisco_ios",
    "ip": "172.16.24.150",
    "username": "admin",
    "password": "cisco"
}
ssh123 = ConnectHandler(**deviceinfo123)
output123 = ssh123.send_config_set(["do show clock", "router ospf 100"])
print(output123)

