from __future__ import print_function
import time
import sys

try:
    import winsound
except ImportError:
    import os

name = input("What is your name? ")

try:
	winsound.Beep(264, 250)
	sys.stdout.write('Ha')	
	time.sleep(500/2000.0)
	sys.stdout.write('ppy ')
	winsound.Beep(264, 250)
	time.sleep(250/2000.0)
	sys.stdout.write('birth')
	winsound.Beep(297, 1000)
	time.sleep(250/2000.0)
	sys.stdout.write('day ')
	winsound.Beep(264, 1000)
	time.sleep(250/2000.0)
	sys.stdout.write('to ')
	winsound.Beep(352, 1000)
	time.sleep(250/2000.0)
	print('you')
	winsound.Beep(330, 2000)
	time.sleep(500/2000.0)

	sys.stdout.write('Ha')
	winsound.Beep(264, 250)
	time.sleep(500/2000.0)
	sys.stdout.write('ppy ')
	winsound.Beep(264, 250)
	time.sleep(250/2000.0)
	sys.stdout.write('birth')
	winsound.Beep(297, 1000)
	time.sleep(250/2000.0)
	sys.stdout.write('day ')
	winsound.Beep(264, 1000)
	time.sleep(250/2000.0)
	sys.stdout.write('to ')
	winsound.Beep(396, 1000)
	time.sleep(250/2000.0)
	print('you')
	winsound.Beep(352, 2000)
	time.sleep(500/2000.0)

	sys.stdout.write('Ha')
	winsound.Beep(264, 250)
	time.sleep(250/2000.0)
	sys.stdout.write('ppy ')
	winsound.Beep(264, 500)
	time.sleep(250/1000.0)
	sys.stdout.write('birth')
	winsound.Beep(440, 1000)
	time.sleep(250/2000.0)
	sys.stdout.write('day ')
	winsound.Beep(350, 1000)
	time.sleep(250/2000.0)
	sys.stdout.write('dear ')
	winsound.Beep(330, 1000)
	print(name)
	time.sleep(250/2000.0)
	winsound.Beep(297, 1000)


	time.sleep(500/2000.0)
	sys.stdout.write('Ha')
	winsound.Beep(466, 250)
	time.sleep(500/2000.0)
	sys.stdout.write('ppy ')
	winsound.Beep(466, 250)
	time.sleep(250/2000.0)
	sys.stdout.write('birth')
	winsound.Beep(440, 1000)
	time.sleep(250/2000.0)
	sys.stdout.write('day ')
	winsound.Beep(352, 1000)
	time.sleep(250/2000.0)
	sys.stdout.write('to ')
	winsound.Beep(396, 1000)
	time.sleep(250/2000.0)
	print('you')
	winsound.Beep(352, 2000)
	time.sleep(250/2000.0)
except:
	os.system('beep -f 264 -l 250')
	sys.stdout.write('Ha')
	sys.stdout.flush()
	time.sleep(500/2000.0)
	sys.stdout.write('ppy ')
	sys.stdout.flush()	
	os.system('beep -f 264 -l 250')
	time.sleep(250/2000.0)
	sys.stdout.write('birth')
	sys.stdout.flush()
	os.system('beep -f 297 -l 1000')
	time.sleep(250/2000.0)
	sys.stdout.write('day ')
	sys.stdout.flush()
	os.system('beep -f 264 -l 1000')
	time.sleep(250/2000.0)
	sys.stdout.write('to ')
	sys.stdout.flush()
	os.system('beep -f 352 -l 1000')
	time.sleep(250/2000.0)
	print ('you')
	os.system('beep -f 330 -l 2000')
	time.sleep(500/2000.0)
	
	sys.stdout.write('Ha')
	sys.stdout.flush()
	os.system('beep -f 264 -l 250')
	time.sleep(500/2000.0)
	sys.stdout.write('ppy ')
	sys.stdout.flush()
	os.system('beep -f 264 -l 250')
	time.sleep(250/2000.0)
	sys.stdout.write('birth')
	sys.stdout.flush()
	os.system('beep -f 297 -l 1000')
	time.sleep(250/2000.0)
	sys.stdout.write('day ')
	sys.stdout.flush()
	os.system('beep -f 264 -l 1000')
	time.sleep(250/2000.0)
	sys.stdout.write('to ')
	sys.stdout.flush()
	os.system('beep -f 396 -l 1000')
	time.sleep(250/2000.0)
	print ('you')
	os.system('beep -f 352 -l 2000')
	time.sleep(500/2000.0)
	
	sys.stdout.write('Ha')
	sys.stdout.flush()
	os.system('beep -f 264 -l 250')
	time.sleep(250/2000.0)
	sys.stdout.write('ppy ')
	sys.stdout.flush()
	os.system('beep -f 264 -l 500')
	time.sleep(250/1000.0)
	sys.stdout.write('birth')
	sys.stdout.flush()
	os.system('beep -f 440 -l 1000')
	time.sleep(250/2000.0)
	sys.stdout.write('day ')
	sys.stdout.flush()
	os.system('beep -f 352 -l 1000')
	time.sleep(250/2000.0)
	sys.stdout.write('dear ')
	sys.stdout.flush()
	os.system('beep -f 330 -l 1000')
	print (name)
	time.sleep(250/2000.0)
	os.system('beep -f 297 -l 1000')
	
	os.system('beep -f 440 -l 1000')
	time.sleep(250/2000.0)
	
	time.sleep(500/2000.0)
	sys.stdout.write('Ha')
	sys.stdout.flush()
	os.system('beep -f 466 -l 250')
	time.sleep(500/2000.0)
	sys.stdout.write('ppy ')
	sys.stdout.flush()
	os.system('beep -f 466 -l 250')
	time.sleep(250/2000.0)
	sys.stdout.write('birth')
	sys.stdout.flush()
	os.system('beep -f 440 -l 1000')
	time.sleep(250/2000.0)
	sys.stdout.write('day ')
	sys.stdout.flush()
	os.system('beep -f 352 -l 1000')
	time.sleep(250/2000.0)
	sys.stdout.write('to ')
	sys.stdout.flush()
	os.system('beep -f 396 -l 1000')
	time.sleep(250/2000.0)
	print ('you')
	os.system('beep -f 352 -l 2000')
	time.sleep(250/2000.0)

print ('HAPPY BIRTHDAY ' + name )

sys.stdout.write('yay!!')
winsound.Beep(440, 1500)
time.sleep(250/2000.0)
