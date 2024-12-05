# student id 101004154
# student name Andrew Xue

from netmiko import ConnectHandler

routers = [
    {"host": "192.168.11.128", "username": "admin", "password": "admin123", "port": "30001"},
    {"host": "192.168.11.128", "username": "admin", "password": "admin123", "port": "30002"},
    {"host": "192.168.11.128", "username": "admin", "password": "admin123", "port": "30003"}
]

for i, router in enumerate(routers, start=1):
    with open(f'router_{i}.txt', 'w') as file:
        file.write(f"{router['host']}\n")
        file.write(f"{router['username']}\n")
        file.write(f"{router['password']}\n")
        file.write(f"{router['port']}\n")

ospf_config = [
    "router ospf 1",
    "net 0.0.0.0 0.0.0.0 area 0",
    "distance 200",
    "default-information originate"
]

with open('ospf_routing_protocol.txt', 'w') as file:
    for line in ospf_config:
        file.write(line + '\n')

for i in range(1, 4):
    with open(f'router_{i}.txt', 'r') as file:
        host = file.readline().strip()
        username = file.readline().strip()
        password = file.readline().strip()
        port = file.readline().strip()

    router = {
        'device_type': 'cisco_ios',
        'host': host,
        'username': username,
        'password': password,
        'port': port,
    }

    net_connect = ConnectHandler(**router)
    net_connect.enable()

    with open('ospf_routing_protocol.txt', 'r') as file:
        ospf_commands = file.readlines()

    net_connect.send_config_set(ospf_commands)
    net_connect.disconnect()
