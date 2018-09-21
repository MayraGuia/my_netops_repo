from netmiko import ConnectHandler
import time
import sys

asav = {'device_type':'cisco_ios',
        'ip': '10.0.0.8',
        'username': 'ignw',
        'password': 'ignw',
        'port' : 22,
        'secret': 'ignw',
        'verbose': False,}
connection = ConnectHandler(**asav)

print('Starting on GigabitEthernet0/0...')


if  connection.check_enable_mode() == False:
    connection.enable()
    #connection.config_mode()
    commands = ['interface GigabitEthernet0/0',
                'description Connected to CSR',
                'nameif outside',
                'security-level 0',
                'ip address 203.0.113.2 255.255.255.192',
                'no shutdown']


    connection.send_config_set(commands)

    print('Starting on GigabitEthernet0/1...')

    commands = ['interface GigabitEthernet0/1',
                'description Connected to NX-OSv',
                'nameif inside',
                'security-level 100',
                'ip address 10.255.255.1 255.255.255.240',
                'no shutdown']
    connection.send_config_set(commands)
    time.sleep(2)

    show_output = connection.send_command('show int ip brief | in GigabitEthernet0/1')
    print(show_output)
    if show_output.count('up') == 2:
        print('It looks like GigabithEtnernet0/1 is "up/up"!')
    else:
        print('Something went wrong..')
        sys.exit()

    print('Moving to static routing...')

    commands = ['route outside 8.8.4.4 255.255.255.255 203.0.113.1']

    connection.send_config_set(commands)
    time.sleep(2)

    show_output = connection.send_command('show route 8.8.4.4')
    if 'Network not in table' in show_output:
        print('Something went wrong...')
        sys.exit()
    else:
        print('It looks like the route made it into the table!')

    print('Moving on to access-list configuration...')

    commands = ['access-list outside in extended permit icmp any any',
                'access-group outside_in in interface outside']

    connection.send_config_set(commands)
    connection.send_command('wr')
