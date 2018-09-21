from netmiko import ConnectHandler
import time
import sys


nxosv = {'device_type':'cisco_nxos',
         'ip': '10.0.0.6',
         'username': 'ignw',
         'password': 'ignw'}
connection = ConnectHandler(**nxosv)

commands = ['feature interface-vlan',
            'vlan 1000',
            'interface vlan1000',
            'description To ASAv',
            'ip address 10.255.255.2 255.255.255.240',
            'no shut',
            'interface Ethernet1/2',
            'switchport',
            'no shut',
            'switchport mode trunk',
            'switchport trunk native vlan 1000',
            'no shut']
connection.send_config_set(commands)
time.sleep(2)

show_output = connection.send_command('show ip int vlan1000 | in up')
print(show_output)

words = show_output.split()
print(words)

if words.count('up') == 3:
    print('It looks like Vlan1000 is "up/up"!')
else:
    print('Something went wrong...')
    sys.exit()
show_output = connection.send_command('show int status | i Eth1/2')
if show_output.count('connected') == 1:
    print('It looks like Eth1/2 is "up/up"!')
else:
    print('Something wnet wrong')
    sys.exit()
