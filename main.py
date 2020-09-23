# Написать программный код, реализующий простой шифр. 
# (Цезарь, Скитала, Полибий)

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
	word = input('Enter your word: ')
	word = word.lower()
	n = 4
	m = 3
	inp = input('Enter num of <n> and <m> with space: ')
	n = int(inp[:-1]) # столбцы 
	m = int(inp[1:]) # строки 

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
	word = input('Enter your encrypted word: ')
	inp = input('Enter num of <n> and <m> with space: ')
	n = int(inp[:-1]) # столбцы 
	m = int(inp[1:]) # строки 
	del inp

	k = 0
	result = [[ None for i in range(n)] for j in range(m)]
	for j in range(n):
		for i in range(m):
			result[i][j] = word[k]
			k += 1

	for line in result:
		print(line)

def polybius_enc():

	def finder(arr, element):
		for i in range(5):
			try:
				j = abc[i].index(element)
				return i, j
			except:
				pass	

	abc = [
		['a','b','c','d','e'], 
	        ['f','g','h','i','k'],
		['l','m','n','o','p'],
		['q','r','s','t','u'],
		['v','w','x','y','z'],
					]
	msg = 'hello'
	print(finder(abc, 'h'))
	#msg = input('Enter your word: ')
		


def polybius_dec():
	pass

def main():
	print('Choose method')
	print('1: Caesar encrypting\n2: Caesar decryption\n3: Scytale encrypting\n4: Scytale decrypting\n5: Polybius encrypting\n6: Polybius decrypting\n')
	#variant = int(input(''))
	variant = 5
	if variant == 1:
		caesar_enc()
	elif variant == 2:
		caesar_dec()
	elif variant == 3:
		scytale_enc()
	elif variant == 4:
		scytale_dec()
	elif variant == 5:
		polybius_enc()
	elif variant == 6:
		polybius_dec()
	


	
if __name__ == '__main__':
	main()
