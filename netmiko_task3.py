from netmiko import ConnectHandler
import time

cisco_cloud_router = {'device_type': 'cisco_ios',
'ip': '10.0.0.5',
'username': 'ignw',
'password': 'ignw'}
connection = ConnectHandler(**cisco_cloud_router)


config_commands = ['interface loopback 1',
                   'ip address 8.8.4.4 255.255.255.255',
                   'no shutdown']
connection.config_mode()
output = connection.send_config_set(config_commands)
print(output)
time.sleep(2)

output2=connection.send_command("show ip int brief lo1")
if output2.count('up') == 2:
    print('it looks like loopback1 is "up/up" Way to go!')
else:
    print("Something went wrong! let's get outa here before we break something!")
    sys.exit()

#Interface G2 Configuration
config_commands = ['interface GigabitEthernet2',
                   'ip address 203.0.113.1 255.255.255.192',
                   'no shutdown']
connection.config_mode()
output = connection.send_config_set(config_commands)
print(output)
time.sleep(2)

output2=connection.send_command("show ip int brief gi2")
if output2.count('up') == 2:
    print('it looks like gi2 is "up/up" Keep going!')
else:
    print("Something went wrong! let's get outa here before we break something!")
    sys.exit()

print('Moving on to static routing...')

comands = ['ip route 10.255.255.2 255.255.255.255 203.0.113.2']

connection.send_config_set(commands)
time.sleep(2)

show_output = connection.send_command('show ip route 10.255.255.2')
if 'Network not in table' in show_output:
    print('Something went wrong...')
    sys.exit()
else:
    print('It looks like the route made it into the table!')

connection.send_command('wr')
