from netmiko import ConnectHandler


cisco1 = {
    "device_type": "cisco_ios",
    "ip": "192.168.43.207",
    "username": "router",
    "password": "cisco",
}


# Show command that we execute.

command = "show version"



with ConnectHandler(**cisco1) as net_connect:

    output = net_connect.send_command(command)
   
  

# Automatically cleans-up the output so that only the show output is returned
print()
print(output)
print()


