#1
import csv
from netmiko import ConnectHandler
# Create a list of devices to connect to
devices = [
{"device_type": "cisco_ios",
"ip": "sandbox-iosxe-recomm-1.cisco.com",
"username": "developer",
"password": "lastorangerestoreball8876",
},
{
"device_type": "cisco_ios",
"ip": "sandbox-iosxr-1.cisco.com",
"username": "admin",
"password": "C1sco12345",
}
# Add more devices as needed
]

# Open a CSV file to store the collected information
with open("network_device_inventory.csv","w",newline="") as csv_file:
    csv_writer = csv.writer(csv_file)
    # Write headers to the CSV file
    csv_writer.writerow(["Hostname", "IP Address", "Interfaces", "VLANs"])
    # Connect to each device and collect information
    for device in devices:
        with ConnectHandler(**device) as net_connect:
            hostname = net_connect.send_command("show run | i hostname").split()[-1]
            ip_address = device["ip"]
            interfaces = net_connect.send_command("show ip interface brief")
            vlans = net_connect.send_command("show vlan brief")
            # Write the collected information to the CSV file
            csv_writer.writerow([hostname, ip_address, interfaces, vlans])

#2
from netmiko import ConnectHandler
# Prompt the user for device information and backup file location
ip_address = input("Enter device IP address: ")
username = input("Enter device username: ")
password = input("Enter device password: ")
backup_file = input("Enter backup file location: ")
# Connect to the device using Netmiko and backup its configuration
device = {"device_type": "cisco_ios",
          "ip": ip_address,
          "username": username,
          "password": password,}
with ConnectHandler(**device) as net_connect:
    backup_config = net_connect.send_command("show run")
# Write the backup configuration to the specified file
with open(backup_file,"w") as backup_file:
    backup_file.write(backup_config)

#3
from netmiko import ConnectHandler
# Prompt the user for device information and VLAN configuration details
ip_address = input("Enter device IP address: ")
username = input("Enter device username: ")
password = input("Enter device password: ")
vlan_id = input("Enter VLAN ID: ")
vlan_name = input("Enter VLAN name: ")
interface_list = input("Enter interface list (comma-separated): ")
# Connect to the device using Netmiko and configure the VLAN
device = {"device_type": "cisco_ios",
          "ip": ip_address,
          "username": username,
           "password": password,
         }
with ConnectHandler(**device) as net_connect:
# Create the VLAN
    vlan_commands = [f"vlan {vlan_id}", f"name {vlan_name}"]
    net_connect.send_config_set(vlan_commands)
    # Assign interfaces to the VLAN
    interface_commands = [f"interface {interface}" for interface in interface_list.split(",")]
    interface_commands.append(f"switchport access vlan {vlan_id}")
    net_connect.send_config_set(interface_commands)

#4
import csv
from netmiko import ConnectHandler
# Create a list of devices to connect to
devices = [
{"device_type": "cisco_ios",
"ip": "172.16.24.135",
"username": "admin",
"password": "cisco",
},
{"device_type": "cisco_ios",
"ip": "172.16.24.154",
"username": "admin",
"password": "cisco",
}
# Add more devices as needed
]
# Open a CSV file to store the collected information
with open("network_health_check.csv", "w", newline="") as csv_file:
    csv_writer = csv.writer(csv_file)
    # Write headers to the CSV file
    csv_writer.writerow(["Device", "Connectivity", "Interface Status", "Network Performance", "Issues"])
    # Connect to each device and perform health check
    for device in devices:
        with ConnectHandler(**device) as net_connect:
        # Check device connectivity
            try:
                ping_output = net_connect.send_command("ping 8.8.8.8")
                connectivity = "Success" if "!" in ping_output else "Failed"
            except:
                connectivity = "Failed"
            # Check interface status
            interface_status = net_connect.send_command("show ip interface brief")
            # Test network performance
            network_performance = net_connect.send_command("ping 172.16.24.135 repeat 100")
            # Identify potential issues
            issues = ""
            if "down" in interface_status:
                issues += "Interface Down; "
            if "Success rate is 0 percent" in network_performance:
                issues += "Network Performance Issues; "
        # Write the collected information to the CSV file
        csv_writer.writerow([device["ip"], connectivity, interface_status, network_performance, issues])

#5
from netmiko import ConnectHandler
# Prompt the user for device information and troubleshooting rules
ip_address = input("Enter device IP address: ")
username = input("Enter device username: ")
password = input("Enter device password: ")
interface_down_action = input("Enter action for down interfaces (up, shut): ")
config_error_action = input("Enter action for configuration errors (fix, ignore): ")
# Connect to the device using Netmiko and perform troubleshooting
device = {"device_type": "cisco_ios",
          "ip": ip_address,
          "username": username,
          "password": password,
        }
with ConnectHandler(**device) as net_connect:
    # Check for down interfaces
    down_interfaces = net_connect.send_command("show ip interface brief | i down")
    if down_interfaces:
        if interface_down_action == "up":
            up_commands = [f"interface {interface}", "no shutdown"]
            for interface in down_interfaces.splitlines():
                net_connect.send_config_set(up_commands)
        elif interface_down_action == "shut":
            shut_commands = [f"interface {interface}", "shutdown"]
            for interface in down_interfaces.splitlines():
                net_connect.send_config_set(shut_commands)
        # Check for configuration errors
    config_errors = net_connect.send_command("show running-config | include ^!|\\s{2,}")
    if config_errors:
        if config_error_action == "fix":
            config_commands = [line.strip() for line in config_errors.splitlines() if not line.startswith("!")]
            net_connect.send_config_set(config_commands)
        elif config_error_action == "ignore":
            pass
