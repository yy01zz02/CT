import secrets
from netaddr import IPNetwork

protocols = ['6', '17']
common_ports = ['20','21','22','23','25','80','109','110','119','143','156','161','389','443']
action_list = ['Deny', 'Accept', 'Drop', 'Reject']
src_network = IPNetwork('192.168.1.0/24')
dest_network = IPNetwork('172.35.0.0/16')

fo = open("replay_log.txt", "w")
while True:
    proto_index = secrets.randbelow(2)
    protocol = protocols[proto_index]
    src_port_index = secrets.randbelow(14)
    dest_port_index = secrets.randbelow(14)
    src_port = common_ports[src_port_index]
    dest_port = common_ports[dest_port_index]
    action_index = secrets.randbelow(4)
    action = action_list[action_index]
    src_ip_index = 1 + secrets.randbelow(254)
    src_ip = src_network[src_ip_index]
    dest_ip_index = 1 + secrets.randbelow(65535)
    dest_ip = dest_network[dest_ip_index]