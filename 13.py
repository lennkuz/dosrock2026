from ipaddress import *
ip = '146.180.173.153'
mask = '255.192.0.0'
net = ip_network(f'{ip}/{mask}',0)
print(net[-2])
s = sum(int(x) for x in str(net[-2]).split('.'))
print(s)
s = eval(str(net[-2]).replace('.', '+'))
print(s)
print(146+191+255+254)