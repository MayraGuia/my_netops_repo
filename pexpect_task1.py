import pexpect

username = 'ignw'
password = 'ignw'
device_ip = '10.0.0.5'

connection = pexpect.spawn(f'ssh {username}@{device_ip}')
#print(connection)
#print(type(connection))


connection.expect('WHAT TO EXPECT')
connection.sendline(password)


connection.sendline('show run interface g1')
connection.expect('ignw-csr#')

connection.sendline('show run interface g1')
connection.expect('ignw-csr#')
