# Написать программный код, реализующий простой шифр. (Цезарь, Скитала, Полибий)

import string

def caesar_enc():
	abc = (string.ascii_lowercase)
	word = input('Enter your word: ')
	word = word.lower()
	k = int(input('Enter your key: '))

	result = ''

	for symbol in word:
		position = abc.find(symbol)
		#print(position)
		if position+k >= len(abc):
			result += abc[position+k - len(abc)]
		else:	
			result += abc[position+k]
	
	print('\nYour result is ' + result)

def caesar_dec():
	abc = (string.ascii_lowercase)
	word = input('Enter your encrypted word: ')
	word = word.lower()
	k = int(input('Enter your key: '))

	result = ''

	for symbol in word:
		position = abc.find(symbol)
		#print(position)
		if position+k >= len(abc):
			result += abc[position+k - len(abc)]
		else:	
			result += abc[position-k]
	
	print('\nYour result is ' + result)

def scytale_enc():
	abc = (string.ascii_lowercase)
	#word = input('Enter your word: ')
	word = 'hello_world'
	print('word len =', len(word))
	word = word.lower()
	n = 4
	m = 3
	result = [[ None for i in range(n)] for j in range(m)]
	k = 0

	for i in range(m):
		#print('i:', i)
		for j in range(n):
			#print('j:', j)
			if k >= len(word):
				result[i][j] = '*'
			else:
				result[i][j] = word[k]
			#print('k:', k)
			k += 1

	for line in (result):
		print(line)

	last_result = ''
	for j in range(n):
		for i in range(m):
			last_result += result[i][j]

	print('Your result is: ')
	print(last_result)
	


def scytale_dec():
    pass
	# https://ru.wikipedia.org/wiki/%D0%A1%D0%BA%D0%B8%D1%82%D0%B0%D0%BB%D0%B0


def main():
	print('Choose method')
	print('1: Caesar encrypting\n2: Caesar decryption\n3: Scytale encrypting\n4: Scytale decrypting')
	#variant = int(input(''))
	variant = 3
	if variant == 1:
		caesar_enc()
	elif variant == 2:
		caesar_dec()
	elif variant == 3:
		scytale_enc()
	elif variant == 4:
		scytale_dec()
	
if __name__ == '__main__':
	main()