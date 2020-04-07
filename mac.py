#!usr/bin/python

import subprocess 
from termcolor import colored


def changeMacAddress(interface,mac):
	subprocess.call(["ifconfig",interface,"down"])
	subprocess.call(["ifconfig",interface,"hw","ether",mac])
	subprocess.call(["ifconfig",interface,"up"])


def main():
	interface = str(input("Enter interface to change Mac Address on :"))
	newMacAddress = input("Enter mace address to Change To:")
	beforeChange = subprocess.check_output(["ifconfig",interface])
	changeMacAddress(interface,newMacAddress)
	afterChange = subprocess.check_output(["ifconfig",interface])
	if beforeChange == afterChange:
		print(colored("failed to change mac address to : " + newMacAdress,'red'))
	else:
		print(colored("successfully Done",'green'))




main()
