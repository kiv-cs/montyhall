# -*- coding: utf-8 -*-
#������ ���������� �������� ����� �����
#��� ��� �������� http://ru.wikipedia.org/wiki/��������_�����_�����
#	1. ���� ��� �����. �� ���� � ��������� ������� �����������: ����, ���� � ������������
#	2. ����� �������� ����� �����
#	3. ������� ��������� ���� �� ���������� ������. 
#���� �������� ���� � ����������, �� ��������� ����� � �����. ���� ��� ����, �� �������� ��������� �����.
#	4. �) � �������� ������������� ����� ������ ����� (������������ 2/3 ����� �� ����� ������ �������������)
#	   �) � �������� ������������� ����� �� ������ �����

# ��� ��������� ��������� �������� ������������ API ������� https://www.random.org/clients/http/
# ����� ������� ���������� ��� ������ http://pypi.python.org/pypi/randomdotorg/
#���� ���������� http://code.google.com/p/randomdotorg/
#import randomdotorg
import random
import sys

def args():
	args = sys.argv[1:]
	dotorg = False
	change = False
	number = 1000
	if len(args)>0:
		if '-d' in args:
			dotorg = True
		if '-c' in args:
			change = True
		if '-n' in args:
			number = int(args[args.index('-n') + 1])
	return (dotorg, change, number)

def log(dotorg, change, number, wins):
#	logpath = '/home/kiv/mfresults'
	logpath = 'D:\\mhlog.log'
	logtext = ''
	if not dotorg:
		logtext = 'pythonrandom, '
	else:
		logtext += 'randomdotorg, '
	if change:
		logtext += 'change, '
	else:
		logtext += 'not change, '
	logtext += str(number) + ': ' + str(wins) + ' (' + str(wins / float(number) * 100.0) + '%)\n'

	out = open(logpath,'a')
	out.write(logtext)
	out.close

def monthy(change, dotorg, i):
	log = '==TESN#' + str(i) + '\n'
	if dotorg:
		r = randomdotorg.RandomDotOrg()
	else:
		r = random
	#��������� �����
	doors = ['goat-1', 'goat-2', 'car'] #��������, �������� ������ ������ ���� ��� ������� (��� ������ ����)
	r.shuffle(doors)
	log += 'INIT: ' + str(doors) + '\n'
	#�������� �����
	choice = r.choice(doors)
	log += 'CHOICE: ' + str(choice) + '\n'
	#���������� �����
	other = doors
	other.remove(choice)
	log += 'OTHER: ' + str(other) + '\n'
	#��������� �����
	if not 'car' in other:
		opened = r.choice(other)
	else:	
		opened = other[:]
		opened.remove('car')
		opened = opened[0]
	log += 'OPENED: ' + opened + '\n'
	#�������� �����
	if change:
		other.remove(opened)
		choice = other

	log += 'RESULT: ' + str(choice)
	win = False
	if 'car' in choice:
		win = True
	print choice
	return win

dotorg = args()[0]
change = args()[1]
number = args()[2]

wins = 0
for i in range(0, number):
	print str(i) + ': '	
	if monthy(change, dotorg, i):
		wins += 1
	print ' | wins:' + str(wins)
print wins

log(dotorg, change, number, wins)
