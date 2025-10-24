import re

def group_24(ip_list):
  subnets = {}

  for ip in ip_list:

    subnet = '.'.join(ip.split(".")[0:3])
    if subnet not in subnets:
      subnets[subnet] = []
    subnets[subnet].append(ip)


  for subnet, ips in subnets.items():
    print(f"{subnet}.0/24: {ips}")










ips = [
    "192.168.0.1",
    "192.168.0.25",
    "192.168.0.200",
    "192.168.1.5",
    "192.168.1.100",
    "10.0.0.2",
    "10.0.0.55",
    "10.0.1.3",
    "172.16.5.10",
    "172.16.5.99",
    "172.16.6.1",
    "172.16.6.45"
]

group_24(ips)