#!/bin/python3

#variable to help assign status to ip
x = 0 
y = True

#fucntion to check availability
def status_check(a):
	#this would be checking if hosts are online, but for now is just randomly returning true or false
	global x
	global y
	if x < 3:
		y = True
	else:
		y = False
	x += 1
	return(y)
	
#function to request a vm and connect to IP, placeholder values for now
def connect(a):
	print("\n")
	print("Requesting VM...")
	print("Connecting to host at {}...".format(ip_list[ip]))
	#final project would include a way to actually connect to machines


#list of lap IP addresses
ip_list = ["1.1.1.1", "2.2.2.2", "3.3.3.3", "4.4.4.4"]

for ip in range(4):
	busy = status_check(ip)
	if busy == True:
		print("Host at {} is busy".format(ip_list[ip]))
	else:
		print("Host at {} is availabe".format(ip_list[ip]))
		connect (ip)
		break


