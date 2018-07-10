from random import randint

def main():
	correct = 0
	random_number = randint(0,9)
	while True:
		guess_num = input("Guess the number: ")
		if guess_num == random_number:
			correct = 1
			print("Correct!")
			break
		else:
			correct = 0
			print("Wrong, try again!\n")
if __name__ == '__main__':
	main()