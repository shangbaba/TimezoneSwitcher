#!/usr/bin/python

import sys, subprocess

print "* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n"
print "*                                                             *\n"
print "*           WELCOME TO USE MY TIME CHANGING PROGRAM           *\n"
print "*                                                             *\n"
print "* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n"

def selecttimezone():
	print "Select a timezone from the following options: \n"
	print "1. Sydney\n"
	print "2. Brisbane\n"
	print "3. Adelaide\n"
	print "4. Perth\n"
	tz = raw_input("Please select a number: ")
	print "\n"
	options = [1, 2, 3, 4]
	if int(tz) in options:
		if int(tz) == 1:
			changetimezone('Sydney')
		if int(tz) == 2:
			changetimezone('Brisbane')
		if int(tz) == 3:
			changetimezone('Adelaide')
		if int(tz) == 4:
			changetimezone('Perth')
	else:
		print "Wrong input.\n"
		selecttimezone()


def changetimezone(city):
	try:
		subprocess.call("sudo systemsetup -settimezone Australia/'%s'" % city, shell=True)
	except:
		print 'Can\'t change the timezone.' + '\n'
	return 0

def entermin():
	cmin = input("Please enter the minute: ")
	print "\n"

	if cmin >= 0 and cmin < 10:
		return format(cmin, "02")
	elif cmin >= 10 and cmin < 60:
		return str(cmin)
	else:
		print "Wrong input! Please enter a number between 0 and 60\n"
		entermin()

def enterhour():
	chour = input("Please enter the hour: ")
	print "\n"
	if chour >= 0 and chour < 10:
		return format(chour, "02")
	elif chour >=10 and chour <24:
		return str(chour)
	else:
		print "Wrong input! Please enter a number between 0 and 24\n"
		enterhour()


def entertime():

	changetotime = enterhour() + ":" + entermin() + ":" + "00"
	settime(changetotime)
	return 0

def settime(time):
	try:
		subprocess.call("sudo systemsetup -setusingnetworktime off && sudo systemsetup -settime '%s'" % time, shell=True)
	except:
		print 'Can\'t change the time.' + '\n'	
	return 0

def turnonnetworktime():
	try:
		subprocess.call('sudo systemsetup -setusingnetworktime on', shell=True)
	except:
		print 'Can\'t turn on network time.' + '\n'


def main():
	print "1. Change your timezone\n"
	print "2. Change your time\n"
	print "3. Sync your time with internet\n"
	selecter = input("What would you like to do: ")
	if selecter == 1:
		selecttimezone()
	elif selecter == 2:
		entertime()
	elif selecter == 3:
		turnonnetworktime()
	else:
		print 'Please select an option in the list'
		main()

main()
