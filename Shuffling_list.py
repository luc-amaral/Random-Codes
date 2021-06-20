# Shuffling an order in the list

import random

name1 = (input('Name: '))
print('First name: {}'.format((name1)))
name2 = (input('Name: '))
print('Second name: {}'.format((name2)))
name3 = (input('Name: '))
print('Third name: {}'.format((name3)))
name4 = (input('Name: '))
print('Fourth name: {}'.format((name4)))

Names = [name1, name2, name3, name4]

random.shuffle(Names)
print(Names)
