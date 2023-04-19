import ipaddress

print("Veryfing IP Adress is well formatted")
print("    ",ipaddress.ip_address(u'192.168.0.255'))
try:
    print("    ",ipaddress.ip_address(u'192.168.0.255'))
except:
    print("    ","IP address not well formed")

print("    ",ipaddress.ip_address(u'FFFF:9999:2:FDE:257:0:2FAE:1120'))

print("Checking the typr of IP adress")
print("    ",type(ipaddress.ip_address(u'192.168.0.255')))
print("    ",type(ipaddress.ip_address(u'2001:db8::')))
print("    ",ipaddress.ip_address(u'192.168.0.255').reverse_pointer)
print("    ",ipaddress.ip_network(u'192.168.0.0/28'))

print("Comparing IP address")
print("    ",ipaddress.IPv4Address(u'192.168.0.2') > ipaddress.IPv4Address(u'192.168.0.1'))
print("    ",ipaddress.IPv4Address(u'192.168.0.2') == ipaddress.IPv4Address(u'192.168.0.1'))
print("    ",ipaddress.IPv4Address(u'192.168.0.2') != ipaddress.IPv4Address(u'192.168.0.1'))

print("IP addresses Arithmetic")
print("    "+str(ipaddress.IPv4Address(u'192.168.0.2')+1))

print(("    ",ipaddress.IPv4Address(u'192.168.0.253')-3))

print("    ",ipaddress.IPv4Address(u'192.168.0.253')+3)

try:
    print(("    ",ipaddress.IPv4Address(u'255.255.255.255')+1))
except:
    print("    ", "IP address not well formed")