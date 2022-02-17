from cmath import pi
import math

# Comments

'''
Multi-line
comments
'''

# Basic print

print('Hello World')
print(1+3)

# Variables & adv print
vardas = 'Deividas'
metai = 21

# Method #1
print('Mano vardas ' + vardas)
print('Man yra ' + str(metai))

# Method #2
print(f'Mano vardas {vardas}')
print(f'Man yra + {metai}')
metai = '21'

# Method #3
print('Mano vardas ' .format(vardas))
print('Man yra ' .format(metai))

# Method #4
print('Mano vardas', vardas)
print('Man yra', metai)

# str() | int -> str
# int() | str -> int

# Conversion
print(int(metai) + (2))

# String multiplication
print('-'*20)

# No new line
print('Helo word', end='')
print('It prints on same line')

# Mixing ' "
#print(f'Mano vardas yra {vardas} ir as noriu pasakyti {echo("")}')

# Math
print('2 + 2 = ', 2 + 2)
print('2 - 2 = ', 2 - 2)
print('2 * 2 = ', 2 * 2)
print('2 / 2 = ', 2 / 2)
print('3 ^ 2', math.pow(3, 2))
print('2 % 3 = ', 2 % 3)

# Functions

# Simple function without args
def hello_world():
  print('Hello world from func')
hello_world()

# Simple function with args
def hello(name):
  print(f'Hello, {name}')
hello('Deividas')

def sum(a, b):
  print(f'{a} + {b} = {a + b}')
sum(2, 3)

# TODO: remove this on final push
print('-'*20)

a = input('Pasirink pirma skaiciu: ')
b = input('Pasirink antra skaiciu: ')

def parse(input_string):
  return int(input_string)

sum(parse(a), parse(b))