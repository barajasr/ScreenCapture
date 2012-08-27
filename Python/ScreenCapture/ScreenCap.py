# ScreenCap.py
# 
# Author: Richard Barajas
# Date: 27-08-2012
#
# Script invokes import command to take screenshot of desktop periodically 
# for a requested amount of time.

import argparse
import errno
import os
from sys import exit
from time import sleep, time
import datetime

targetDir = "./"

parser = argparse.ArgumentParser()
parser.add_argument('-D', '--Directory', action='store', dest='directory', help='Directory/path to save images. Default is ./')
parser.add_argument('-d', '--Duration', action='store', dest='duration', required=True, type=int, help='Duration of runtime for script in seconds by default.')
#parser.add_argument('-dMin', action='store_true', dest='durMin', default=False, help='Use flag to set Duration to Minutes rather than seconds.')
parser.add_argument('-p', '--Period', action='store', dest='period', required=True, type=int, help='Interval between screenshots in seconds by default.')
#parser.add_argument('-pMin', action='store_true', dest='perMin', default=False, help='Use flag to set Period to Minutes rather than seconds.')


def dirExists(target):
	return os.path.isdir(targetDir)

def main():
	periodaicShots()

def periodaicShots(duration, period):
	"""
	dur: How long to take screenshots in seconds; 0 equal infinite duration time.
	per:   Time interval between screenshots in seconds.
	"""
	start = time()
	while (time() - start) < duration:
		snapShot()
		sleep(period)

def snapShot():
	"""
	Takes a screenshot of current desktop. Saves image with timestap as filename.
	"""

	timeStamp = targetDir + datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S")

	# import - saves  any visible window on an X server and outputs it as an 
	#	   image file. You can capture a single window, the entire screen, 
	#	   or any rectangular portion of the screen.
	command = "import -window root " + timeStamp + ".png"
	os.system(command)

if __name__ == "__main__":
	args = vars(parser.parse_args())
	print vars(parser.parse_args())
	if args['directory'] is not None:
		targetDir = args['directory']

	duration = args['duration']
	if duration < 0:
		print "Duration must be non-negative."
		exit()

	period = args['period']
	if period <= 0:
		print "Period must be greater than zero."
		exit()

	# Make sure proper directory name ending in slash
	if targetDir[-1] != '/':
		targetDir += '/' 
	targetDir += datetime.datetime.now().strftime("%Y-%m-%d") + "/"
	print "Images shall be stored under appropiate date folder in \'" + targetDir + "\'"

	if not dirExists(targetDir):
		try:
			os.makedirs(targetDir)
		except OSError as exception:
			if exception.errno != errno.EEXIST:
				raise

	periodaicShots(duration, period)
