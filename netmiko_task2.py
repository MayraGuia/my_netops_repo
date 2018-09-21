from netmiko import ConnectHandler

cisco_cloud_router = {'device_type': 'cisco_ios',
'ip': '10.0.0.5',
'username': 'ignw',
'password': 'ignw'}
connection = ConnectHandler(**cisco_cloud_router)

#config_commands = ['interface loopback 0', 'description I made this with Python!', 'ip address 172.16.1.1 255.255.255.255']
#output = connection.send_config_set(config_commands)
#print(output)

config_commands = ['interface loopback 0', 'shutdown']
output = connection.send_config_set(config_commands)

output2=connection.send_command("show ip int brief lo0")
print(output2)

my_string= output2

if 'down' in my_string:
   print('It looks like loopback is not up!')
else:
   print('It looks like loopback0 is "up/up"! Way to go!')
